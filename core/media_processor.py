from pathlib import Path
import shutil

class MediaProcessor:
    def __init__(self, trushes_dir: str = "trushes"):
        self.trushes_path = Path(trushes_dir)
        
        # 分類先のサブディレクトリを定義
        self.image_dir = self.trushes_path / "images"
        self.video_dir = self.trushes_path / "videos"
        self.other_dir = self.trushes_path / "others"

        # フォルダが存在しない場合は自動作成
        for d in [self.image_dir, self.video_dir, self.other_dir]:
            d.mkdir(parents=True, exist_ok=True)

    def process_recovered_files(self):
        """trushes/ 直下のファイルを走査して拡張子ごとに振り分ける"""
        if not self.trushes_path.exists():
            return {"status": "error", "message": "trushes directory not found."}

        results = []
        
        # trushes/ 直下のファイルのみを対象にする（サブフォルダは除外）
        for file_path in self.trushes_path.iterdir():
            if file_path.is_file():
                ext = file_path.suffix.lower()
                action_result = self._dispatch_and_move(file_path, ext)
                results.append(action_result)
                
        return {
            "status": "success",
            "message": "Files processed and classified successfully.",
            "processed": results
        }

    def _dispatch_and_move(self, file_path: Path, ext: str):
        """拡張子を判定して対応するフォルダへ移動する"""
        target_dir = self.other_dir
        file_type = "other"

        # 画像ファイルの判定
        if ext in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
            target_dir = self.image_dir
            file_type = "image"
        # 動画ファイルの判定
        elif ext in [".mp4", ".mov", ".avi", ".mkv"]:
            target_dir = self.video_dir
            file_type = "video"

        # 同名ファイルが存在する場合の対策（上書き防止）
        dest_path = target_dir / file_path.name
        if dest_path.exists():
            dest_path = target_dir / f"{file_path.stem}_copy{ext}"

        # ファイルを移動
        shutil.move(str(file_path), str(dest_path))

        return {
            "file": file_path.name,
            "type": file_type,
            "destination": str(dest_path.relative_to(self.trushes_path))
        }
