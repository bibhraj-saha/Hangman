from src.high_score import HighScoreManager
from src.models import ScoreEntry

manager = HighScoreManager()

manager.add_score(
    ScoreEntry(
        player="Bibhraj",
        score=275,
        category="Programming",
        difficulty="Hard",
        word="algorithm",
        won=True,
        timestamp="2026-07-22",
    )
)

manager.add_score(
    ScoreEntry(
        player="Alex",
        score=180,
        category="Science",
        difficulty="Medium",
        word="ecosystem",
        won=True,
        timestamp="2026-07-22",
    )
)

print()

print("=" * 60)

print("TOP SCORES")

print("=" * 60)

print()

for index, score in enumerate(
    manager.get_top_scores(),
    start=1,
):

    print(
        f"{index}. "
        f"{score.player:<12}"
        f"{score.score:<5}"
        f"{score.category:<15}"
        f"{score.difficulty}"
    )
