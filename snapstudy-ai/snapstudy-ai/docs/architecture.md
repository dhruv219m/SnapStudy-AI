# Architecture

The prototype keeps document processing and retrieval on the local machine.

PDF notes -> text extraction -> chunking -> TF-IDF retrieval -> source passages

The planned generation layer will use a compact local language model. The production target is Snapdragon-powered HP PCs, with model/runtime selection and NPU acceleration validated through actual device testing.

## Evaluation
- retrieval relevance
- response latency
- memory usage
- battery/power behavior
- answer quality
- offline reliability
