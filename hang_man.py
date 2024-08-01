import re

riddle = input("Type in a word: ")
# creating a list to facilitate position substitution
blank = list(len(riddle) * "_")
print("\n \n \n \n \n \n \n \n \n \n \n")

print("You have 6 chances to guess the letter in the word. ")
answer = None
trials = 6

while trials > 0 and answer != riddle:
    x = input("Type in a letter that you think would be in the word. \n")

    # re.search returns a <> match result which contains backstage information
    if not bool(re.search(x, riddle)):
        trials -= 1
        if trials == 0:
            while True:
                guess = input("You have used up your chances of guessing letters, do you want to guess the word? \n")
                if guess == "yes":
                    answer = input("Type in your answer: ")
                    if answer == riddle:
                        print("This is the CORRECT answer, congratulations!!")
                        break
                    else:
                        print("This is NOT the correct answer.")
                        continue
                elif guess == "no":
                    print("Sorry, you have lost this game. \nThe correct answer is", riddle, ". Good luck next time!")
                    break
                else:
                    print("Answer cannot be recognised.")
                    continue
        else:
            print("This letter is NOT in the word. You have", trials, "more chances.")

    else:
        # m.start() gets us one single value, otherwise it will return a tuple of the start and the end pos
        pos = [m.start() for m in re.finditer(x, riddle)]
        for i in range(len(pos)):
            blank[pos[i]] = x
        # "" means join the items in the list without separators
        print("".join(blank))
        while True:
            guess = input("Do you want to guess the word now? \n")
            if guess == "yes":
                answer = input("Type in your answer: ")
                if answer == riddle:
                    print("This is the CORRECT answer, congratulations!!")
                    break
                else:
                    print("This is NOT the correct answer.")
                    continue
            elif guess == "no":
                break
            else:
                print("Answer cannot be recognised.")
                continue
