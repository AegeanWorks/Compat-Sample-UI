# Compat Sample UI

[![Built with AIKit](https://img.shields.io/badge/built%20with-AIKit-6f42c1)](https://github.com/AegeanWorks/AIKit)

UI sample for AI-compat proof

## ⚡ 30-Second Cold-Start Quick Reference

- **Runtime Prerequisites**: Python 3.10+ (stdlib only, no extra dependencies)
- **Canonical Regression Shield Gate**:
  ```bash
  python -m unittest discover
  ```

### 🛠️ AIKit Commands (run from the AIKit folder)
| Role | Command |
|---|---|
| Status, task and gates | `python aikit.py status compat-sample-ui` |
| Phase 4: every gate | `python aikit.py check compat-sample-ui` |
| Repair memory and map, then check | `python aikit.py fix compat-sample-ui` |
| Resume an interrupted task | `python aikit.py resume compat-sample-ui` |

## 📦 What's Inside

```text
compat-sample-ui/
├── .gitignore                <- transient AIKit state excluded
├── LICENSE                   <- Aegean License 1.1 (AL-1.1): free personal use
├── COMMERCIAL.md             <- Commercial licensing terms
├── LICENSES/                 <- REUSE license texts
├── REUSE.toml                <- Machine-readable SPDX metadata
├── README.md
├── demo.py                   <- scripted WORLD-DELTA drive (compat)
├── inventory.py              <- UI inventory kind|name|locator (compat)
├── assets/                   <- logo, social preview, screenshots
├── tests/                    <- regression shield (unittest)
└── .aikit/                   <- this project's memory: record, ledger, decisions
```

## 📜 License

Free for personal use under the Aegean License 1.1 (AL-1.1); see [LICENSE](LICENSE). Any commercial use needs the Aegean Commercial License 1.0 (ACL-1.0); see [COMMERCIAL.md](COMMERCIAL.md).
