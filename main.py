from fastapi import FastAPI
from core.api_router import router as media_router

app = FastAPI(
    title="MediaProjector API",
    description="trushes/内のファイルを拡張子ごとに自動処理するメディア処理システム",
    version="0.1.0"
)

# core 内のAPIルーターを組み込む
app.include_router(media_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to MediaProjector! Check /docs for API documentation."}
