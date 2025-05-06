from brain_games.game_runner import run_game
from brain_games.games.prime_game_logic import TASK_DESCRIPTION, make_question


def main():
    run_game(TASK_DESCRIPTION, make_question)


if __name__ == "__main__":
    main()
