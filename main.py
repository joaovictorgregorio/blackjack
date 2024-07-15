import os
import random
import time
import art


os.system("cls")

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/
def menu():
    os.system("cls")
    print(art.logo)
    time.sleep(0.5)
    print("\033[7;37;44m\nBEM-VINDO AO BLACKJACK ♠️\033[m")
    
    start_blackjack = str(input("\nDigite \033[33m[S]\033[m para iniciar uma partida de Blackjack ou \033[33m[N]\033[m para sair: ")).upper()
    if start_blackjack not in ["S", "N"]:
        os.system("cls")
        print("\033[1;31mOpção inválida. Tente novamente.\033[m")
        exit()
    else:
        if start_blackjack == "N":
            os.system("cls")
            print("Obrigado por jogar! Até a próxima.")
            exit()
        else:
            time.sleep(0.5)
            print("\033[7;37;44m\nPARTIDA INICIADA...\n\033[m")
            blackjack()


def blackjack():
    user_cards = []
    computer_cards = []

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            
    user_cards += random.sample(cards, 2)
    computer_cards = user_cards + random.sample(cards, 2)

    print(f"   Sua mão: {user_cards}, seu score atual: \033[1;32m{sum(user_cards)}\033[m")
    print(f"   A primeira carta do computador é: \033[1;34m{computer_cards[0]}\033[m")

    keep_playing = True

    while keep_playing:
        continue_game = str(input("\nDigite \033[33m[S]\033[m para obter outra carta ou \033[33m[N]\033[m para parar: ")).upper()
        if continue_game not in ["S", "N"]:
            os.system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\033[m")
            exit()
        else:
            if continue_game == "S":
                user_cards += random.sample(cards, 1)
                computer_cards += random.sample(cards, 1)
                print(f"   Sua mão: {user_cards}, seu score atual: \033[1;32m{sum(user_cards)}\033[m")
                print(f"   A primeira carta do computador é: \033[1;34m{computer_cards[0]}\033[m")
                if sum(user_cards) > 21:
                    keep_playing = False
                    print(f"   Sua mão final: {user_cards}, seu score final: \033[1;31m{sum(user_cards)}\033[m")
                    print(f"   Mão final do computador: {computer_cards}, score final: \033[1;34m{sum(computer_cards)}\033[m")
                    print("\033[1;31mVocê perdeu! ��\033[m")
            elif continue_game == "N":
                if sum(user_cards) <= 21 and sum(user_cards) > sum(computer_cards):
                    keep_playing = False
                    print(f"   Sua mão final: {user_cards}, seu score final: \033[1;32m{sum(user_cards)}\033[m")
                    print(f"   Mão final do computador: {computer_cards}, score final: \033[1;34m{sum(computer_cards)}\033[m")
                    print("\033[1;32mVocê venceu! 😎��\033[m")
                elif sum(computer_cards) > 21 or sum(user_cards) > sum(computer_cards):
                    keep_playing = False
                    print(f"   Sua mão final: {user_cards}, seu score final: \033[1;32m{sum(user_cards)}\033[m")
                    print(f"   Mão final do computador: {computer_cards}, score final: \033[1;34m{sum(computer_cards)}\033[m")
                    print("\033[1;32mVocê venceu! ����\033[m")
            
                    
menu()



