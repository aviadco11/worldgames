import Utils


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        my_file = open(Utils.SCORES_FILE_NAME, "r", encoding="utf-8")
        for line in my_file.readlines():
            result = (int(line) + int(points_of_winning))
    except BaseException as e:
        result = points_of_winning
    finally:
        my_file = open(Utils.SCORES_FILE_NAME, "w", encoding="utf-8")
        my_file.writelines(f"{result}")
        my_file.close()

