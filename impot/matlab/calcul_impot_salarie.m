function impot = calcul_impot_salarie(revenus_net_imposables, nb_parts_foyer)

% INPUT
% 1. revenus_net_imposables (array):    revenus net imposables du foyer
% 2. nb_parts_foyer (scalar):           nombre de parts du foyer 

% OUTPUT (Structure impot)
% 1. value (scalar):    Valeur de l'impôt calculé
% 2. tranche (scalar):  Tranche dans laquelle l'impôt calculé se trouve
%                       d'après les seuils de la loi française
% 3. taux (scalar):     Taux d'imposition

% Seuils des tranches d'imposition 2019
seuil1 = 9964;      % €
seuil2 = 27519;     % €
seuil3 = 73779;     % €
seuil4 = 156244;    % €

% Pourcentage de prévèvement par seuils
pourcent1 = 14/100; 
pourcent2 = 30/100;
pourcent3 = 41/100;
pourcent4 = 45/100;

% Revenus net imposable du foyer
revenu_net_imposable = sum(revenus_net_imposables);

% Abattement de 10% sur le revenus net imposable du foyer
abattement = 90/100;
revenu_net_apres_abattement = abattement*revenu_net_imposable;



if revenu_net_apres_abattement/nb_parts_foyer < seuil1
    % TRANCHE 1
    impot.value = 0;
    impot.tranche = 1;
    
elseif revenu_net_apres_abattement/nb_parts_foyer >= seuil1 && ...
        revenu_net_apres_abattement/nb_parts_foyer < seuil2
    
    % TRANCHE 2
    impot.value = (revenu_net_apres_abattement/nb_parts_foyer - seuil1) * pourcent1 * nb_parts_foyer;
    impot.tranche = 2;
    
elseif revenu_net_apres_abattement/nb_parts_foyer >= seuil2 && ...
        revenu_net_apres_abattement/nb_parts_foyer < seuil3
    
    % TRANCHE 3
    impot.value = ...
        (seuil2 - seuil1) * pourcent1 * nb_parts_foyer + ...
        (revenu_net_apres_abattement/nb_parts_foyer - seuil2) * pourcent2 * nb_parts_foyer;
    
    impot.tranche = 3;
    
elseif revenu_net_apres_abattement/nb_parts_foyer >= seuil3 && ...
        revenu_net_apres_abattement/nb_parts_foyer < seuil4 
    
    % TRANCHE 4
    impot.value = ...
        (seuil2 - seuil1) * pourcent1 * nb_parts_foyer + ...
        (seuil3 - seuil2) * pourcent2 * nb_parts_foyer + ...
        (revenu_net_apres_abattement/nb_parts_foyer - seuil3) * pourcent3 * nb_parts_foyer;
    
    impot.tranche = 4;
    
elseif revenu_net_apres_abattement/nb_parts_foyer >= seuil4
    
    % TRANCHE 5
    impot.value = ...
        (seuil2 - seuil1) * pourcent1 * nb_parts_foyer + ...
        (seuil3 - seuil2) * pourcent2 * nb_parts_foyer + ...
        (seuil4 - seuil3) * pourcent3 * nb_parts_foyer + ...
        (revenu_net_apres_abattement/nb_parts_foyer - seuil4) * pourcent4 * nb_parts_foyer;
    
    impot.tranche = 5;
    
end

impot.taux = round(impot.value/revenu_net_imposable*100*100)/100;
