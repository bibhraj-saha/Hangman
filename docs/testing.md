# Testing Guide

This project uses automated testing and validation to maintain code quality.

---

# Unit Testing

Framework:

- pytest

Run:

```bash
pytest
```

---

# Coverage

Generate coverage reports:

```bash
pytest
```

Reports:

- Terminal coverage
- HTML coverage

Open the HTML report:

```bash
open htmlcov/index.html
```

---

# Validation Scripts

Validate the complete project:

```bash
python -m validation.validate_project
```

Validate the word database:

```bash
python -m validation.validate_word_database
```

Validate high scores:

```bash
python -m validation.validate_high_scores
```

---

# Formatting

Run Black:

```bash
black .
```

---

# Linting

Run Ruff:

```bash
ruff check .
```

---

# Import Sorting

Run:

```bash
isort .
```

---

# Complete Development Validation

Run:

```bash
python dev_tools.py
```

or

```bash
make all
```

---

# Current Test Coverage

Current automated tests include:

- Game Engine
- Word Loader
- High Score Manager
- Configuration
- Utility Functions

Additional UI testing may be added in future versions.