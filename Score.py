from pathlib import Path


def add_score(difficulty):
    POINTS_OF_WINNING = str((difficulty * 3) + 5)

    try:
        score_file = open(Path("Scores.txt"), "r")
        score = open(Path("Scores.txt"), "a")
        score.write(f" ,{POINTS_OF_WINNING}")
    except FileExistsError:
        score = open(Path("Scores.txt"), "a")
        score.write(POINTS_OF_WINNING)


