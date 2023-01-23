import emoji
from time import sleep
from os import system
from random import choice
import emoji_words as w
import emoji_functions  as f

main_menu = True
game_active = True
diff = ""

stars = 10
hint = ""

def how_to_play():
    system("CLS")
    print(w.title)
    print(emoji.emojize(w.rules))
    back = input("Type 'BACK' to go to Main Menu: ")
    
    if back.upper() == "BACK":
        return True

    else:
        how_to_play()

while main_menu:
    system("CLS")
    print(w.title)
    print(emoji.emojize(w.menu))
    option = input("Type an option: ")

    if option.upper() == "START GAME":
        diff = f.choose_difficulty()
        game_active = True

        while game_active:
            chosen_word = choice(w.emoji_words)
            correct_letters_hard = set()

            if diff == "EASY": 
                hint = f.easy_mode(chosen_word['Answer'])

            else:
                hint = f.hard_mode(chosen_word['Answer'])

                for letters in chosen_word['Answer']:
                    if letters.isalpha():
                        correct_letters_hard.add(letters)
            
            while game_active:
                menu = False
                system("CLS")
                print(w.title)
                print(emoji.emojize(f":books: Category: {chosen_word['Category']}\t\t:star: Stars: {stars}\n{chosen_word['Emoji']}"))
                f.print_words(hint)
                answer = input("\nEnter your answer: ")

                if answer.lower() == "\hint":
                    if stars > 0:
                        stars -= 1
                        correct_letters_hard, hint = f.apply_hint(diff, chosen_word['Answer'], correct_letters_hard, hint)

                    else:
                        print("You don't have any stars to use a hint.")
                        sleep(3)

                elif answer.lower() == "\skip":
                    break

                elif answer.lower() == "\help":
                    system("CLS")
                    f.print_words(w.commands)
                    sleep(5)

                elif answer.lower() == "\menu":
                    game_active = False
                    menu = True
                    break
                else:
                    game_active, stars = f.check_answer(answer.upper(), chosen_word['Answer'], chosen_word['Trivia'], stars)

                    if game_active == False:
                        w.emoji_words.remove(chosen_word)

            if menu == False:
                game_active = f.continue_playing()

                if game_active == False:
                    print(w.title)
                    f.print_words(emoji.emojize("Thank you for playing! :waving_hand: :backhand_index_pointing_right: :door:"))
                    exit()

    elif option.upper() == "HOW TO PLAY":
        how_to_play()

    elif option.upper() == "EXIT GAME":
        main_menu = False

    else:
        print(emoji.emojize("Your answer is :prohibited:. Try again."))
        sleep(3)