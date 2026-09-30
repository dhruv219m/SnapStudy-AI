from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search(passages, query, top_k=5):
    if not passages:
        return []
    v = TfidfVectorizer(stop_words="english")
    m = v.fit_transform(passages)
    q = v.transform([query])
    scores = cosine_similarity(q, m).ravel()
    return [(passages[i], float(scores[i])) for i in scores.argsort()[::-1][:top_k]]
