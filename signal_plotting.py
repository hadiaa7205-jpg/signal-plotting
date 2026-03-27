Project: Signal Plotting
Purpose: To visualize basic telecom signals using Python
Author: Hadia Batool

import numpy as np
import matplotlib.pyplot as plt

Create time vector
t = np.linspace(0, 1, 1000) 

Generate signals
frequency1 = 5  
frequency2 = 10 

sine_wave = np.sin(2 * np.pi * frequency1 * t)
cosine_wave = np.cos(2 * np.pi * frequency2 * t)

Plot signals
plt.figure(figsize=(10,5))
plt.plot(t, sine_wave, label='5 Hz Sine Wave')
plt.plot(t, cosine_wave, label='10 Hz Cosine Wave', linestyle='--')
plt.title('Signal Plotting - Sine and Cosine Waves')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
