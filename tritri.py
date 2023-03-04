def tritri(total, avanceFanny5050):
    """
    total :     dépensé dans le tritri
    equilibre : ce que Michel doit à Fanny en répartition 50/50
    """

    mc_60pc = 60/100*total
    mc = total/2 - avanceFanny5050
    # fg = total/2 + equilibre5050
    mc2fg_60pc = round(mc_60pc - mc,2)
    print('Michel doit', mc2fg_60pc, '€ à Fanny (Répartition 60/40)')
    
tritri(total=429.02, avanceFanny5050=109.83)

