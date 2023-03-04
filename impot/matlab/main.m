% ------------------------------------------------------------------------
%                               CALCUL IMPOT
% ------------------------------------------------------------------------

% update: 2019
clear, close all, clc

revenu_net_imposable1 = 36899;  % €
revenu_net_imposable2 = 36899;  % €

revenus_net_imposables = [...
    revenu_net_imposable1 ... 
    revenu_net_imposable2 ...
    ];

nb_parts_foyer = 2;

impots = calcul_impot_salarie(revenus_net_imposables, nb_parts_foyer);

disp(['Tranche d''imposition:   ' num2str(round(impots.tranche))])
disp(['Taux d''imposition:      ' num2str(round(impots.taux*10)/10) ' %'])
disp(['Impots à payer:         ' num2str(round(impots.value)) ' €'])
