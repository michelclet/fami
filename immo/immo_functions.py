def simulation_resultat(bien, taux, duree, apport, assurance, revenus, credit, notaire):
    
    taux        /= 100
    duree       *= 12
    # notaire     = 7.2/100 * bien
    dossier     = 1000
    garantie    = (bien + notaire + dossier - apport)/120
    
    pret        = bien - apport + notaire + dossier + garantie + assurance*duree
    mensualite  = ((pret*taux)/12) / (1-(1+(taux/12))**(-duree))
    interets    = mensualite*duree - pret 
    pret        += interets 
    
    endettement = (mensualite + credit)/revenus*100
    
    output = {}
    output['mensualite  ']      = round(mensualite)
    output['notaire     ']      = round(notaire)
    output['dossier     ']      = round(dossier)
    output['garantie    ']      = round(garantie)
    output['pret        ']      = round(pret)
    output['interets    ']      = round(interets)
    output['endettement ']      = round(endettement, 1)
    
    return output
    

def mensualite_resultat(prix, taux, duree):
    taux    /= 100
    duree   *= 12
    mensualite      = (prix*taux/12) / (1-(1+(taux/12))**(-duree))
    return mensualite
    
def interet_resultat(prix, taux, duree):
    taux    /= 100
    duree   *= 12
    mensualite      = (prix*taux/12) / (1-(1+(taux/12))**(-duree))
    interet         = mensualite*duree - prix
    return interet

def capital_resultat(mensualite, taux, duree):
    taux    /= 100
    duree   *= 12
    capital = (12*mensualite/taux) * (1-(1+(taux/12))**(-duree))
    return capital

def capacite_resultat(taux, duree, apport, assurance, revenus, credit, endettement):
    
    taux            /= 100
    duree           *= 12
    endettement     /= 100
    capacite        = endettement*revenus - credit
    mensualite_ha   = capacite
    capital         = (12*mensualite_ha/taux) * (1-(1+(taux/12))**(-duree))
    
    dossier         = 1000
    garantie        = capital/90
    
    notaire         = 7/100 * (capital + apport - dossier - garantie)
    bien            = capital + apport - notaire - dossier - garantie
    
    pret_ha         = capital 
    pret            = capital + assurance*duree
    interets        = mensualite_ha*duree - pret_ha 
    mensualite      = mensualite_ha + assurance
    
    output = {}
    output['bien        ']      = round(bien)
    output['mensualite  ']      = round(mensualite)
    output['notaire     ']      = round(notaire)
    output['dossier     ']      = round(dossier)
    output['garantie    ']      = round(garantie)
    output['pret        ']      = round(pret)
    output['interets    ']      = round(interets)
    output['endettement ']      = round(endettement*100, 1)
    
    return output
    