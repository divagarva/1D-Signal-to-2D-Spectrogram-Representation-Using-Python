import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate a 1D signal (sinusoidal wave with added noise)
fs = 1000  # Sampling frequency in Hz
N = 10000  # Number of data points
t = np.linspace(0, 10, N, endpoint=False)  # Time vector for 10 seconds
signal_1d = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 50 * t) + 0.5 * np.random.randn(t.size)

# Generate a spectrogram, which is a 2D representation of the signal
frequencies, times, Sxx = signal.spectrogram(signal_1d, fs)

# Plot the spectrogram (2D signal)
plt.figure(figsize=(10, 6))
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram of 1D Signal (Converted to 2D)')
plt.colorbar(label='Intensity [dB]')
plt.show()
