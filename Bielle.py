import numpy as np 


tau = 20 #[-]  #Diesel https://stringfixer.com/fr/Compression_Ratio
"""D = @valeur alesage@ #[m]
C = @valeur course@ #[m]
L = @valeur longueur bielle@ #[m]
mpiston = @valeur masse piston@ #[kg]
mbielle = @valeur masse bielle@ #[kg]
Q = @valeur chaleur emise par fuel par kg de melange admis@ #[J/kg_inlet gas]
"""
print(f"tau = {tau}")

def chaleur_de_combustion (Qtot, theta, td, Dtcomb):
    
    ##  Mise en radian (np.cos fonctionne avec des radians)
    theta = theta * (np.pi / 180)
    td = td * (np.pi / 180)
    Dtcomb = Dtcomb * (np.pi / 180)
    
    
    Q = Qtot/2 * (1 - np.cos(np.pi * (theta - td)/ Dtcomb))
    return Q

def position_piston ()
theta = np.arange(-180, 180, 60)
td = 40
tcomb = 100
Qtot = 300

print(chaleur_de_combustion(Qtot, theta, td, tcomb))




