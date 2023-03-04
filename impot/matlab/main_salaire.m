clc
salaire_brut = 47.55e3;
ticket_resto = 4*20;
salaire_net_mois = salaire_brut*0.791/12 - ticket_resto;

impot_mois = salaire_brut*0.82/12 * 0.079;

salaire_apres_impot = salaire_net_mois - impot_mois;
salaire_apres_impot