# BuffettStack

## Disclaimer

These are personal research tools, not financial advice, investment advice, or
a recommendation to buy or sell any security. Use your own judgment and verify
all outputs against primary sources before making investment decisions.

Codex skills for systematic investment research, inspired by Warren Buffett,
Charlie Munger, Benjamin Graham, and Philip Fisher.

This project is meant to be shared freely with people who want a more
disciplined way to study businesses before making investment decisions. The
skills help turn annual filings and financial statements into source-grounded
research outputs, with quality-control and audit passes built into the workflow.

These tools are not a stock picker and they are not financial advice. They are
personal research aids for reading better, checking assumptions, and keeping an
investment process organized.

## Install

This is a Codex skills bundle, not a Python or npm package.

Clone the repository:

```bash
git clone <repo-url>
cd BuffettStack
```

To make the skills available in Codex across projects, copy them into your
Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R .codex/skills/* ~/.codex/skills/
```

Then restart Codex so it reloads available skills.

You can also work directly from this repository if your Codex setup loads
workspace-local skills from `.codex/skills/`.

## Quick Start

Ask Codex to run one of the skills by name:

```text
$fetch-financials CME
$synthesize-annual-filing CME 2024
$calc-oe CME
```

Research outputs use `./research/` by default. You can override that with
`--research-base /path/to/research`, the `RESEARCH_BASE_PATH` environment
variable, or `.codex/settings.local.json` at `env.RESEARCH_BASE_PATH`.

`$fetch-financials` uses FMP when `FMP_API_KEY` is set. Without a token, it
falls back to free SEC EDGAR Company Facts with Yahoo Finance as supplemental
profile and market metadata.

## Skills

| Skill | Purpose |
| --- | --- |
| `$synthesize-annual-filing` | Synthesize one annual filing into an analyst memo with QC and audit passes. |
| `$fetch-financials` | Fetch and store financial statements as canonical JSON plus Markdown summary, using FMP or free SEC-first data. |
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
example-outputs/
└── synthesize-annual-filing/
```

## Notes

- Bundled scripts should be used instead of calling data providers directly.
- Keep generated research outputs out of git, except curated examples under
  `example-outputs/`.

## License

MIT License. See [LICENSE](LICENSE).
