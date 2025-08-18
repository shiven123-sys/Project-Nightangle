import io
import streamlit as st
from PyPDF2 import PdfReader
import torch
from sentence_transformers import SentenceTransformer, util

# --------------------------
# Load pretrained model
# --------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

model = load_model()

# --------------------------
# PDF se text nikalna
# --------------------------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

# --------------------------
# Streamlit UI
# --------------------------
st.title("🕊️ Project Nightingale – Resume Screener")

jd = st.text_area("📄 Paste Job Description (JD)", height=150)

uploaded_files = st.file_uploader(
    "👤 Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

top_k = st.slider("Top candidates to show", 1, 10, 5)

if st.button("🔎 Rank Candidates"):
    if not jd:
        st.warning("Pehle JD paste karo.")
        st.stop()
    if not uploaded_files:
        st.warning("At least 1 PDF resume upload karo.")
        st.stop()

    # Resumes text extract
    resumes = []
    for f in uploaded_files:
        text = extract_text_from_pdf(io.BytesIO(f.read()))
        if len(text) > 50:  # filter out empty PDFs
            resumes.append({"name": f.name, "text": text})

    if not resumes:
        st.error("Resumes ka text extract nahi ho paaya.")
        st.stop()

    # Encode
    jd_emb = model.encode(jd, convert_to_tensor=True, normalize_embeddings=True)
    res_embs = model.encode([r["text"] for r in resumes],
                            convert_to_tensor=True, normalize_embeddings=True)

    # Similarity
    cos_scores = util.cos_sim(jd_emb, res_embs)[0]
    top_results = torch.topk(cos_scores, k=min(top_k, len(resumes)))

    st.subheader("🏆 Top Candidates")
    for score, idx in zip(top_results.values, top_results.indices):
        candidate = resumes[int(idx)]
        st.markdown(f"**{candidate['name']}** — Similarity: `{score:.4f}`")
        st.text(candidate["text"][:300] + "...")