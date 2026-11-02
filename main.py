from pathlib import Path
from core.film_parser import FilmParser


def main():
    print("=== mediaProjector: パイプライン起動 ===")

    # trushes/others/ に着地した film.yaml をターゲットにする
    target_yaml = Path("trushes/others/film.yaml")

    if target_yaml.exists():
        print(f"ターゲットファイルを検知しました: {target_yaml}")
        # パーサーを初期化してデータを読み込む
        parser = FilmParser(target_yaml)
        # パースされた内容を展開・確認
        parser.display_parsed_info()

        # TODO: ここから先（次の生成パイプライン：音声合成やシーンごとの処理）へバトンを渡す
        scenes = parser.get_scenes()
        print(
            f"-> 成功: 全 {len(scenes)} シーンのデータ抽出が完了しました。"
        )
    else:
        print(
            f"待機中: {target_yaml} が見つかりません。ファイルがソートされるのを待っています..."
        )


if __name__ == "__main__":
    main()
