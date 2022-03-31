import time
import random
import string
import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, sleep_time=0):
    typewriter_simulator(Color.get_color()+message)
    time.sleep(sleep_time)


def valid_input(prompt, options):
    while True:
        option = input(prompt)
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def cave(sleep_time, random_enemi):
    print_pause("You peer cautiously into the cave.", sleep_time)
    print_pause("It turns out to be only a very small cave.", sleep_time)
    print_pause("Your eye catches a glint of metal behind a rock.", sleep_time)
    print_pause("You have found the magical Sword of Ogoroth!", sleep_time)
    print_pause("You discard your silly old dagger and take the sword "
                + " with you.", sleep_time)
    print_pause("You walk back out to the field.", sleep_time)
    print_pause('', 0)
    field(sleep_time, random_enemi)


def field(sleep_time, random_enemi):
    print_pause("Enter 1 to knock on the door of the house.", sleep_time)
    print_pause("Enter 2 to peer into the cave.", sleep_time)
    print_pause("What would you like to do?", sleep_time)

    option = valid_input("(Please enter 1 or 2.)", ['1', '2'])
    if option == '1':
        house(sleep_time, random_enemi)
    else:
        cave(sleep_time, random_enemi)


def house(sleep_time, random_enemi):
    print_pause("You approach the door of the house.", sleep_time)
    print_pause("You are about to knock when the door opens and out steps a "
                + random_enemi + " .", sleep_time)
    print_pause("Eep! This is the " + random_enemi + "'s house!", sleep_time)
    print_pause("The " + random_enemi + " attacks you!", sleep_time)
    print_pause("You feel a bit under-prepared for this, what with only "
                + " having a tiny dagger.", sleep_time)

    option = valid_input("Would you like to (1) fight or (2) run away ?",
                         ['1', '2'])
    if option == '1':
        fight(sleep_time, random_enemi)
    else:
        print_pause("You run back into the field. Luckily, you don't seem "
                    + " to have been followed.", sleep_time)
        print_pause('', 0)
        field(sleep_time, random_enemi)


def fight(sleep_time, random_enemi):

    win = random.choice([True, False])
    if win:
        print_pause("Fight is going on.", sleep_time)
        print_pause("You seem strong and well prepared.", sleep_time)
        print_pause("wooh you WIN the " + random_enemi + ", congratulations")
    else:
        print_pause("You do your best...", sleep_time)
        print_pause("but your dagger is no match for the " + random_enemi
                    + ".", sleep_time)
        print_pause("You have been defeated!", sleep_time)

    option = valid_input("Would you like to play again? (y/n)", ['y', 'n'])
    if option == 'y':
        print_pause("Excellent! Restarting the game ...", sleep_time)
        print_pause('', 0)
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.", sleep_time)
        exit(0)


def play_game():
    sleep_time = 0
    enemies = ["pirate", "troll", "dragon"]
    random_enemi = random.choice(enemies)
    print_pause("You find yourself standing in an open field, filled with "
                + " grass and yellow wildflowers.", sleep_time)
    print_pause("Rumor has it that a " + random_enemi + " is somewhere "
                + "around here, and has been terrifying the nearby"
                + "village.", sleep_time)
    print_pause("In front of you is a house.", sleep_time)
    print_pause("To your right is a dark cave.", sleep_time)
    print_pause("In your hand you hold your trusty (but not very effective)"
                + "dagger.", sleep_time)
    print_pause('', 0)
    field(sleep_time, random_enemi)


if __name__ == '__main__':
    play_game()
