#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare

print("---------------------------------")
print("Bienvenue sur l'API CryptoCompare")
print("---------------------------------")

def getCoinsList():

	listeCoins = cryptocompare.get_coin_list()

	for coin in listeCoins:
		print(coin)

def question():

	choix = int(input("\nQue souhaitez vous faire ? \n\n1> Afficher la liste des cryptomonaies \n2> Obtenir des informations sur une cryptomonaie \n3> Quitter \n\nChoix : "))

	if (choix == 1):
		print("\nListe des cryptomonaies :")
		print("Cette opération peut prendre du temps.")
		print(getCoinsList())

	elif (choix == 2):
		crypto = input("\nQuelle cryptomonaie souhaitez vous afficher ? : " )
		
		identifiant = cryptocompare.get_coin_list().get(crypto).get('Name')
		nomComplet = cryptocompare.get_coin_list().get(crypto).get('CoinName')
		valeurEUR = repr(cryptocompare.get_price(crypto).get(crypto).get('EUR')) #repr permet de convertir la valeur en string pour pouvoir l'insérer dans le print
		valeurUSD = repr(cryptocompare.get_price(crypto, curr='USD').get(crypto).get('USD')) 
		classement = cryptocompare.get_coin_list().get(crypto).get('SortOrder')

		print("\n----------------------")
		print("Identifiant : "+identifiant)
		print("Nom complet : "+nomComplet)
		print("Valeur : "+valeurEUR+"€ / "+valeurUSD+"$")
		print("Classement : "+classement)
		print("-----------------------")

	elif (choix == 3):
		print("\nA bientot sur l'API CryptoCompare !")
		exit()

	else:
		print("\nMerci de rentrer 1, 2 ou 3 !")

while True:
	try:
		question()

	except AttributeError:
		print("\nMerci de rentrer une valeur exacte !")

	except ValueError:
		print("\nMerci de rentrer 1, 2 ou 3 !")
