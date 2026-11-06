#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manager.py - 琉坊スタイル独立映写機エンジン (Ryubo Theater Projector)
Target Repository: ryubostyle/mediaProjector
Description: holographic.yml を読み込み、ホログラフィックな展示パネルへ詩的に投影する
"""

import yaml
from pathlib import Path

class RyuboProjector:
    def __init__(self, yaml_path="holographic.yml"):
        self.yaml_path = Path(yaml_path)
        self.config = self._load_scenario()

    def _load_scenario(self):
        if not self.yaml_path.exists():
            print(f"[警告]: シナリオデータ {self.yaml_path} が見つかりません。")
            return {}
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def boot_projection(self):
        meta = self.config.get("project_meta", {})
        prologue = self.config.get("prologue", {})
        movements = self.config.get("movements", [])
        epilogue = self.config.get("epilogue", {})

        if not meta:
            print("投影すべきシナリオデータが空です。映写機は静寂を保ちます。")
            return

        print(f"=== {meta.get('target_repository', 'Ryubo Project')} Holographic Projection ===")
        print(f"Atmosphere: {meta.get('base_atmosphere')}")
        print(f"Narrator: {meta.get('narrator_profile')}\n")

        print(f"【プロローグ】 ({prologue.get('timestamp')} @ {prologue.get('location')})")
        print(f"景観: {prologue.get('visual_cue')}")
        print(f"台詞: {prologue.get('dialog_text')}\n")

        for mov in movements:
            print(f"--- [{mov.get('chapter')}] {mov.get('subtitle')} ---")
            print(f"観測対象: {mov.get('target')}")
            for measure in mov.get("measures", []):
                print(f"  [第{measure.get('id')}小節] {measure.get('title')}")
                print(f"    - ノード種別: {measure.get('node_type')}")
                print(f"    - 役割と仕事: {measure.get('role_and_task')}")
                print(f"    - 挙動: {measure.get('behavior')}")
            print()

        print(f"【エピローグ】")
        print(f"結論: {epilogue.get('conclusion')}")
        print(f"Git Log: {epilogue.get('commit_log')}")
        print("=== Projection Completed. 母艦は零点に在り。 ===")

if __name__ == "__main__":
    projector = RyuboProjector("holographic.yml")
    projector.boot_projection()
