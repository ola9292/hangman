import random
import hangman_words
import hangman_art

stages = hangman_art.stages
# word_list = ['aardvark', 'baboon', 'camel']
word_list = hangman_words.word_list
lives = 6
chosen_word = random.choice(word_list)

placeholder = ""


for letter in chosen_word:
    placeholder += '_'
print(placeholder)

guess_word = []
game_over = False
while not game_over:
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input('Guess a letter: ').lower()
    if guess in guess_word:
        print(f"You have entered the word {guess} before")
    guess_word.append(guess)

    if guess not in chosen_word:
        print(f"You have entered a wrong word {guess}. You lose a life!")
        lives -= 1
    display = ""

    for letter in chosen_word:
        if letter in guess_word:
            display += letter
        else:
            display += "_"
    print(display)
    print(lives)    
    print(stages[lives])
    if "_" not in display:
        game_over = True
        
        print("****************************YOU WIN****************************")
    if lives == 0:
         game_over = True
         print(f"the word you are trying to guess is {chosen_word}")
         print(f"***********************YOU LOSE**********************")