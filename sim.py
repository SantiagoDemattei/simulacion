import control as ctrl
import numpy as np
import time

# Se define la función de transferencia y se convierte a forma de espacio de estados
H = ctrl.tf([3], [1, 3, 2, 3]) 
sistema_ee = ctrl.tf2ss(H)
dt = 0.01 # definición del paso

# Se discretiza el sistema de espacio de estados para hacerlo adecuado para la simulación paso a paso
sistema_discreto = ctrl.sample_system(sistema_ee, dt, method='zoh')

x = np.zeros((sistema_discreto.A.shape[0], 1))
Tinicio = time.time()
Tfinal = Tinicio + 50  # Ejecuta por 50 segundos

while time.time() - Tinicio < Tfinal: 
    T = time.time() - Tinicio  # tiempo actual
    u = np.sin(2 * np.pi * 0.1 * T) # se define la señal de entrada: en este caso, una señal senoidal

    x = np.dot(sistema_discreto.A, x) + np.dot(sistema_discreto.B, u)
    y = np.dot(sistema_discreto.C, x) + np.dot(sistema_discreto.D, u)

    print(f"Tiempo: {T:.2f}, Salida del sistema: {y[0, 0]:.4f}")

    time.sleep(dt)
