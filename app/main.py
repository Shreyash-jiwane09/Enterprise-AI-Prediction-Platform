from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Prediction Platform",
    description="Production-ready FastAPI backend for AI prediction services.",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """
    Root endpoint.
    """
    return {"message": "Welcome to Enterprise AI Prediction Platform"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    """
    return {"status": "healthy"}