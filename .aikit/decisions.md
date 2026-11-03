# Decisions

Why this project is built the way it is, oldest first. One entry per decision that changes a
contract, a dependency, a data format or the architecture; IDs are consecutive and never reused.

<!-- Entry format:
### ADR-NNN: <decision in one line>
- **Date**: YYYY-MM-DD
- **Status**: Accepted
- **Context**: <what forced the decision>
- **Decision**: <what was decided>
- **Consequences**: <what follows, including what it costs>
-->

### ADR-001: Sync compat contract to current scaffold with seeded replay
- **Date**: 2026-11-03
- **Status**: Accepted
- **Context**: Audit of wave 0 + 2 commits found demo.py and compat.json predating the current scaffold: no --seed flag, no seed/bench/evidence sections, and missing replay/bench/evidence files, while 5/5 gates still passed because those checks are optional when absent.
- **Decision**: Align to scripts/project_compat.py scaffold for kind ui: demo.py parses --seed and prints SEED plus seeded WORLD-DELTA lines, compat.json declares seed/bench/evidence, and .aikit/replay.log, bench-baseline.json, bench-delta.json, evidence.json are added; regression shield gains a seeded-replay determinism test.
- **Consequences**: Seeded replay is deterministic and verifiable, bench/evidence hooks exist for future runs; cost is one extra test (~2 subprocess runs, <500ms) and four small JSON/log files.
