# Investing Skills

Codex skills for systematic investment research, inspired by Warren Buffett,
Charlie Munger, Benjamin Graham, and Philip Fisher.

This repository contains only the Codex-migrated skills from the original
`investment-research-skills` project. Source commit: `3556b00`.

## Skills

| Skill | Purpose |
| --- | --- |
| `$synthesize-annual-filing` | Synthesize one annual filing into an analyst memo with QC and audit passes. |
| `$fetch-financials` | Fetch and store FMP financial statements as canonical JSON plus Markdown summary. |
| `$calc-oe` | Calculate historical owner's earnings from financial statement JSON and annual filing memos. |
| `$quality-control` | Re-read sources and surgically fix content gaps in a research output. |
| `$audit-output` | Check a research output against its skill requirements and fix compliance violations. |

## Layout

```text
.codex/
└── skills/
    ├── audit-output/
    ├── calc-oe/
    ├── fetch-financials/
    ├── quality-control/
    └── synthesize-annual-filing/
```

## Notes

- Skills expect a research root configured through
  `.claude/settings.local.json` as `env.RESEARCH_BASE_PATH`.
- Bundled scripts should be used instead of calling vendor APIs directly.
- `fetch-financials` requires an `FMP_API_KEY` environment variable.
