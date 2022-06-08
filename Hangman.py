import random
from Functions import list_duplicates_of

word_pool = open("word_pool.txt").readlines()
word_choice = list(random.choice(word_pool))
word_choice.remove("\n")
print(word_choice)
user_input_list = []
strike_number = 3

for x in word_choice:
    user_input_list.append("_ ")
for x in word_choice:
    print(user_input_list)
    user_input = input("Choose a letter (a to z): ")
    if user_input in word_choice:
        print("Correct.")
        user_input_compare = list_duplicates_of(word_choice, user_input)
        z = 0
        while z == 0:
            y = len(user_input_compare) - 1
            for x in user_input_compare:
                user_input_list[user_input_compare[y]] = user_input
                y = y - 1
            z = z + 1
        if user_input_list == word_choice:
            print("Congratulations you won!")
            break
    else:
        strike_number = strike_number - 1
        print("Incorrect,", strike_number, "strikes remaining.")
        if strike_number == 0:
            print("You ran out of strikes. Quitting...")
            break
