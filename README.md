# 🎵 Harmonia

<p align="center">
  <a href="#russian">🇷🇺 Русский</a> &nbsp;|&nbsp; <a href="#english">🇬🇧 English</a>
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green?style=flat-square)](https://python.org)
[![GitHub stars](https://img.shields.io/github/stars/zad111ak-ai/harmonia?style=social)](https://github.com/zad111ak-ai/harmonia)
[![GitHub contributors](https://img.shields.io/github/contributors/zad111ak-ai/harmonia)](https://github.com/zad111ak-ai/harmonia/graphs/contributors)

**Loop collector and optimizer for LLM workloads.**

No cloud, no SaaS, no config fatigue. One binary, one database, one command.

---

<a id="russian"></a>
## 🇷🇺 О проекте

**Harmonia** — анализатор петель коррекции в LLM-агентах. Сидит между твоим агентом и любым OpenAI-совместимым API. Отслеживает каждый вызов, находит петли коррекции и рефлексии, анализирует их эффективность и даёт конкретные рекомендации.

### Зачем

LLM-агенты делают тысячи API-вызовов. Многие из них — петли коррекции: агент спрашивает, проверяет, чинит, спрашивает снова, чинит снова. Каждая итерация стоит токенов и времени. Но никто не видит внутренности этих петель.

Harmonia даёт рентгеновское зрение:

- Сколько итераций в петле?
- Какие модели используются?
- Где узкие места?
- Какие петли можно сократить вдвое?

### Быстрый старт

```bash
pip install harmonia

# Запуск трекинга
harmonia track --label my-agent

# Или прокси (перехватывает API-вызовы в реальном времени)
harmonia proxy --port 8090
# Направь агента на http://127.0.0.1:8090/v1

# Анализ сессии
harmonia optimize

# Визуализация (Mermaid-граф)
harmonia viz

# Список сессий
harmonia sessions

# Бенчмарк моделей
harmonia models
```

### Все команды

| Команда | Описание |
|---|---|
| `harmonia track --label` | Запуск трекинга сессии |
| `harmonia proxy --port` | Прокси-режим (перехват API) |
| `harmonia optimize` | Анализ петель и рекомендации |
| `harmonia viz` | Визуализация как Mermaid-граф |
| `harmonia sessions` | Список всех сессий |
| `harmonia models` | Бенчмарк моделей |

### Детекция петель

Harmonia автоматически находит петли коррекции — цепочки LLM-вызовов, где результат одного кормится обратно как вход для следующего. Для каждой петли reports:

- Количество итераций
- Общая длительность
- Используемая модель
- Статус сходимости
- Quality score

### Хранение

Все данные локально в `~/.harmonia/harmonia.db` (SQLite). Ничего не покидает твой компьютер.

### API-совместимость

Работает с любым OpenAI-совместимым эндпоинтом:

```bash
export HARMANIA_API_URL=http://localhost:3000/v1
export HARMANIA_API_KEY=sk-...
```

Или используй прокси-режим для прозрачного перехвата трафика без изменения клиентского кода.

---

<a id="english"></a>
## 🇬🇧 About

**Harmonia** sits between your agent and any OpenAI-compatible API. It tracks every call, detects correction and reflection loops, analyzes their efficiency, and gives actionable recommendations — all from a single CLI command.

### Why

LLM agents run thousands of API calls. Many of those calls are correction loops — the agent asks, checks, fixes, asks again, fixes again. Each iteration costs time and tokens. But nobody can see inside those loops.

Harmonia gives you X-ray vision into your agent's internals:

- How many iterations per loop?
- Which models are being used in each loop?
- Where are the bottlenecks?
- Which loops could be cut in half?

### Quick Start

```bash
pip install harmonia

# Start a tracking session
harmonia track --label my-agent

# Or start a proxy (intercepts API calls in real-time)
harmonia proxy --port 8090
# Point your agent to http://127.0.0.1:8090/v1

# Analyze a session
harmonia optimize

# Visualize as Mermaid graph
harmonia viz
```

### Loop Detection

Harmonia automatically detects correction loops — chains of LLM calls where the output of one is fed back as input for refinement. For each loop it reports:

- Number of iterations
- Total duration
- Model used
- Convergence status
- Quality score

### Storage

All data is stored locally in `~/.harmonia/harmonia.db` (SQLite). No data ever leaves your machine.

### API Compatibility

Works with any OpenAI-compatible endpoint:

```bash
export HARMANIA_API_URL=http://localhost:3000/v1
export HARMANIA_API_KEY=sk-...
```

Or use the proxy mode to transparently intercept traffic without modifying your client code.

---

## 💸 Donations / Донаты

| Валюта / Currency | Адрес / Address |
|---|---|
| **BTC** | `bc1qd8sa7e4f696wmcyszuxh9snqt2n66zrhz9g80j` |
| **ETH** | `0xD26f0efE6A8F11e127c3Af3D6163BD458a1693c3` |
| **USDT (TON)** | `UQAoI2i8P9-JeZhvGSUwKnymVyY5cb-1Rg7pdqoWMNena7DP` |
| **SOL** | `99EtqBVTeF5UNp9a1oPi18iVXbXptTG7YQ6JeJvXMUJK` |

---

## License

MIT
