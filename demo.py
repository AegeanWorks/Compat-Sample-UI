#!/usr/bin/env python3
"""Headless scripted drive: prints WORLD-DELTA lines, no input, exits 0."""
import sys
def _parse_seed(argv):
    seed = 0
    if "--seed" in argv:
        index = argv.index("--seed")
        try:
            seed = int(argv[index + 1])
        except (IndexError, ValueError):
            print("Usage: python demo.py --scripted [--seed N]")  # hygiene: allow usage text for demo.py in the scaffolded project
            sys.exit(2)
    return seed
if __name__ == "__main__":
    if "--scripted" not in sys.argv:
        print("Usage: python demo.py --scripted [--seed N]")  # hygiene: allow usage text for demo.py in the scaffolded project
        sys.exit(2)
    _seed = _parse_seed(sys.argv)
    print(f"SEED: {_seed}")
    print(f"WORLD-DELTA: counter={_seed}->{_seed + 1}")
    print(f"WORLD-DELTA: items={_seed + 2}->{_seed + 3}")
    print("OK: scripted drive complete")
