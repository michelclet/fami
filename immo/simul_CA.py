# %% Bien
bien        = 621000 
agence      = 9000
estimation  = 375000
epargne     = 50000
restant     = 148153
rachat      = estimation - epargne

notaire         = 44300
garantie_relais = 4252.5
garantie_joint  = 5129.5
dossier_joint   = 800

apport = notaire + garantie_relais + garantie_joint + dossier_joint

# %% Relais
print('\n----- Projet Relais -----')
# notaire         = 44456
# garantie_relais = 1738
dossier_relais  = 0
relais          = 80/100*rachat
pret_sup        = rachat - relais
pret            = 455000
projet_relais   = notaire + garantie_relais + dossier_relais + relais + pret_sup + pret
apport_relais   = 46705
cout_relais     = projet_relais - apport_relais

print('Projet:  ', int(projet_relais))
print('Cout:    ', int(cout_relais))

# Echéancier
mensualite_pret     = 1851.74 # hors assurance?? 
mensualite_relais   = 23.75 # avec assurance
mensualite_pret_sup = 275.66 # seulement assurance??
mensualite_prelais  = mensualite_pret + mensualite_relais + mensualite_pret_sup

print('Echéancier mensuel:  ', mensualite_prelais)

# %% Joint
print('\n----- Projet Joint -----')
# notaire         = 44456
# garantie_joint  = 2190
# dossier_joint   = 1335
relais          = 300000
pret_sup        = rachat - relais
pret            = 455000
projet_joint    =   bien + agence + restant + \
                    notaire + garantie_joint + dossier_joint
                    
apport_joint    = 48382
cout_joint      = projet_joint - apport_joint

print('Projet:  ', int(projet_joint))
print('Cout:    ', int(cout_joint))


# Echéancier
mensualite_pret     = 1783.90 # hors assurance?? 
mensualite_en_cours = 1036.30
mensualite_pjoint   = mensualite_pret + mensualite_relais +\
                        mensualite_pret_sup + mensualite_en_cours

print('Echéancier mensuel:  ', mensualite_pjoint)

