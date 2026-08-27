import random
def ageGuesser():
    print("Welcome. This program will try and guess your age. What is your name?")
    username=input("Enter name: ")
    Ages = list(range(15,41))
    guessed = False
    while guessed==False:
        guess_index=random.randint(0,len(Ages)-1)
        guess = Ages[guess_index]
        print(f"Is your age {guess}?")
        cur_guess=input(f"Y/N ")
        if cur_guess == "y" or cur_guess == "Y":
            guessed = True
            print(f"{username} is {guess} years old.")
        else:
            print("Rats")
            Ages.pop(guess_index)
            if len(Ages) == 0:
                print("I give up. I couldn't guess your age.")
                break
        
        




if __name__ == "__main__":
    ageGuesser()