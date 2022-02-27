import numpy as np 


tau = 20 #[-]  #Diesel https://stringfixer.com/fr/Compression_Ratio
D = 0.040 #[m]
#C = @valeur course@ #[m]
L = 0.1 #[m]
#mpiston = @valeur masse piston@ #[kg]
#mbielle = @valeur masse bielle@ #[kg] 
Q = 2800000 #[J/kg_inlet gas] pour un moteur essence 

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


def myfunc(rpm, s, theta, thetaC, deltaThetaC): #Elisa
    
    #Calcul de Q_output 
    
    m = 0.5 #Masse du gaz admis par ex -> A CALCULER !!
    Q_tot = Q*m #Chaleur de combustion pour un moteur essence de masse m
    
    Q_output = 0.5*Q_tot*(1-np.cos(np.pi*((theta-thetaC)/deltaThetaC)))
    
    dQ = 0.5*Q_tot*np.sin(np.pi*((theta-thetaC)/deltaThetaC))*(np.pi/deltaThetaC)
    
    
    #Calcul de V_output
    
    Vc = np.pi*D*D*R/2
    beta = L/R
    Vmin = Vc/(tau - 1)
    root = np.sqrt(beta**2 - np.sin(theta)**2)
    
    
    V = (Vc/2)*(1 - np.cos(theta) + beta - root) + Vmin
    
    dV = (Vc/2)*(np.sin(theta) + np.sin(theta)*np.cos(theta)/root)
                
    
    
    
    return (V_output, Q_output, F_pied_output, F_tete_output, p_output, t)  ;




