from pathlib import Path
import os

SCORES_FILE_NAME = open(Path("Scores.txt"), "w")
path = Path("Scores.txt")
if not os.path.exists(path):
    os.mkdir(path)

BAD_RETURN_CODE = int(401)


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
