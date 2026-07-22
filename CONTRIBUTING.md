# Contributing

Thank you for your interest in contributing to this project.

## Development Setup

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd Hangman
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run Home.py
```

---

## Code Quality

Before every commit run:

```bash
python dev_tools.py
```

or

```bash
make all
```

---

## Style Guide

This project uses:

- Black
- Ruff
- isort
- pytest

Please ensure all checks pass before submitting changes.

---

## Pull Requests

- Keep pull requests focused.
- Write descriptive commit messages.
- Update documentation if required.