import sys
from pathlib import Path
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract(pdf):
    return "\n".join((p.extract_text() or "") for p in PdfReader(pdf).pages)

def chunks(text, size=900):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

def main():
    if len(sys.argv) < 3:
        print("Usage: python app.py notes.pdf \"your question\"")
        return
    text = extract(sys.argv[1])
    parts = chunks(text)
    q = sys.argv[2]
    vec = TfidfVectorizer(stop_words="english")
    X = vec.fit_transform(parts + [q])
    scores = cosine_similarity(X[-1], X[:-1]).ravel()
    for i in scores.argsort()[::-1][:3]:
        print(f"\n--- Relevant passage {i+1} ---\n{parts[i]}")
    print("\nNext step: connect a compact local LLM for grounded answer generation.")

if __name__ == "__main__":
    main()
