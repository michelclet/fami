import numpy as np

loyer     = 500*6 + 1060*2
# loyer = 1060*12

# % REGIME MICRO-BIC

ab          = 50/100 # abbatement
ir          = 30/100 # taux impot sur le revenus
ps          = 17.2/100 # prélèvement sociaux
impot       = loyer*ab*(ir + ps)

print('Régime Micro     ', round(impot), '€')


# Régime Micro


# % REGIME REEL

charges = 350           # taxe fonciere
charges += 130*12       # charges copro
charges += 212*12       # interets
charges += 35*12        # assurance habitation
charges += 200000/120   # amortissement bien
charges += 2000/5       # amortissement meubles
impot       = (loyer-charges)*ab*(ir + ps)
comptable = 1500

if impot < 0:
    impot = 0
print('Regime Réel      ', round(impot+comptable), '€') 