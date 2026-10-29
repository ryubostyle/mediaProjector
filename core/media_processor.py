from pathlib import Path

class MediaProcessor:
    def __init__(self, trushes_dir: str = "trushes"):
        self.trushes_path = Path(trushes_dir)

    def process_recovered_files(self):
        """trushes/ 内のファイルを走査して拡張子ごとに処理を振り分ける"""
        if not self.trushes_path.exists():
            return {"status": "error", "message": "trushes directory not found."}

        results = []
        for file_path in self.trushes_path.iterdir():
            if file_path.is_file():
                ext = file_path.suffix.lower()
                res = self._dispatch_handler(file_path, ext)
                results.append(res)
                
        return {"status": "success", "processed": results}

    def _dispatch_handler(self, file_path: Path, ext: str):
        # 拡張子に応じたハンドリング
        if ext in [".jpg", ".jpeg", ".png", ".webp"]:
            return {"file": file_path.name, "type": "image", "status": "handled"}
        elif ext in [".mp4", ".mov", ".avi"]:
            return {"file": file_path.name, "type": "video", "status": "handled"}
        else:
            return {"file": file_path.name, "type": "unknown", "status": "skipped"}
