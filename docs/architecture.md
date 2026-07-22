# Architecture

## High-Level Architecture

```text
                           User
                             │
                             ▼
                    Streamlit Web UI
                             │
                             ▼
                 Session & Game Manager
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
      Game Engine      Word Loader     High Score Manager
            │                │                │
            ▼                ▼                ▼
      Game State      JSON Word Files   high_scores.json
            │
            ▼
       Scoring System
```

---

## Project Structure

```text
Hangman/
│
├── app.py
├── pages/
│   ├── 1_Play_Game.py
│   ├── 2_Leaderboard.py
│   └── 3_About.py
│
├── src/
│   ├── game.py
│   ├── word_loader.py
│   ├── high_score.py
│   ├── scoring.py
│   ├── validator.py
│   ├── logger.py
│   ├── config.py
│   ├── constants.py
│   ├── utils.py
│   ├── models.py
│   └── ui/
│
├── data/
│   ├── words/
│   └── high_scores.json
│
├── tests/
├── validation/
├── docs/
├── config/
├── assets/
└── requirements.txt
```

---

## Design Principles

- Modular architecture
- Separation of concerns
- Object-oriented design
- Persistent high-score storage
- Configuration-driven behaviour
- Automated validation
- Automated testing
- Modern Streamlit user interface
- Production-quality project structure

---

## Technology Stack

### Backend

- Python 3.14
- Object-Oriented Programming
- JSON
- Logging

### Frontend

- Streamlit
- Custom CSS
- Session State

### Quality

- pytest
- pytest-cov
- Ruff
- Black
- isort
- pre-commit

### Packaging

- setuptools
- build
- twine