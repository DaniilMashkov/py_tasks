# Проект Крестики-нолики

def make_board(p_1_steps, p_2_steps):
    """Принимает список ходов и печатает доску с их учётом"""

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for step in p_1_steps:
        board.remove(step)
        board.insert(step-1, "X")
    for step in p_2_steps:
        board.remove(step)
        board.insert(step-1, "O")

    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")


def check_step(steps):
    """Проверяется, что клетка пуста и что пользователь ввел число"""

    while True:
        try:
            enter = input()
            if int(enter) in steps[0] or int(enter) in steps[1]:
                print("Клетка занята")
            elif int(enter) in range(1, 10):
                return int(enter)
            else:
                print("Такой клетки нет")
        except ValueError:
            print(f"Некорректный ввод. Введите число ")


def check_winner(steps):
    """проверяет, есть ли выигрышная комбинация на поле"""

    comb = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7], \
           [3, 2, 1], [6, 5, 4], [9, 8, 7], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3], \
           [1, 3, 2], [4, 6, 5], [7, 9, 8], [1, 7, 4], [2, 8, 5], [3, 9, 6], [1, 9, 5], [3, 7, 5], \
           [3, 1, 2], [6, 4, 5], [9, 7, 8], [7, 1, 4], [8, 2, 5], [9, 3, 6], [9, 1, 5], [7, 3, 5], \
           [2, 1, 3], [5, 4, 6], [8, 7, 9], [4, 1, 7], [5, 2, 8], [6, 3, 9], [5, 1, 9], [5, 3, 7], \
           [3, 2, 1], [6, 5, 4], [9, 8, 7], [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 5, 1], [7, 5, 3]

    return True if steps in comb else False


def play_game():
    """Тело игры, включает ввод пользователей, списки их ходов"""

    while True:
        player_1 = input("Введите имя 1 игрока: ") or "Настя"
        print(f'Игрок 1: {player_1}')
        player_2 = input("Введите имя 2 игрока: ") or "Игорь"
        print(f'Игрок 2: {player_2}')
        p_1_steps = []
        p_2_steps = []
        steps = p_1_steps, p_2_steps

        while len(p_2_steps) < 3:
            print(f'Ходит {player_1}.Куда ставить X?')
            p_1_steps.append(check_step(steps))
            make_board(p_1_steps, p_2_steps)
            print(f'Ходит {player_2}.Куда ставить O?')
            p_2_steps.append(check_step(steps))
            make_board(p_1_steps, p_2_steps)

        if check_winner(p_1_steps) is True and check_winner(p_2_steps) is True:
            print("Ничья")
        elif check_winner(p_1_steps) is True:
            print(f"Победил(а) {player_1}")
        elif check_winner(p_2_steps) is True:
            print(f"Победил(а) {player_2}")
        else:
            print("Ничья")

        cycle = input(f"Ещё партию?\n('да' или любой символ): ")
        if cycle == "да":
            play_game()
        else:
            print('Игра завершена')
        break


play_game()