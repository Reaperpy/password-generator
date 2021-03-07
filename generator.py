import random

running = True

symbols = ["!", "?", ",", ".", "/"]
letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M," "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Welcome to Reaperpy's Password Generator. Use help for a list of commands.")


random_choices = ["symbols", "letters_lower", "letters_upper", "numbers"]

password = ""
command = ""

while running:
    command = input("> ").lower()
    if command == "generate":
        random_choice = random.choice(random_choices)
        random_choice2 = random.choice(random_choices)
        random_choice3 = random.choice(random_choices)
        random_choice4 = random.choice(random_choices)
        random_choice5 = random.choice(random_choices)
        random_choice6 = random.choice(random_choices)
        random_choice7 = random.choice(random_choices)
        random_choice8 = random.choice(random_choices)
        if random_choice == "symbols":
            character_1 = random.choice(symbols)
        elif random_choice == "letters_lower":
            character_1 = random.choice(letters_lower)
        elif random_choice == "letters_upper":
            character_1 = random.choice(letters_upper)
        elif random_choice == "numbers":
            character_1 = random.choice(numbers)
        if random_choice2 == "symbols":
            character_2 = random.choice(symbols)
        elif random_choice2 == "letters_lower":
            character_2 = random.choice(letters_lower)
        elif random_choice2 == "letters_upper":
            character_2 = random.choice(letters_upper)
        elif random_choice2 == "numbers":
            character_2 = random.choice(numbers)
        if random_choice3 == "symbols":
            character_3 = random.choice(symbols)
        elif random_choice3 == "letters_lower":
            character_3 = random.choice(letters_lower)
        elif random_choice3 == "letters_upper":
            character_3 = random.choice(letters_upper)
        elif random_choice3 == "numbers":
            character_3 = random.choice(numbers)
        if random_choice4 == "symbols":
            character_4 = random.choice(symbols)
        elif random_choice4 == "letters_lower":
            character_4 = random.choice(letters_lower)
        elif random_choice4 == "letters_upper":
            character_4 = random.choice(letters_upper)
        elif random_choice4 == "numbers":
            character_4 = random.choice(numbers)
        if random_choice5 == "symbols":
            character_5 = random.choice(symbols)
        elif random_choice5 == "letters_lower":
            character_5 = random.choice(letters_lower)
        elif random_choice5 == "letters_upper":
            character_5 = random.choice(letters_upper)
        elif random_choice5 == "numbers":
            character_5 = random.choice(numbers)
        if random_choice6 == "symbols":
            character_6 = random.choice(symbols)
        elif random_choice6 == "letters_lower":
            character_6 = random.choice(letters_lower)
        elif random_choice6 == "letters_upper":
            character_6 = random.choice(letters_upper)
        elif random_choice6 == "numbers":
            character_6 = random.choice(numbers)
        if random_choice7 == "symbols":
            character_7 = random.choice(symbols)
        elif random_choice7 == "letters_lower":
            character_7 = random.choice(letters_lower)
        elif random_choice7 == "letters_upper":
            character_7 = random.choice(letters_upper)
        elif random_choice7 == "numbers":
            character_7 = random.choice(numbers)
        if random_choice8 == "symbols":
            ch8 = random.choice(symbols)
        elif random_choice8 == "letters_lower":
            ch8 = random.choice(letters_lower)
        elif random_choice8 == "letters_upper":
            ch8 = random.choice(letters_upper)
        elif random_choice8 == "numbers":
            ch8 = random.choice(numbers)
        password = character_1 + character_2 + character_3 + character_4 + character_5 + character_6 + character_7 + ch8
        print(f"Your newly generated password is {password}")
        password_file = open("password.txt", "w")
        password_write = password_file.write(password)
        password_file.close()
        input("Press enter to close.")
        break

    elif command == "help":
        print("""
Here is a list of commands:
help - Brings up this list of commands
generate - Generates a password.
quit - Exits the program
        """)

    elif command == "quit":
        break
    else:
        print("I don't understand that command. Please use the help command to see a list of available commands.")

