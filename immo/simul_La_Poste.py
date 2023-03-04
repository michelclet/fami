vente   = 386100
du      = 148421
bien    = 630000
frais   = 47525 + 4647 + 1000 + 290 # notaire + garantie + dossier + expertise
apport  = 49999
pret    = du + bien + frais - apport

relais      = 88.355/100*(vente - du)
pret_long   = pret - relais

plu_value   = vente - relais 