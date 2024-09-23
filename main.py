class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' '
        self.is_occupied = False

    def occupy(self, symbol):
        if not self.is_occupied:
            self.symbol = symbol
            self.is_occupied = True
            return True
        return False


class Board:
    def __init__(self):
        self.cells = [Cell(ind) for ind in range(1, 10)]

    def display(self):
        for k in range(0, 9, 3):
            for i in range(3):
                print(f'{self.cells[i + k].symbol} | ', end='')
                # print(f'{self.cells[i + k].symbol} {self.cells[i + k].number} | ', end='')
            print()

    def change_cell_state(self, cell_number, symbol):
        if 1 <= cell_number <= 9:
            cell = self.cells[cell_number - 1]
            return cell.occupy(symbol)
        return False

    def check_game_over(self):
        self.win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for win_comb in self.win_combinations:
            if self.cells[win_comb[0]].symbol == self.cells[win_comb[1]].symbol == self.cells[win_comb[2]].symbol and self.cells[
                win_comb[2]].symbol != ' ':
                return True
        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self):
        while True:
            try:
                move = int(input(f'Введите номер клетки для вашего символа (1-9): '))
                if 1 <= move <= 9:
                    return move
                else:
                    print('Некорректный ввод. Введите число от 1 до 9')
            except ValueError:
                print('Некорректный ввод. Введите число от 1 до 9')


class Game:
    def __init__(self, player_1, player_2):
        self.players = [player_1, player_2]
        self.board = Board()

    def run_one_move(self, player):
        move = player.make_move()
        while not self.board.change_cell_state(move, "X" if player == self.players[0] else "O"):
            print("Эта клетка уже занята. Выберите другую.")
            move = player.make_move()

        self.board.display()
        if self.board.check_game_over():
            player.wins += 1
            print(f'{player.name} победил!')
            return True
        return False

    def run_one_game(self):
        self.board = Board()
        self.board.display()
        while True:
            for player in self.players:
                if self.run_one_move(player):
                    return

    def run(self):
        while True:
            self.run_one_game()
            print(f'{self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}')
            play_again = input('Вы хотите продолжить игру? Y - да, N - нет: ')
            if play_again.lower() != 'y':
                break
        print('До свидания')


if __name__ == '__main__':
    player1_name = input('Введите имя первого игрока: ')
    player2_name = input('Введите имя второго игрока: ')

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    game = Game(player1, player2)
    game.run()
  
