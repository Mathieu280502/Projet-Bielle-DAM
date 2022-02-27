import numpy as np 


tau = 20 #[-]  #Diesel https://stringfixer.com/fr/Compression_Ratio
D = 0.040 #[m]
#C = @valeur course@ #[m]
L = 0.1 #[m]
#mpiston = @valeur masse piston@ #[kg]
#mbielle = @valeur masse bielle@ #[kg] 
#Q = @valeur chaleur emise par fuel par kg de melange admis@ #[J/kg_inlet gas]

R = 0.02



theta = np.arange(-180, 181, 1)  #initialisation en degré
theta =  theta * (np.pi / 180)         #remise en gradient 

def volume_et_derivee (R, D, L, tau, theta): 
    
    Vc = np.pi * D * D * R / 2
    beta = L / R
    
    sin_o = np.sin(theta)
    cos_o = np.cos(theta)
    
    root = np.sqrt(beta**2 - sin_o**2)
    
    V = (1 - cos_o + beta + root) * Vc / 2 + Vc / (tau -1)
    
    dV = (sin_o + sin_o * cos_o / root) * Vc / 2
    
    return (V, dV)

V , dV = volume_et_derivee (R, D, L, tau, theta) 




