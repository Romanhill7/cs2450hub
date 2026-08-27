import random
def ageGuesser():
    print("Welcome. This program will try and guess your age. What is your name?")
    username=input("Enter name")
    Ages = list(range(15,41))
    guessed = False
    while guessed==False:
        guess_index=random.randint(0,len(Ages))
        guess = Ages[guess_index]
        cur_guess=input(f"Is your age {guess}? Y/N")
        if cur_guess == "y" or cur_guess == "Y":
            guessed = True
            print("{username} is {guess} years old.")
        else:
            print("Rats")
            Ages.pop(guess_index)
        
        




if __name__ == "__main__":
    ageGuesser()