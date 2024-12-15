import random
print("\nLet's play a number guessing game")
print("You choose a number, then I'll guess your number\n")


number = input("Enter a number between 1 to 99: ")

while number.isdigit() != True:
    number = input("enter a valid number: ")

number = int(number)
guess = random.randint(1, 99)
print(f"\nMy guess is {guess}\n")

print("Enter 'm' if the number > my guess, 'l' if number < my guess, 't' if number == my guess")

hint = input("Enter your command: ")

while hint != "m" and hint != "l" and hint != "t":
    if hint == "t":
        print("Wow, I guessed the number correctly!!")
        break
    print("\nPlease enter 'm' if your number bigger, 'l' if your number smaller, 't' if I guessed correctly\n")
    hint = input("Enter your command: ")


while hint != "t":
    if hint == "l":
        while hint != "t":
            if hint == "l":
                guess = random.randint(1, guess-1)
                print(f"\nMy guess is {guess}")
                hint = input("Enter your command: ")
                while hint != "l" and hint != "m":
                    if hint == "t":
                        print("\nWow, I guessed the number correctly!!")
                        break
                    print("\nPlease use 'l' if your number smaller, 'm' if your number bigger\n")
                    hint = input("Enter your command: ")
            elif hint == "m":
                guess = random.randint(guess+1, number)
                print(f"\nMy guess is {guess}")
                hint = input("Enter your command: ")
                while hint != "l" and hint != "m":
                    if hint == "t":
                        print("\nWow, I guessed the number correctly!!")
                        break
                    print("\nPlease use 'l' if your number smaller, 'm' if your number bigger\n")
                    hint = input("Enter your command: ")

    elif hint == "m":  
        while hint != "t":
            if hint == "m":
                guess = random.randint(guess+1, 99)
                print(f"\nMy guess is {guess}")
                hint = input("Enter your command: ")
                while hint != 'm' and hint != 'l':
                    if hint == "t":
                        print("\nWow, I guessed the number correctly!!")
                        break
                    print("\nPlease use 'l' if your number smaller, 'm' if your number bigger\n")
                    hint = input("Enter your command: ")
            elif hint == "l":
                guess = random.randint(number, guess-1)
                print(f"\nMy guess is {guess}")
                hint = input("Enter your command: ")
                while hint != 'm' and hint != 'l':
                    if hint == "t":
                        print("\nWow, I guessed the number correctly!!")
                        break
                    print("\nPlease use 'l' if your number smaller, 'm' if your number bigger\n")
                    hint = input("Enter your command: ")

print("\nThanks for playing")