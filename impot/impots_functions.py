import numpy as np
import matplotlib.pyplot as plt

def get_impot(revenus_net_imposables, n_parts):
    """
    INPUT
    1. revenus_net_imposables (array):    revenus net imposables du foyer
    2. n_parts (scalar):           nombre de parts du foyer 
    
    OUTPUT (Structure impot)
    1. valeur:   Valeur de l'impôt calculé
    2. tranche:  Tranche dans laquelle l'impôt calculé se trouve
                  d'après les seuils de la loi française
    3. taux:     Taux d'imposition
    """
    
    # % Seuils des tranches d'imposition 2019
    seuil1 = 10777
    seuil2 = 27478
    seuil3 = 78570
    seuil4 = 168994
    
    # % Pourcentage de prévèvement par seuils
    pourcent1 = 11/100 
    pourcent2 = 30/100
    pourcent3 = 41/100
    pourcent4 = 45/100
    
    # % Revenus net imposable du foyer
    revenu_net_imposable = revenus_net_imposables;
    
    # % Abattement de 10% sur le revenus net imposable du foyer
    abattement                  = 90/100
    revenu_net_apres_abattement = abattement*revenu_net_imposable
    if revenu_net_apres_abattement/n_parts < seuil1:
        # % TRANCHE 1
        value = 0
        tranche = 1
        
    elif revenu_net_apres_abattement/n_parts >= seuil1 and\
            revenu_net_apres_abattement/n_parts < seuil2:
        
        # % TRANCHE 2
        value = (revenu_net_apres_abattement/n_parts - seuil1) * pourcent1 * n_parts
        tranche = 2
        
    elif revenu_net_apres_abattement/n_parts >= seuil2 and\
            revenu_net_apres_abattement/n_parts < seuil3:
        
        # % TRANCHE 3
        value = (seuil2 - seuil1) * pourcent1 * n_parts +\
            (revenu_net_apres_abattement/n_parts - seuil2) * pourcent2 * n_parts
        
        tranche = 3
        
    elif revenu_net_apres_abattement/n_parts >= seuil3 and\
            revenu_net_apres_abattement/n_parts < seuil4:
        
        # % TRANCHE 4
        value = (seuil2 - seuil1) * pourcent1 * n_parts +\
            (seuil3 - seuil2) * pourcent2 * n_parts +\
            (revenu_net_apres_abattement/n_parts - seuil3) * pourcent3 * n_parts
        
        tranche = 4
        
    elif revenu_net_apres_abattement/n_parts >= seuil4:
        
        # % TRANCHE 5
        value = (seuil2 - seuil1) * pourcent1 * n_parts +\
            (seuil3 - seuil2) * pourcent2 * n_parts +\
            (seuil4 - seuil3) * pourcent3 * n_parts +\
            (revenu_net_apres_abattement/n_parts - seuil4) * pourcent4 * n_parts
        
        tranche = 5

    taux = round(value/revenu_net_imposable*100*100)/100
    
    value = np.floor(value)
    
    output              = {}
    output['value']    = value
    output['tranche']   = tranche
    output['taux']      = taux
    
    return output


# revenus_brut            = [65000]
# transport               = 34
# ticket_resto            = 0
# revenus_net_imposables = []
# for revenu in revenus_brut:
#     net_imposable = revenu*.788 + (transport - ticket_resto)*12
#     net_imposable *= .9
#     revenus_net_imposables.append(net_imposable)

n_parts     = 1
# revenus_year = 77e3 
# revenus_net_imposable_mc = 66e3

revenu = 75e3 
output = get_impot(revenu, n_parts)

for key in output.keys():
    print(key, output[key])
    if key == 'value':
        print('value per month', round(output[key]/12))
    
# print('Salaire mensuel brut :', round(revenus_year/12))
# print('Salaire mensuel net :', round(revenus_year/15.3))
# print("Salaire mensuel net d'impot':", round(revenus_year/15.3 - output['value']/12))