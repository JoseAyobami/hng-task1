from fastapi import FastAPI
from route import router as strings_router
import os
import uvicorn

app = FastAPI(title="String Analyzer Service")

app.include_router(strings_router)


@app.get("/")
def health():
	return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
