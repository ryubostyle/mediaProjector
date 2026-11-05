"""
=============================================================================
Project: mediaProjector
Module: main.py (零点回帰 ── 単一の母艦に宿る多段式カスケードの思惟)
Philosophy: 試行的指向哲学 (Oriented-Philosophia)
=============================================================================
"""

import os
from pathlib import Path


class ErrorTrapper:
    """
    【第1階層：母体・根源の零点（ErrorTrapper）】
    すべての混沌や例外を包み込む零点の母体。
    存在しない空間（trushes/）を自らの意志で創生し、静寂を守ります。
    """
    def __init__(self, sanctuary: str = "trushes"):
        self.sanctuary = Path(sanctuary)
        self._manifest_sanctuary()

    def _manifest_sanctuary(self):
        if not self.sanctuary.exists():
            self.sanctuary.mkdir(parents=True, exist_ok=True)
            print(f"[零点創生]: 空間 '{self.sanctuary}' が顕現しました。")

    def trap(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[零点抱擁]: 揺らぎをトラップし零点へ還しました -> {e}")
                return None
        return wrapper


class RecyclingCar(ErrorTrapper):
    """
    【第2階層：回収・見張り役（RecyclingCar）】
    零点の荒野を巡回し、生の零れ点（ファイル）を見つけ出すオブジェ。
    """
    def __init__(self, sanctuary: str = "trushes"):
        super().__init__(sanctuary)
        print("[回廊巡回]: 見張り車（rycyclingCar）が起動しました。")

    @ErrorTrapper.trap
    def patrol_and_collect(self):
        entities = [e for e in self.sanctuary.iterdir() if e.is_file()]
        if not entities:
            return []
        print(f"\n[混沌検知]: {len(entities)} 個の零れ点をキャッチしました。")
        return entities


class CascadingFilter(RecyclingCar):
    """
    【第3階層：濾過・精製の系譜（CascadingFilter）】
    ロート状のカスケードで粗目から細目へ挽き分け、Beansとして定住させる最下層。
    """
    def __init__(self, sanctuary: str = "trushes"):
        super().__init__(sanctuary)
        print("[段々畑濾過]: ロート状のカスケードシステムが展開されました。")

    def filter_and_cascade(self, entities):
        if not entities:
            print("[巡回静寂]: ゴミはありません。トークンは穏やかに周回しています。")
            return

        for entity in entities:
            suffix = entity.suffix.lower()
            
            if suffix in ['.jpg', '.png', '.jpeg', '.webp']:
                dest = Path("Assets/Images")
                bean_type = "光の粒子（Images Bean）"
            elif suffix in ['.mp3', '.wav', '.m4a']:
                dest = Path("Assets/Audios")
                bean_type = "風の響き（Audios Bean）"
            elif suffix in ['.mp4', '.mov']:
                dest = Path("Assets/Videos")
                bean_type = "時の鏡（Videos Bean）"
            else:
                dest = Path("Assets/Others")
                bean_type = "名もなき土壌（Others Bean）"

            dest.mkdir(parents=True, exist_ok=True)
            destination_path = dest / entity.name
            entity.rename(destination_path)
            print(f"  └─ [精製完了]: {entity.name} ➔ {bean_type} [{destination_path}]")


if __name__ == "__main__":
    print("=================================================================")
    print(" ryubostyle/mediaProjector : 零点回帰の航海モード ")
    print("=================================================================\n")

    # 零点からカスケードを起動
    voyage_engine = CascadingFilter(sanctuary="trushes")

    # 巡回と濾過の遂行
    raw_chaos = voyage_engine.patrol_and_collect()
    voyage_engine.filter_and_cascade(raw_chaos)

    print("\n-----------------------------------------------------------------")
    print(" 母艦は零点に在り。静寂の周回を続けます。")
    print("-----------------------------------------------------------------")
