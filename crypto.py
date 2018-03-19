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

	choix = int(input("\nQue souhaitez vous faire ? \n\n1> Afficher la liste des cryptomonaies \n2> Connaitre la valeur d'une cryptomonaie \n3> Quitter \n\nChoix : "))

	if (choix == 1):
		print("\nListe des cryptomonaies :")
		print("Cette opération peut prendre du temps.")
		print(getCoinsList())

	elif (choix == 2):
		crypto = input("\nQuelle cryptomonaie souhaitez vous afficher ? : " )
		
		dico = cryptocompare.get_price(crypto)

		valeur = repr(dico.get(crypto).get('EUR')) #repr permet de convertir la valeur en string pour pouvoir l'insérer dans le print

		print("\n-------------------")
		print(crypto+" : "+valeur+" €")
		print("-------------------")


	elif (choix == 3):
		print("\nA bientot sur l'API CryptoCompare !")
		exit()

	else:
		print("\nMerci de rentrer 1 ou 2 !")

while (True):
	question()
