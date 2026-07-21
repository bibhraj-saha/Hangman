"""
Engine validation.
"""

from src.game import GameEngine
from src.word_loader import WordLoader

loader = WordLoader()

entry = loader.get_random_word(
    "Animals",
    "Easy",
)

engine = GameEngine(entry)

print("=" * 60)
print("ENGINE VALIDATION")
print("=" * 60)

print(f"Category      : {entry.category}")
print(f"Difficulty    : {entry.difficulty}")
print(f"Description   : {entry.description}")
print(f"Word Length   : {len(entry.word)}")

print()
print("Initial Board")
print(engine.current_word())

print()

engine.guess(entry.word[0])

print("After First Guess")
print(engine.current_word())

print()

print(f"Remaining Attempts : {engine.state.remaining_attempts}")
print(f"Won               : {engine.is_won()}")
print(f"Lost              : {engine.is_lost()}")