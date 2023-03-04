% CALCUL IMPOT 2017
clear
close all
clc


options = 33.192e3; % €
taxe_achat_options = 0.18*options;
rev1 = 40.5e3 ;
rev1_bis = rev1 + options - taxe_achat_options;   % €
rev2 = 16.5e3;   % €

revs = [rev1 rev2];
revs_bis = [rev1_bis rev2];
nb_parts = 2.5;

impot = calcul_impots(revs_bis, nb_parts);

impot.final_avec_options = impot.final + taxe_achat_options;
impot.final_only_options  = impot.final_avec_options - impot.t1_final;

gain = options - impot.final_only_options;

revenus = 20000:50:300e3;

for i = 1 : length(revenus)
    rev = revenus(i);
    impot1 = calcul_impots(rev, 1);
    impot2 = calcul_impots(rev, 2);
    impot3 = calcul_impots(rev, 2.5);
    
    impots1(i) = impot1.final;
    impots2(i) = impot2.final;
    impots3(i) = impot3.final;
end

plot(revenus./1e3,impots1./1e3,'linewidth',2)
hold on
plot(revenus./1e3,impots2./1e3,'linewidth',2)
plot(revenus./1e3,impots3./1e3,'linewidth',2)
axis tight
title(['Impots vs revenus'])
xlabel('Revenus net imposable total (x1000)')
ylabel('Impots / an (x1000)')
legend('1 part', '2 parts', '2.5 parts','Location','northwest')