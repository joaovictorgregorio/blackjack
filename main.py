import os
import random
import time
import art

def calculator_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    

def buy_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# def menu():
    
            

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "\nEmpate 🙃"
    elif computer_score == 0:
        return "\n Você perdeu!!! O computador tem Blackjack 😱"
    elif user_score == 0:
        return "\n Você venceu!!! Você tem Blackjack 😁"
    elif user_score > 21:
        return "\nVocê ultrapassou de 21. Você perdeu 😭"
    elif computer_score > 21:
        return "\nO computador ultrapassou de 21. Você venceu 😎"
    elif user_score > computer_score:
        return "\nVocê venceu 🫡"
    else:
        return "\nVocê perdeu 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(buy_cards())
        computer_cards.append(buy_cards())

    while not is_game_over:
        user_score = calculator_score(user_cards)
        computer_score = calculator_score(computer_cards)
        print(f"  Sua mão: {user_cards}, seu score atual: \033[1;32m{user_score}\033[m")
        print(f"  A primeira carta do computador é: \033[1;34m{computer_cards[0]}\033[m")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_game = str(input("\nDigite \033[33m[S]\033[m para obter outra carta ou \033[33m[N]\033[m para parar: ")).upper()
            if continue_game not in ["S", "N"]:
                os.system("cls")
                print("\033[1;31mOpção inválida. Tente novamente.\033[m")
                exit()
            elif continue_game == "S":
                user_cards.append(buy_cards())
            else:
                is_game_over = True
                        

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(buy_cards())
        computer_score = calculator_score(computer_cards)


    print(f"\n  Sua mão final: {user_cards}, score final: \033[1;32m{user_score}\033[m")
    print(f"  Mão final do computador: {computer_cards}, score final: \033[1;34m{computer_score}\033[m")
    print(compare(user_score, computer_score))


while input("\nDigite \033[33m[S]\033[m para iniciar uma partida de Blackjack ou \033[33m[N]\033[m para sair: ").upper() == "S":
    os.system("cls")
    print(art.logo)
    time.sleep(0.5)
    print("\033[7;37;44m\nBEM-VINDO AO BLACKJACK ♠️\033[m")
    play_game()
    
    
    # if start_blackjack not in ["S", "N"]:
    #     os.system("cls")
    #     print("\033[1;31mOpção inválida. Tente novamente.\033[m")
    #     time.sleep(1)
    #     print("\nVoltando para o menu principal...")
    #     time.sleep(1.5)
    #     menu()
    # else:
    #     if start_blackjack == "N":
    #         print("\033[1;33m\nObrigado por jogar! Até a próxima.\033[m")
    #         exit()
    #     else:
    #         time.sleep(0.5)
    #         print("\033[7;37;44m\nPARTIDA INICIADA...\n\033[m")
    #         play_game





