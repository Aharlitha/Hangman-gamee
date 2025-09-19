import random
word_list = ["Apple", "Banana", "Grapes", "orange", "pineapple","custardapple"]
lives=6
a = random.choice(word_list)  
placeholder = "_" * len(a)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    char = input("\nGuess a letter: ")

    display = ""
    for letter in a:
        if char == letter:
            display += letter
            if char not in correct_letters:
                correct_letters.append(char)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if char not in a:
        lives-=1
        if lives==0:
            game_over=True
            print("you lost")

    if "_" not in display:
        game_over = True
        print("You won")



