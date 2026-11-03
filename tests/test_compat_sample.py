"""Compat sample regression shield: inventory, scripted drive, compat wiring."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestCompatSample(unittest.TestCase):
    def test_inventory_lists_expected_controls(self):
        proc = subprocess.run(
            [sys.executable, "inventory.py"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stderr[-400:])
        lines = sorted(
            line.strip() for line in proc.stdout.splitlines() if line.strip()
        )
        self.assertIn("button|Save|save-btn", lines)
        self.assertIn("input|Name|name-field", lines)
        self.assertIn("handler|save|on-save", lines)
        for entry in lines:
            parts = entry.split("|")
            self.assertEqual(len(parts), 3)
            self.assertTrue(all(part.strip() for part in parts))

    def test_scripted_drive_prints_world_delta(self):
        proc = subprocess.run(
            [sys.executable, "demo.py", "--scripted"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stderr[-400:])
        self.assertIn("WORLD-DELTA:", proc.stdout)
        deltas = [
            line for line in proc.stdout.splitlines() if "WORLD-DELTA:" in line
        ]
        self.assertGreaterEqual(len(deltas), 2)
        self.assertIn("OK: scripted drive complete", proc.stdout)

    def test_seeded_replay_is_deterministic(self):
        compat = json.loads(
            (ROOT / ".aikit" / "compat.json").read_text(encoding="utf-8")
        )
        seed_flag = (compat.get("seed") or {}).get("flag")
        self.assertEqual(seed_flag, "--seed")
        first = subprocess.run(
            [sys.executable, "demo.py", "--scripted", "--seed", "7"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        second = subprocess.run(
            [sys.executable, "demo.py", "--scripted", "--seed", "7"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(first.returncode, 0, msg=first.stderr[-400:])
        self.assertEqual(second.returncode, 0, msg=second.stderr[-400:])
        first_deltas = sorted(
            line for line in first.stdout.splitlines() if "WORLD-DELTA:" in line
        )
        second_deltas = sorted(
            line for line in second.stdout.splitlines() if "WORLD-DELTA:" in line
        )
        self.assertTrue(first_deltas)
        self.assertEqual(first_deltas, second_deltas)
        self.assertIn("SEED: 7", first.stdout)
        self.assertIn("WORLD-DELTA: counter=7->8", first.stdout)
        for rel_key in ("baseline", "delta"):
            rel = (compat.get("bench") or {}).get(rel_key, "")
            self.assertTrue(rel, msg=f"bench.{rel_key} is empty")
            json.loads((ROOT / rel).read_text(encoding="utf-8"))
        evidence_rel = (compat.get("evidence") or {}).get("file", "")
        self.assertTrue(evidence_rel, msg="evidence.file is empty")
        evidence = json.loads(
            (ROOT / evidence_rel).read_text(encoding="utf-8")
        )
        self.assertEqual(evidence.get("schema"), 1)

    def test_compat_layout_matches_inventory_and_screenshots(self):
        compat = json.loads(
            (ROOT / ".aikit" / "compat.json").read_text(encoding="utf-8")
        )
        layout = json.loads(
            (ROOT / ".aikit" / "layout-map.json").read_text(encoding="utf-8")
        )
        self.assertEqual(compat.get("kind"), "ui")
        self.assertTrue(compat.get("has_ui"))
        shots = compat.get("screenshots", {})
        for key in ("before", "after"):
            rel = shots.get(key, "")
            self.assertTrue(rel, msg=f"screenshots.{key} is empty")
            data = (ROOT / rel).read_bytes()
            self.assertTrue(
                data.startswith(b"\x89PNG\r\n\x1a\n"),
                msg=f"{rel} is not a PNG",
            )
        controls = layout.get("controls", [])
        self.assertGreaterEqual(len(controls), 2)
        names = {item.get("name") for item in controls}
        self.assertIn("save-btn", names)
        self.assertIn("name-field", names)


if __name__ == "__main__":
    unittest.main()
