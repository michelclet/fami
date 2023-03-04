% update: 2019
clear, close all, clc

revenu_net_imposable1 = 46.6e3*0.83;  % €
revenu_net_imposable2 = 15.5e3;  % €

revenus_net_imposables = [...
    revenu_net_imposable1 ... 
    revenu_net_imposable2 ...
    ];

nb_parts_foyer = 2;

% Seuils des tranches d'imposition 2019
seuils      = linspace(10,150,14) .* 1e3;
pourcents   = linspace(14,45,length(seuils))./100;

% Revenus net imposable du foyer
revenu_net_imposable = sum(revenus_net_imposables);

% Abattement de 10% sur le revenus net imposable du foyer
abattement = 90/100;
revenu_net_apres_abattement = abattement*revenu_net_imposable;

detect_tranche = revenu_net_apres_abattement/nb_parts_foyer >= seuils;

tranche = find(detect_tranche == 0, 1, 'first');

if isempty(tranche)
   tranche = length(detect_tranche) + 1;
end

if tranche == 1
    impot = 0;
else
    impot = (revenu_net_apres_abattement/nb_parts_foyer - seuils(tranche-1)) * pourcents(tranche-1) * nb_parts_foyer;
    for i = 1 : tranche-1-1
        impot = impot +   (seuils(i+1) - seuils(i)) * pourcents(i) * nb_parts_foyer;
    end
end

impot