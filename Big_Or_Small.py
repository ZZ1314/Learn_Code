from random import random


def random_num():
    counte = 3
    result = 0
    while counte > 0:
        result += int(random()*6+1)
        counte -= 1
    if result > 9:
        return("B")
    else:
        return ("S")


def game_start(own_money=10000, rate=1):
    result = random_num()
    if own_money > 0:
        print("========Game start!======== \n")
        choices = ['B', 'S']
        own_money = own_money
        rate = rate
        gamer_choices = input("Choice Big or Small!\n")
        if gamer_choices in choices:
            bet = int(input("How much you want bet?You have {} now!\n".format(own_money)))
            if bet <= own_money:
                if own_money > 0:
                    if gamer_choices == result:
                        own_money = own_money + bet*rate
                        print("You Win!You have {} now!\n".format(own_money))
                        nextround = input("You want next round?\n Yes or No\n")
                        if nextround == "Y":
                            game_start(own_money=own_money)
                        else:
                            None
                    else:
                        own_money = own_money - bet
                        print("You Lose,You have {} now!\n".format(own_money))
                        nextround = input("You want next round?\n Yes or No\n")
                        if nextround == "Y":
                            game_start(own_money=own_money)
                        else:
                            None
                else:
                    print("You don't have money anymore!You lose the game")
            else:
                print("Try again,You don't have {}, You only have {} !".format(bet, own_money))
                game_start(own_money=own_money)
        else:
            print("Error,Try again!")
            game_start(own_money=own_money)
    else:
        print("You don't have money anymore!You lose the game")


game_start()
