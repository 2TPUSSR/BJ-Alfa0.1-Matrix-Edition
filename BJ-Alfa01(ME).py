import logging
import numpy as np
import random
import copy
import sys
import os
import time

class ResetFunkcji(Exception):
    pass


def gra():
    money = 1000
    debt = 2000
    print("Money: ", money)
    print("Debt: ", debt)
    result = bet(money, debt)
    return result


def bet(money, debt):
    bet_a = int(input("Dawaj kase: "))
    money = money - bet_a
    print(money)
    while money < 0:
        money, debt = kredyt(money, debt)
    if bet_a > 0 and money >= 0:
        blackjack(money)


def hit_me(deck):
    if len(deck) == 0:
        print("Deck jest pusty!")
        return None, deck
    card = deck[0]
    updated_deck = np.delete(deck, 0)
    return card, updated_deck


def blackjack(money):
    karty = np.arange(2, 15).astype(object)
    karty[9] = "J"
    karty[10] = "Q"
    karty[11] = "K"
    karty[12] = "A"
    grupowane = np.repeat(karty, 4)
    przetasowane = copy.deepcopy(grupowane)
    tasowane = input("Tasowac? ").lower()
    if tasowane in ("y", "yes", "tak"):
        random.shuffle(przetasowane)
        print(przetasowane)
    else:
        matrix()
        time.sleep(5)
        raise ResetFunkcji
    zaczynasz = input("Zaczynasz? (y/n): ").lower()
    if zaczynasz in ("y", "yes", "tak"):
        wyciagnieta_karta1, przetasowane = hit_me(przetasowane)
        wyciagnieta_karta2, przetasowane = hit_me(przetasowane)
        print(f"Twoje karty: {wyciagnieta_karta1}, {wyciagnieta_karta2}")
        wyciagnieta_karta_dealer1, przetasowane = hit_me(przetasowane)
        wyciagnieta_karta_dealer2, przetasowane = hit_me(przetasowane)
        print("Karta dealer: ", wyciagnieta_karta_dealer1, wyciagnieta_karta_dealer2)
        print(f"Pozostało kart: {len(przetasowane)}")
    else:
        matrix()
        time.sleep(6)
        raise ResetFunkcji


def kredyt(money, debt):
    kredyta = [500, 2500, 5000]
    opcja1 = input("Brac kredyt, czy game over Cristopher? ").lower()
    if opcja1 in ("y", "yes", "tak"):
        print("To fajnie")
        opcja2 = int(input("Ile: 500, 2500, 5000? "))
        if opcja2 in kredyta:
            money += opcja2
            debt += opcja2
            print(f"Nowy stan konta: {money}, Dlug: {debt}")
            return money, debt
        if money < 0:
            kredyt(money, debt)
        else:
            print("Nie ma takiej kwoty.")
            return kredyt(money, debt)
    else:
        print("Game Over Cristopher")
        exit()


def confirm():
    start = input("START? (y/n): ")
    if start in ("y", "Y"):
        print(start + " has been chosen, starting")
        gra()
    elif start in ("n", "N"):
        print("chosen not to start")
        confirm()
    else:
        print(start + " is not an option, try again")
        confirm()
    return start


def matrix():
    print("\n","Nie potrzebujemy cię w naszym składzie")
    print("Adios amigo")
    time.sleep(4)
    clear = 'cls'
    os.system(clear)
    print("T0 Tylk0 M4trix")
    time.sleep(2)
    os.system(clear)
while True:
    try:
        confirm()
        break
    except ResetFunkcji:
        continue


confirm()
