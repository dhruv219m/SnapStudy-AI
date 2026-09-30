import tempfile
from pathlib import Path
import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="SnapStudy AI", page_icon="📚", layout="wide")
st.title("📚 SnapStudy AI")
st.caption("Private, local-first study assistant prototype")

def extract_pdf(path):
    return "\n".join((p.extract_text() or "") for p in PdfReader(path).pages)

def make_chunks(text, size=180, overlap=35):
    words = text.split()
    step = max(1, size-overlap)
    return [" ".join(words[i:i+size]) for i in range(0, len(words), step)
            if words[i:i+size]]

if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "sources" not in st.session_state:
    st.session_state.sources = []

with st.sidebar:
    st.header("Study material")
    uploads = st.file_uploader("Upload PDF notes", type="pdf", accept_multiple_files=True)
    if st.button("Index documents", type="primary"):
        chunks, sources = [], []
        for upload in uploads or []:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                f.write(upload.getbuffer())
                temp = f.name
            try:
                text = extract_pdf(temp)
            finally:
                Path(temp).unlink(missing_ok=True)
            for chunk in make_chunks(text):
                chunks.append(chunk)
                sources.append(upload.name)
        st.session_state.chunks = chunks
        st.session_state.sources = sources
        st.success(f"Indexed {len(chunks)} passages locally.")

question = st.text_input("Ask your notes", placeholder="Explain the main concept in simple terms")

if question and st.session_state.chunks:
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(st.session_state.chunks)
    q = vectorizer.transform([question])
    scores = cosine_similarity(q, matrix).ravel()
    for rank, idx in enumerate(scores.argsort()[::-1][:5], 1):
        with st.expander(f"{rank}. {st.session_state.sources[idx]} — relevance {scores[idx]:.2f}", expanded=rank == 1):
            st.write(st.session_state.chunks[idx])
elif question:
    st.warning("Upload and index PDF notes first.")

st.divider()
st.markdown("### Snapdragon optimization roadmap")
st.markdown("1. Integrate a compact quantized local language model\n"
            "2. Evaluate Qualcomm AI Hub-compatible deployment\n"
            "3. Benchmark CPU/GPU/NPU execution on real Snapdragon hardware\n"
            "4. Measure latency, memory, power and answer quality")
