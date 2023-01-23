from time import sleep
import emoji
from os import system
from random import shuffle, choice
from emoji_words import title

def print_words(word):
    for char in word:
        sleep(0.05)
        print(char, end = "", flush = True)

def choose_difficulty():
    system("CLS")
    print(title)
    print("Difficulty:\nEasy\nHard")
    
    difficulty = input("Choose difficulty: ")

    if difficulty.upper() == "EASY" or difficulty.upper() == "HARD":
        return difficulty.upper()
    else:
        print(emoji.emojize("Your answer is :prohibited:. Try again."))
        sleep(3)
        choose_difficulty()


def easy_mode(word):
    hint = word.split()

    for each_word in range(len(hint)):
        temp_list = list()
        temp_list.extend(hint[each_word])
        shuffle(temp_list)
        hint[each_word] = "".join(temp_list)

    hint = " ".join(hint)

    return hint

def hard_mode(word):
    hint = list()

    for char in word:
        if char.isalpha():
            hint.append("_")

        else:
            hint.append(char)

    hint = "".join(hint)

    return hint

def check_answer(ans, word, trivia, stars):
    if ans.isalpha() or ans == "\hint" or ans.__contains__(" "):
        if ans == word:
            print(emoji.emojize(f"{word} is :check_mark_button:!\n{trivia}"))
            stars += 1

            return False, stars

        else:
            print(emoji.emojize("Your answer is :cross_mark_button:. Try again or type \help to know helpful commands"))

    else:
        print(emoji.emojize("Your answer is :prohibited:. Try again."))

    sleep(3)

    return True, stars

def apply_hint(diff, word, correct_set, hint):
    if diff == "EASY":
        new_hint = easy_mode(word)
        correct_set.clear()

    else:
        new_hint = ""

        if hint.__contains__("_"):
            hint = list(hint)
            random_letter = choice(list(correct_set))
            correct_set.remove(random_letter)

            for letters in range(len(list(word))):
                if (word[letters] == random_letter or word[letters] == " " or hint[letters].isalpha()):
                    new_hint += word[letters]

                else:
                    new_hint += "_"
        
        else:
            print("All the letters are already given.")
            sleep(3)
            new_hint = hint

    return set(correct_set), new_hint

def continue_playing():
    cont_ans = input("Would you like to play again? (Y/N): ").upper()

    if cont_ans == "N":
        play = False

    elif cont_ans == "Y":
        play = True

    else:
        continue_playing()

    system("CLS")
    
    return play