from objects.board import Board


class Game:
    """
    Create a game of tic-tac-toe.

    It manages the turns, the symbol's placement in the board by the two players.
    At each turn the board will be test to see if the game is won by one of the two players.
    Equality case are also check.

    Attributes:
        board (Board)  Stock the board
        player ("X" or "O")     The player who it is the turn

    """

    def __init__(self):

        self.board = Board()
        self.player = "X"

    @staticmethod
    def __victory_display(winner: str):
        print(f"The player {winner} won. Well done !!")

    @staticmethod
    def __equality_display():
        print(f"There is  equality...")

    @staticmethod
    def __which_cell():
        """
        Demands the cell which the player wants to put his symbol.

        :return:
        """

        cell_line = int(input("Enter the line of the cell wanted : "))
        cell_column = int(input("Enter the column of the cell wanted : "))

        return cell_line, cell_column

    @staticmethod
    def play_again() -> bool:
        """
        Demands if player want to play another game.

        :return: True, False
        """
        request = input("Do you want to play again [y/n]?").lower()

        return True if request == 'y' else False

    def __is_won(self) -> bool or str:
        """
        Test if the game is won and by which player.

        :return: False (if the game isn't won), "X" (if the "X" player won), "O" (if the "O" player won)
        """
        X = ("X", "X", "X")
        O = ("O", "O", "O")

        winner = False
        for n in range(len(self.board)):

            if self.board.line(n) == X or self.board.line(n) == O:
                winner = self.board.line(n)[0]

            elif self.board.column(n) == X or self.board.column(n) == O:
                winner = self.board.column(n)[0]

            elif self.board.diagonal(n) == X or self.board.diagonal(n) == O:
                winner = self.board.column(n)[0]

        if winner:
            self.__victory_display(str(winner))

        return winner

    def __equality(self) -> bool:
        """
        Tests if there is equality.

        :return: True (if yes), False (else)
        """
        if self.board.is_complete():
            self.__equality_display()
            return True

        return False

    def run(self) -> None:
        """
        Runs the game.

        Calls different other methods to manage the game.

        :return: None
        """
        print("Welcome to the Tic-Tac-Toe game.")

        while (self.__is_won() is False) and (not self.__equality()):
            print(self.board)

            print(f"This is the turn of the {self.player} player: \n")

            cell_coordinates = self.__which_cell()

            # Test while the cell wanted is already taken
            while self.board.add_symbol(self.player, cell_coordinates[0], cell_coordinates[1]) is False:
                print("\nThe cell wanted is not empty. Please, retry...")
                cell_coordinates = self.__which_cell()

            # Changing player
            self.player = "X" if self.player == "O" else "O"
