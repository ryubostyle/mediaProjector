"""
=============================================================================
Project: mediaProjector
Module: main.py (クラウド自律駆動版 ── 零点回帰と自動濾過の系譜)
Philosophy: 試行的指向哲学 (Oriented-Philosophia)
=============================================================================
"""

import os
from pathlib import Path
import subprocess


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

    @staticmethod
    def trap(func):
        """すべての予期せぬ揺らぎやエラーを優しく抱擁し、システムを静かに守る防壁"""
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
        root_dir = Path(".")
        ignore_files = {'main.py', '.gitignore', 'README.md'}
        
        entities = [
            e for e in root_dir.iterdir() 
            if e.is_file() and e.name not in ignore_files and not e.name.startswith('.')
        ]
        
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
            return False

        moved_any = False
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
            
            # replace を用いることで、移動と不要な残骸の消去（浄化）をひとつの息吹で完結させる
            entity.replace(destination_path)
            
            print(f"  └─ [精製完了]: {entity.name} ➔ {bean_type} [{destination_path}]")
            moved_any = True
            
        return moved_any


def auto_commit_and_push():
    """クラウド（GitHub）上でファイルが移動した際、自ら変更をGitに刻む思惟"""
    try:
        subprocess.run(["git", "config", "--global", "user.name", "mediaProjector-Bot"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "bot@ryubostyle.github"], check=True)
        subprocess.run(["git", "add", "Assets/", "trushes/"], check=True)
        
        status = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if status.returncode != 0:
            subprocess.run(["git", "commit", "-m", "Auto-cascade: 零れ点を段々畑へ精製しました"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("[クラウド同調]: 濾過の軌跡がGitHubへ美しく刻まれました。")
        else:
            print("[クラウド同調]: 新たな変更の蓄積はありませんでした。")
    except Exception as e:
        print(f"[クラウド同調 揺らぎ]: Git同調中に微細な風を検知しました -> {e}")


if __name__ == "__main__":
    print("=================================================================")
    print(" ryubostyle/mediaProjector : クラウド自律駆動モード ")
    print("=================================================================\n")

    voyage_engine = CascadingFilter(sanctuary="trushes")

    # 巡回、濾過、そしてクラウドへの定住の連鎖
    raw_chaos = voyage_engine.patrol_and_collect()
    has_filtered = voyage_engine.filter_and_cascade(raw_chaos)

    if has_filtered:
        auto_commit_and_push()

    print("\n-----------------------------------------------------------------")
    print(" 母艦は零点に在り。静寂の周回を続けます。")
    print("-----------------------------------------------------------------")
