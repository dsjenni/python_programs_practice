#solving below statement
#We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

#🇨🇴 Colombian pesos
#🇵🇪 Peruvian soles
#🇧🇷 Brazilian reais
#A program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

co = int(input("What do you have left in pesos? "))
pe = int(input("What do you have left in soles? "))
br = int(input("What do you have left in reais? "))

usd1 = co * 0.055
usd2 = pe * 0.27
usd3 = br * 0.18

USD = usd1 + usd2 + usd3       # or USD = co*0.055 + pe*0.27 + br*0.18
print(USD)