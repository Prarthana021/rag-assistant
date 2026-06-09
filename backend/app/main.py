from fastapi import FastAPI

app = FastAPI(
    title="Personal Career RAG Assistant API",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Report whether the API process is available."""
    return {"status": "ok"}
