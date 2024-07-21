rows = columns = 4

game_field = [
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]


def print_field():
    for i in range(rows):
        for j in range(columns):
            print(game_field[i][j], end=" ")
        print()


def is_filled():
    return all(unit != '-' for row in game_field[1:] for unit in row)


def is_winner():
    # Горизонталь
    for i in range(1, 4):
        if game_field[i][1] == game_field[i][2] == game_field[i][3] != '-':
            return game_field[i][1]

    # Вертикаль
    for j in range(1, 4):
        if game_field[1][j] == game_field[2][j] == game_field[3][j] != '-':
            return game_field[1][j]

    # Диагональ
    if game_field[1][1] == game_field[2][2] == game_field[3][3] != '-':
        return game_field[1][1]
    if game_field[1][3] == game_field[2][2] == game_field[3][1] != '-':
        return game_field[1][3]


while True:

    while True:
        try:
            i = int(input('Первый игрок, введите номер строки (1-3): '))
            j = int(input('Введите номер столбца (1-3): '))

            if 1 <= i <= 3 and 1 <= j <= 3:
                if game_field[i][j] == '-':
                    game_field[i][j] = 'x'
                    break
                else:
                    print("Ячейка занята. Попробуйте снова.")
            else:
                print("Ошибка, введите номера от 1 до 3.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    print_field()

    winner = is_winner()
    if winner:
        print("Первый игрок победил!")
        break

    if is_filled():
        print("Ничья!")
        break

    while True:
        try:
            i = int(input('Второй игрок, введите номера строки (1-3): '))
            j = int(input('Введите номер столбца (1-3): '))

            if 1 <= i <= 3 and 1 <= j <= 3:
                if game_field[i][j] == '-':
                    game_field[i][j] = 'o'
                    break
                else:
                    print("Ячейка занята. Попробуйте снова.")
            else:
                print("Ошибка, введите номер от 1 до 3.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    print_field()

    winner = is_winner()
    if winner:
        print("Второй игрок победил!")
        break
