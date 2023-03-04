# Régime Micro
revenus     = 500*6 + 1060*2
ab          = 50/100 # abbatement
ir          = 30/100 # taux impot sur le revenus
ps          = 17.2/100 # prélèvement sociaux
impot       = revenus*ab*(ir + ps)

print('Régime micro', impot)


# Régime Micro