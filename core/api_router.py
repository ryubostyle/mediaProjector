from fastapi import APIRouter, HTTPException
from core.media_processor import MediaProcessor

router = APIRouter(prefix="/media", tags=["media"])
processor = MediaProcessor(trushes_dir="trushes")

@router.post("/process-trushes")
def api_process_trushes():
    """trushes/ 内のファイルをAPI経由で一括処理する"""
    try:
        result = processor.process_recovered_files()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
