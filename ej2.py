import numpy as np
from scipy.io import wavfile
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
import os

# 1. Cargar la señal de audio desde un archivo WAV
filename = 'Trabajo Fourier/ej2-se\u00f1al-entrada (1).wav'  # Ruta al archivo WAV
fs, audio_signal = wavfile.read(filename)  # fs = frecuencia de muestreo, audio_signal = datos de la se\u00f1al

# Si la se\u00f1al es est\u00e9reo, convertirla a mono tomando el promedio de los dos canales
if len(audio_signal.shape) > 1:
    audio_signal = np.mean(audio_signal, axis=1)

# Normalizar la se\u00f1al dividiendo por su valor m\u00e1ximo (para evitar problemas de escala)
audio_signal = audio_signal / np.max(np.abs(audio_signal))

# 2. Aplicar la Transformada Discreta de Coseno (DCT) a la se\u00f1al normalizada
dct_signal = dct(audio_signal, norm='ortho')  # Calcula la DCT de la se\u00f1al

# 3. Eliminar el ruido manualmente en las franjas especificadas
# Crear una copia de los coeficientes DCT para aplicar el filtrado
filtered_dct_signal = np.copy(dct_signal)

# Filtrar el ruido en la franja de 0 a 100,000 coeficientes (amplitudes > 6 o < -6)
filtered_dct_signal[:100000][(dct_signal[:100000] > 6) | (dct_signal[:100000] < -6)] = 0

# Filtrar el ruido en la franja de 100,000 a 200,000 coeficientes (amplitudes > 4 o < -3)
filtered_dct_signal[100000:200000][(dct_signal[100000:200000] > 4) | (dct_signal[100000:200000] < -3)] = 0

# 4. Reconstruir la se\u00f1al filtrada usando la Transformada Inversa de Coseno (IDCT)
filtered_signal = idct(filtered_dct_signal, norm='ortho')  # Reconstruye la se\u00f1al a partir de la DCT filtrada

# Normalizar la se\u00f1al filtrada para convertirla a un rango de enteros de 16 bits (formato WAV)
filtered_signal = np.int16(filtered_signal / np.max(np.abs(filtered_signal)) * 32767)

# 5. Ecualizar la se\u00f1al filtrada
# Definir los puntos de corte en las frecuencias bajas, medias y altas
low_cutoff = int(500 / (fs / 2) * len(dct_signal))
mid_cutoff = int(2000 / (fs / 2) * len(dct_signal))
high_cutoff = len(dct_signal)

# Definir factores de amplificaci\u00f3n/atenuaci\u00f3n
lowboost = 5.5  # Amplificar frecuencias bajas
midcut = 0.2    # Atenuar frecuencias medias
highcut = 0.1   # Atenuar frecuencias altas

# Aplicar los factores de ecualizaci\u00f3n a las diferentes bandas de frecuencias
filtered_dct_signal[:low_cutoff] *= lowboost
filtered_dct_signal[low_cutoff:mid_cutoff] *= midcut
filtered_dct_signal[mid_cutoff:high_cutoff] *= highcut

# Reconstruir la se\u00f1al ecualizada
equalized_signal = idct(filtered_dct_signal, norm='ortho')
equalized_signal = np.int16(equalized_signal / np.max(np.abs(equalized_signal)) * 32767)

# 6. Guardar las se\u00f1ales filtrada y ecualizada como archivos WAV
output_folder = r"C:\\Users\\USUARIO\\Desktop\\3 curso\\variable compleja\\Trabajo Fourier"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

wavfile.write(os.path.join(output_folder, 'ej2-se\u00f1al-filtrada.wav'), fs, filtered_signal)
wavfile.write(os.path.join(output_folder, 'ej2-se\u00f1al-ecualizada.wav'), fs, equalized_signal)

# 7. Graficar los resultados en una sola ventana
plt.figure(figsize=(12, 12))

# Gr\u00e1fica de la se\u00f1al original
plt.subplot(4, 1, 1)
plt.plot(audio_signal, color='blue')
plt.title('Se\u00f1al Original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.grid(True)

# Espectro de la se\u00f1al original con ruido
plt.subplot(4, 1, 2)
plt.plot(dct_signal, '.', color='orange')
plt.title('Espectro DCT de la Se\u00f1al Original con Ruido')
plt.xlabel('Coeficientes DCT')
plt.ylabel('Amplitud')
plt.grid(True)

# Espectro de la se\u00f1al original sin ruido
plt.subplot(4, 1, 3)
plt.plot(filtered_dct_signal, '.', color='green')
plt.title('Espectro DCT de la Se\u00f1al Original Sin Ruido')
plt.xlabel('Coeficientes DCT')
plt.ylabel('Amplitud')
plt.grid(True)

# Gr\u00e1fica de la se\u00f1al ecualizada
plt.subplot(4, 1, 4)
plt.plot(equalized_signal, color='purple')
plt.title('Se\u00f1al Ecualizada')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()

print("Se\u00f1ales Filtrada y Ecualizada guardadas como archivos WAV en la carpeta especificada.")