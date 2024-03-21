import random

#Exibir mensagem de boas vindas 
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Gerar numero aleatorio entre 1 e 10

number = random.randint(1, 10)

#variável de controle
isGuessRight = False

#Loop

while isGuessRight:True
#pedir ao usuário um número
guess= input("Guess a number between 1 and 10")

#condicional
if int(guess)== number:
    print("You guessed {}. Thats correct! You win!".format(guess))
    isGuessRight = True

    #Enquanto o usuário não adivinhar
else:
    print("You guessed {}. Sorry, that isn't correct. Try again!".format(guess))

