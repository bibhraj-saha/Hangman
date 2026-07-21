"""
Game scoring.
"""


class ScoreCalculator:
    """
    Calculates Hangman score.
    """

    DIFFICULTY_POINTS = {
        "Easy": 100,
        "Medium": 200,
        "Hard": 300,
    }

    REMAINING_ATTEMPT_POINTS = 10

    WRONG_GUESS_PENALTY = 5

    @classmethod
    def calculate(
        cls,
        difficulty: str,
        remaining_attempts: int,
        wrong_guesses: int,
        won: bool,
    ) -> int:

        if not won:
            return 0

        base = cls.DIFFICULTY_POINTS[
            difficulty
        ]

        bonus = (
            remaining_attempts
            * cls.REMAINING_ATTEMPT_POINTS
        )

        penalty = (
            wrong_guesses
            * cls.WRONG_GUESS_PENALTY
        )

        return max(
            0,
            base + bonus - penalty,
        )