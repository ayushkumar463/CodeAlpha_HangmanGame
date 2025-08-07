import random
import hangman_stages
import words
listt = choices = ['apple', 'banana', 'mango', 'orange', 'papaya', 'pomegranate', 'guava', 'watermelon']
# choice=random.choice(words.fruits + words.general +words.lst +words.places + words.technology)
choice = random.choice(listt)

choices =[]
tries=7
display = list('_'*len(choice))
print("===================================")
print("🎉 Welcome to the Hangman Game! 🎉")
print("===================================")
print("Rules:")
print("- A secret word will be selected.")
print("- You have to guess one letter at a time.")
print("- You are allowed only 6 wrong attempts.")
print("- Each wrong guess brings the hangman closer to danger!")
print("- You win if you guess the word before all 6 chances are used.")
print("Let's begin! Good luck!\n")
print(' '.join(display))

while '_'  in display and tries>0:
    print('word : ',' '.join(display))
    letter=input("enter letter : ").lower()
    if len(letter)!=1 or not letter.isalpha():
        print("please enter single alphabet : ")
    if letter in choice:
        print("you already entered the letter")

    choices.append(letter)
    if letter in choice:
        for i in range(len(choice)):
            if choice[i]==letter:
                display[i]=letter
            
    else:
        tries-=1
        print("you entered wrong letter. Your live remain ",tries)
        print(hangman_stages.stages[tries])

if '_'not in display:
    print("you won the match. your word was : ",choice)
else:
    print("you loose the match. Your word was : ",choice)