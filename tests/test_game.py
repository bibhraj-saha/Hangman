"""
Tests for GameEngine.
"""

from __future__ import annotations


def test_game_initialization(game):
    assert game.state.word == "python"

    assert game.state.remaining_attempts == 6


def test_correct_guess(game):
    game.guess("p")

    assert "p" in game.state.guessed_letters


def test_wrong_guess(game):
    attempts = game.state.remaining_attempts

    game.guess("z")

    assert game.state.remaining_attempts == attempts - 1


def test_game_won(game):
    for letter in "python":
        game.guess(letter)

    assert game.is_won()


def test_game_not_lost(game):
    assert not game.is_lost()
