# Harmonia

**Loop collector and optimizer for LLM workloads.**

Harmonia sits between your agent and any OpenAI-compatible API. It tracks every call, detects correction and reflection loops, analyzes their efficiency, and gives actionable recommendations — all from a single CLI command.

No cloud, no SaaS, no config fatigue. One binary, one database, one command.

---

## Why

LLM agents run thousands of API calls. Many of those calls are correction loops — the agent asks, checks, fixes, asks again, fixes again. Each iteration costs time and tokens. But nobody can see inside those loops.

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"/></a>
  <img src="https://img.shields.io/badge/python-3.8+-green?style=flat-square" alt="Python 3.8+"/>
  <a href=".github/FUNDING.yml"><img src="https://img.shields.io/badge/sponsor-donate-purple?style=flat-square" alt="Sponsor"/></a>
</p>

Harmonia gives you X-ray vision into your agent's internals:

- How many iterations per loop?
- Which models are being used in each loop?
- Where are the bottlenecks?
- Which loops could be cut in half?

---

## Usage

```bash
# Start a tracking session
harmonia track --label my-agent

# Or start a proxy (intercepts API calls in real-time)
harmonia proxy --port 8090

# Point your agent to http://127.0.0.1:8090/v1

# Analyze a session
harmonia optimize

# Visualize a session as a Mermaid graph
harmonia viz

# List all sessions
harmonia sessions

# Benchmark models
harmonia models
```

---

## Loop Detection

Harmonia automatically detects correction loops — chains of LLM calls where the output of one is fed back as input for refinement. For each loop it reports:

- Number of iterations
- Total duration
- Model used
- Convergence status
- Quality score

---

## Storage

All data is stored locally in `~/.harmonia/harmonia.db` (SQLite). No data ever leaves your machine.

---

## API Compatibility

Works with any OpenAI-compatible endpoint. Set your API URL and key via environment variables:

```bash
export HARMANIA_API_URL=http://localhost:3000/v1
export HARMANIA_API_KEY=sk-...
```

Or use the proxy mode to transparently intercept traffic without modifying your client code.

---

## Support

If Harmonia saves you time, consider a donation:

| Asset | Address |
|---|---|
| **TON** | `UQBLEYICSbxKZAajJspddpVYEFtvCcnp7gUpHDZpTChqqAoC` |
| **USDT (TON)** | `UQAoI2i8P9-JeZhvGSUwKnymVyY5cb-1Rg7pdqoWMNena7DP` |
| **Ethereum (ERC-20)** | `0xD26f0efE6A8F11e127c3Af3D6163BD458a1693c3` |
| **Bitcoin** | `bc1qd8sa7e4f696wmcyszuxh9snqt2n66zrhz9g80j` |

Or just star the repo — that helps too!

---

## License

MIT
