import random


class Die:

    def __init__(self):
        self._value = None  # this is equal to declaring the parameter in the constructor __init__ (value=None).

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False):  # if you not sure whether to make an attribute public or non public,
        # then make it public at first. It is easier to make it public again.
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()  # Aggregation happening right here.


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("====================================")
        print("Welcome to the Roll the Dice 🎲! :)")
        print("====================================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the Dice
        player_value = self._player.roll_die()  # accessing the player instance through aggregation.
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Determine winner and loser
        if player_value > computer_value:
            print("\nYou won the round! :)")
            self.update_counters(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("\nThe computer won this round. Try again :(")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print("\nI's a tie!")

        # Show counters
        self.show_counters()

    def print_round_welcome(self):
        # This is an example of a static method (methods that don't use self in the body of the method)
        # see definition in course notes.
        # Welcome the user
        # The input function will prompt the user to press a key. The
        # program execution will be paused until the player presses a key.
        print("\n----- New Round -----")
        input("🎲 Press any key to roll the dice.")

    def show_dice(self, player_value, computer_value):
        # show the values
        print(f"Your die 🎲: {player_value}")
        print(f"Computer die 🎲: {computer_value}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"\nYour counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(winner=self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(winner=self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):  # Winner is an instance of the class Player
        if winner.is_computer:  # using the Player class property
            print("\n====================================")
            print("GAME OVER 🎉")
            print("====================================")
            print("The computer won the game. Sorry... 😔")
            print("====================================")
        else:
            print("\n====================================")
            print("GAME OVER 🎉")
            print("====================================")
            print("You won the game! Congratulations 🎉")
            print("====================================")


# Crete Instance
player_die = Die()
computer_die = Die()
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

# Start the game
game.play()
