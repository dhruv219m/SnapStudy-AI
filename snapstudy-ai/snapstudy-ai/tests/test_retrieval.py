from snapstudy.retrieval import search

def test_search():
    results = search([
        "Matrices contain rows and columns.",
        "The industrial revolution changed manufacturing."
    ], "What are matrices?", 1)
    assert results
    assert "Matrices" in results[0][0]
