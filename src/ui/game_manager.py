"""
Streamlit game management.
"""

from src.game import GameEngine
from src.word_loader import WordLoader

loader = WordLoader()


def start_new_game(
    player_name: str,
    category: str,
    difficulty: str,
):

    entry = loader.get_random_word(
        category,
        difficulty,
    )

    engine = GameEngine(entry)

    return engine
