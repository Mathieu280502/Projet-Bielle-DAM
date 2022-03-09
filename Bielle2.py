import numpy as np 
import matplotlib 
from matplotlib import pyplot 
from scipy.integrate import solve_ivp

tau = 20 #[-]  #Diesel https://stringfixer.com/fr/Compression_Ratio
D = 0.040 #[m]
C = 0.04 #@valeur course@ #[m]
L = 0.1 #[m]
mpiston = 0.2#@valeur masse piston@ #[kg]
mbielle = 0.3#@valeur masse bielle@ #[kg] 
Q = 2190 #@valeur chaleur emise par fuel par kg de melange admis@ #[J/kg_inlet gas]


theta = np.arange(-180, 180, 1)  #initialisation en degré
theta =  theta * (np.pi / 180)         #remise en gradient 


def myfunc(rpm, s, theta, thetaC, deltaThetaC): #Elisa
    # Calcul des constantes 
    
    p0 = s*1E+5
    w = 2 * np.pi * rpm / 60
    R = C/2
    
    m = 0.5 #Masse du gaz admis par ex -> A CALCULER !!
    
    sigmaC = 450E+6  #resistannce de compression (donné) [450 MPa]
    E = 200E+9       #module d’élasticité (donné)  [200 GPa]

    ddz = R * w * w * np.cos(theta)
    #Calcul de Q_output 
    
    Q_tot = Q*m #Chaleur de combustion pour un moteur essence de masse m
    
    Q_output = 0.5*Q_tot*(1-np.cos(np.pi*((theta-thetaC)/deltaThetaC)))   #dQ = 0.5*Q_tot*np.sin(np.pi*((theta-thetaC)/deltaThetaC))*(np.pi/deltaThetaC)
    
    #Calcul de V_output
    
    Vc = np.pi*D*D*R/2
    beta = L/R
    Vmin = Vc/(tau - 1)
    root = np.sqrt(beta**2 - np.sin(theta)**2)

    V_output = (Vc/2)*(1 - np.cos(theta) + beta - root) + Vmin    #dV = (Vc/2)*(np.sin(theta) + np.sin(theta)*np.cos(theta)/root)
                
    #Calcul de p_output
    
    p_output = pression(theta, p0, Vc, beta, Vmin, Q_tot, thetaC, deltaThetaC) 
    
    F_pression = np.pi * D**2 * p_output / 4
    
    #Cacul des forces  
    
    F_pied_output = F_pression - mpiston * ddz
    
    F_tete_output = -F_pression + (mpiston + mbielle) * ddz
    
    
    # Calcul du flambage et de l'épesseur critique
    
    F_crit = max (F_pied_output - F_tete_output)
    
    coeffxx = [-np.pi*E*419/12*11*sigmaC, F_crit*np.pi*np.pi*E*419/12 , F_crit*(1*L)*(1*L)*11*sigmaC]
    coeffyy = [-np.pi*E*131/12*11*sigmaC, F_crit*np.pi*np.pi*E*131/12 , F_crit*(0.5*L)*(0.5*L)*11*sigmaC]
    
    txx = np.sqrt(max(np.roots(coeffxx)))
    tyy = np.sqrt(max(np.roots(coeffyy)))
    
    t = max (txx , tyy)
    
    return (V_output, Q_output, F_pied_output, F_tete_output, p_output, t)  ;


def pression (theta, p0, Vc, beta, Vmin, Q_tot, thetaC,deltaThetaC):
    
    gamma = 1.3
    
    def dpdt (o, p) : 
         root = np.sqrt(beta**2 - np.sin(o)**2)
         V = (Vc/2)*(1 - np.cos(o) + beta - root) + Vmin
         dV = (Vc/2)*(np.sin(o) + np.sin(o)*np.cos(o)/root)
         dQ = 0.5*Q_tot*np.sin(np.pi*((o-thetaC)/deltaThetaC))*(np.pi/deltaThetaC)
         
         return (-gamma*dV* p + (gamma-1) * dQ ) / V
     
    sol = solve_ivp(dpdt, t_span = (theta[0], max(theta)), y0 = [p0], t_eval = theta)
     
    return sol.y[0]
 
V_output, Q_output, F_pied_output, F_tete_output, p_output, t = myfunc(20, 1, theta, np.pi, np.pi/4)


p = pression (theta, 100000, 1, 3, 3, 2390, np.pi,np.pi/4) * 10**-5



pyplot.plot(theta, -F_tete_output + F_pied_output)


pyplot.show()
    

