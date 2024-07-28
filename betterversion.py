
grid = []

column_index = [' '] + [str(i) for i in range(1, 7)]
grid.append(column_index)

for i in range(1, 7):
    row = [str(i)] + ['◯'] * 6
    grid.append(row)


def print_field():
    for _ in range(1):
        for rows in grid:
            print(' | '.join(rows))
        print()


class Ship:
    def __init__(self):
        self.coordinates = []

    def place_ships(self):
        self.single_ship(4)
        self.double_ship(2)
        self.triple_ship()

    # проверка соседства - возвращает True если соседи
    def are_neighbours(self, point_1, point_2):
        dx = abs(point_1[0] - point_2[0])
        dy = abs(point_1[1] - point_2[1])
        return dx <= 1 and dy <= 1

    def get_coordinates(self, ship_type):
        while True:
            try:
                y = int(input(f'Введите x-координату для {ship_type} (1 - 6): '))
                x = int(input(f'Введите y-координату для {ship_type} (1 - 6): '))
                if all(1 <= coord <= 6 for coord in (x, y)):
                    return x, y
                else:
                    print('Ошибка: введен неверный номер. Попробуйте снова.')
            except ValueError:
                print('Некорректный ввод. Попробуйте снова')


    # катер
    def single_ship(self, count):
        for _ in range(count):
            while True:
                x, y = self.get_coordinates('катера')
                if grid[x][y] == '◯':
                    if not any(self.are_neighbours((x, y), old_coordinates) for old_coordinates in self.coordinates):
                        grid[x][y] = '■'
                        self.coordinates.append((x, y))
                        print_field()
                        break
                    else:
                        print('Соседняя ячейка! Попробуйте снова.')
                else:
                    print('Позиция занята. Попробуйте снова.')

    # крейсер
    def triple_ship(self):
        while True:
            x, y = self.get_coordinates('крейсера')
            direction = input('Выберите направление (left/right/up/down): ')
            if direction not in ['left', 'right', 'up', 'down']:
                print('Некорректный ввод. Попробуйте снова.')
                continue

            if direction in ['left', 'right']:
                shift = -1 if direction == 'left' else 1
                if all(1 <= y + shift * i <= 6 for i in range(3)):
                    if all(grid[x][y + shift * i] == '◯' for i in range(3)):
                        if not any(self.are_neighbours((x, y + shift * i), old_coord) for i in range(3) for old_coord in
                                   self.coordinates):
                            for i in range(3):
                                grid[x][y + shift * i] = '■'
                                self.coordinates.append((x, y + shift * i))
                            print_field()
                            break
                        else:
                            print('Соседняя ячейка! Попробуйте снова.')
                    else:
                        print('Позиция занята. Попробуйте снова')
                else:
                    print('Крейсер вышел за границы поля!')

            elif direction in ['up', 'down']:
                shift = -1 if direction == 'up' else 1
                if all(1 <= x + shift * i <= 6 for i in range(3)):
                    if all(grid[x + shift * i][y] == '◯' for i in range(3)):
                        if not any(self.are_neighbours((x + shift * i, y), old_coord) for i in range(3) for old_coord in
                                   self.coordinates):
                            for i in range(3):
                                grid[x + shift * i][y] = '■'
                                self.coordinates.append((x + shift * i, y))
                            print_field()
                            break
                        else:
                            print('Соседняя ячейка! Попробуйте снова.')
                    else:
                        print('Позиция занята. Попробуйте снова')
                else:
                    print('Крейсер вышел за границы поля!')

    def double_ship(self, count):
        for _ in range(count):
            while True:
                x, y = self.get_coordinates('эсминца')
                direction = input('Выберите направление (left/right/up/down): ')
                if direction not in ['left', 'right', 'up', 'down']:
                    print('Некорректный ввод. Попробуйте снова.')
                    continue

                if direction in ['left', 'right']:
                    shift = -1 if direction == 'left' else 1
                    if all(1 <= y + shift * i <= 6 for i in range(2)):
                        if all(grid[x][y + shift * i] == '◯' for i in range(2)):
                            if not any(
                                    self.are_neighbours((x, y + shift * i), old_coord) for i in range(2) for old_coord
                                    in self.coordinates):
                                for i in range(2):
                                    grid[x][y + shift * i] = '■'
                                    self.coordinates.append((x, y + shift * i))
                                print_field()
                                break
                            else:
                                print('Соседний корабль! Попробуйте снова.')
                        else:
                            print('Позиция занята. Попробуйте снова.')
                    else:
                        print('Эсминец вышел за границы поля!')

                elif direction in ['up', 'down']:
                    shift = -1 if direction == 'up' else 1
                    if all(1 <= x + shift * i <= 6 for i in range(2)):
                        if all(grid[x + shift * i][y] == '◯' for i in range(2)):
                            if not any(
                                    self.are_neighbours((x + shift * i, y), old_coord) for i in range(2) for old_coord
                                    in self.coordinates):
                                for i in range(2):
                                    grid[x + shift * i][y] = '■'
                                    self.coordinates.append((x + shift * i, y))
                                print_field()
                                break
                            else:
                                print('Соседний корабль! Попробуйте снова.')
                        else:
                            print('Позиция занята. Попробуйте снова.')
                    else:
                        print('Эсминец вышел за границы поля!')


game = Ship()
print_field()
game.place_ships()
