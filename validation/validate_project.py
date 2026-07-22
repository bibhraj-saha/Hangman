"""
Project-wide validation script.
"""

from __future__ import annotations

from pathlib import Path

from src.config import load_config
from src.high_score import HighScoreManager
from src.word_loader import WordLoader

ROOT = Path(".")


def print_header(title: str) -> None:
    print("\n" + "=" * 60)

    print(title)

    print("=" * 60)


def validate_structure() -> None:
    print_header("PROJECT STRUCTURE")

    required = [
        "Home.py",
        "config",
        "data",
        "docs",
        "pages",
        "src",
        "tests",
        "validation",
    ]

    missing = []

    for item in required:
        if not (ROOT / item).exists():
            missing.append(item)

    if missing:
        print("Missing")

        for item in missing:
            print(f"  - {item}")

    else:
        print("All required folders/files found.")


def validate_config() -> None:
    print_header("CONFIGURATION")

    config = load_config()

    print("Game Settings")

    print(config["game"])

    print()

    print("Logging")

    print(config["logging"])


def validate_words() -> None:
    print_header("WORD DATABASE")

    loader = WordLoader()

    print(f"Categories : {len(loader.get_categories())}")

    for category in loader.get_categories():
        print(f" - {category}")


def validate_high_scores() -> None:
    print_header("HIGH SCORES")

    manager = HighScoreManager()

    print(f"Entries : {manager.total_games()}")

    print(f"Best Score : {manager.best_score()}")


def main() -> None:
    validate_structure()

    validate_config()

    validate_words()

    validate_high_scores()

    print_header("VALIDATION COMPLETE")


if __name__ == "__main__":
    main()
