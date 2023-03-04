from immo_functions import simulation_resultat
from immo_functions import mensualite_resultat
from immo_functions import interet_resultat
from immo_functions import capital_resultat
from immo_functions import capacite_resultat

revenus     = 3800
credit      = 0
prix        = 390000
notaire     = prix*7.3/100
taux        = 1.95
duree       = 25
apport      = 100000
assurance   = 40
output      = simulation_resultat(prix, taux, duree, apport, assurance, revenus, credit, notaire)

for key in output.keys():
    print(key, output[key])


# %%
endettement = 33
output = capacite_resultat(taux, duree, apport, assurance, revenus, credit, endettement)

for key in output.keys():
    print(key, output[key])
    
# %% Relais

estimation      = 375000
reste_credit    = 150000
garde           = 50000

relais          = 80/100*(estimation - garde)
sup             = (estimation - garde) - relais

taux_relais     = 1.32
taux_sup        = 1.64
mensualite  = mensualite_resultat(sup, taux_sup, duree)
print(mensualite)