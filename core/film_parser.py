from pathlib import Path
import yaml


class FilmParser:
    """mediaProjectorのフィルムYAMLをパースし、シーンデータを管理するクラス"""

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)
        self.data = self._load_yaml()

    def _load_yaml(self) -> dict:
        """YAMLファイルを安全に読み込む"""
        if not self.file_path.exists():
            raise FileNotFoundError(f"指定されたファイルが見つかりません: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                return yaml.safe_load(f) or {}
            except yaml.YAMLError as e:
                print(f"YAMLのパースに失敗しました: {e}")
                return {}

    def get_project_metadata(self) -> dict:
        """プロジェクト全体のメタデータを返す"""
        return self.data.get("project", {})

    def get_scenes(self) -> list:
        """全シーンのリストを返す"""
        return self.data.get("scenes", [])

    def display_parsed_info(self):
        """パース結果をコンソールに美しく展開する（デバッグ・確認用）"""
        project = self.get_project_metadata()
        print("=== 🎬 プロジェクト情報 ===")
        print(f"タイトル: {project.get('title')}")
        print(f"テーマ: {project.get('theme')}")
        print(f"総尺: {project.get('total_duration_sec')} 秒")
        print(f"作者: {project.get('author')}")
        print("-" * 30)

        print("=== 🎞️ シーン別データ構造 ===")
        for scene in self.get_scenes():
            print(f"ID: {scene.get('id')} | タイトル: {scene.get('title')}")
            print(f"  時間: {scene.get('start_sec')}s - {scene.get('end_sec')}s")
            if "dialogue_exchange" in scene:
                for d in scene["dialogue_exchange"]:
                    print(f"  [{d.get('speaker')}]: {d.get('line')}")
            elif "dialogue" in scene:
                print(f"  [台詞]: {scene.get('dialogue')}")
            elif "narration" in scene:
                print(f"  [ナレーション]: {scene.get('narration')}")
            print("-" * 20)


# テスト実行用のエントリポイント
if __name__ == "__main__":
    # trushes/others/film.yaml をターゲットに指定
    target_yaml = Path("trushes/others/film.yaml")
    parser = FilmParser(target_yaml)
    parser.display_parsed_info()
