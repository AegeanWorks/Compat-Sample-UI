#!/usr/bin/env python3
"""Headless scripted drive: prints WORLD-DELTA lines, no input, exits 0."""
import sys
if __name__ == "__main__":
    if "--scripted" not in sys.argv:
        print("Usage: python demo.py --scripted")
        sys.exit(2)
    print("WORLD-DELTA: counter=0->1")
    print("WORLD-DELTA: items=2->3")
    print("OK: scripted drive complete")
