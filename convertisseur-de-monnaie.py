
import forex_python

from forex_python.converter import CurrencyRates

devise = CurrencyRates()


montant = int(input("Entrez le montant : "))

from_ = input("quel devise utilisez vous ?")
to_= input("Vers quelle devise voulez vous utilisez ? ")

print(from_, "de", to_, montant)

resultat = devise.convert(from_, to_, montant)



print("Valeur converti : ",resultat )



ask = str(input("Voulez vous voir l'historique ? "))

try: 

    if  ask == "oui":
        print("montant ", montant," valeur converit de ", from_, " a " , to_)

    else:
        print("fin")

except forex_python.converter.RatesNotAvailableError:
        print("Conversion impossible : une ou plusieurs devises ne sont pas prises en charge.")



