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

def getCoinPrice(coin, devise):

	return repr(cryptocompare.get_price(coin, curr=devise).get(coin).get(devise))

def getCoinName(coin):

	return cryptocompare.get_coin_list().get(coin).get('CoinName')

def getCoinID(coin):

	return cryptocompare.get_coin_list().get(coin).get('Name') 

def getCoinClassement(coin):

	return cryptocompare.get_coin_list().get(coin).get('SortOrder')

def question():

	choix = int(input("\nQue souhaitez vous faire ? \n\n1> Afficher la liste des cryptomonaies \n2> Obtenir des informations sur une cryptomonaie \n3> Convertir une cryptomonaie \n4> Quitter \n\nChoix : "))

	if (choix == 1):
		print("\nListe des cryptomonaies :")
		print("Cette opération peut prendre du temps.")
		print(getCoinsList())

	elif (choix == 2):
		crypto = input("\nQuelle cryptomonaie souhaitez vous afficher ? : ")
		
		identifiant = getCoinID(crypto)
		nomComplet = getCoinName(crypto)
		valeurEUR = getCoinPrice(crypto, 'EUR')
		valeurUSD = getCoinPrice(crypto, 'USD')
		classement = getCoinClassement(crypto)

		print("\n----------------------")
		print("Identifiant : "+identifiant)
		print("Nom complet : "+nomComplet)
		print("Valeur : "+valeurEUR+"€ / "+valeurUSD+"$")
		print("Classement : "+classement)
		print("-----------------------")

	elif (choix == 3):
		crypto = input("\nQuelle cryptomonaie souhaitez vous convertir ? : ")
		devise = input("\nEn quelle devise souhaitez vous convertir votre cryptomonaie ? (EUR ou USD) : ")

		cryptoName = getCoinName(crypto)
		valeur = getCoinPrice(crypto, devise)

		val = float(valeur)

		qte = int(input("\nCombien de "+cryptoName+" souhaitez vous convertir ? : "))
		valTotal = str(qte*val)

		print("\n----------------------")
		print("Cryptomonaie : "+cryptoName)

		if(devise == 'EUR'):
			print("Valeur unitaire : "+valeur+"€")
			print("Quantité : "+str(qte)+" unitée(s)")
			print("Valeur totale : "+valTotal+"€")

		elif(devise == 'USD'):
			print("Valeur unitaire : "+valeur+"$")
			print("Quantité : "+str(qte)+" unitée(s)")
			print("Valeur totale : "+valTotal+"$")

		print("-----------------------")

	elif (choix == 4):
		print("\nA bientot sur l'API CryptoCompare !")
		exit()

	else:
		print("\nMerci de rentrer 1, 2, 3 ou 4 !")

while True:
	try:
		question()

	except AttributeError:
		print("\nMerci de rentrer une valeur exacte !")

	except ValueError:
		print("\nMerci de rentrer 1, 2, 3 ou 4 !")
