import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import spectrogram  # Para calcular el espectrograma
from scipy.fftpack import dct, idct  # Importar la DCT y su inversa

# 1. Cargar la señal de audio
filename = 'Trabajo Fourier/ej1-señal-entrada (1).wav'  # Ruta al archivo WAV
fs, audio_signal = wavfile.read(filename)  # Lee el archivo WAV y obtiene la tasa de muestreo (fs) y la señal de audio

# Si la señal es estéreo, convertirla a mono (promediar las dos señales)
if len(audio_signal.shape) > 1:
    audio_signal = np.mean(audio_signal, axis=1)

# Normalizar la señal para que sus valores estén entre -1 y 1
audio_signal = audio_signal / np.max(np.abs(audio_signal))

# 2. Aplicar la Transformada Discreta del Coseno (DCT)
dct_signal = dct(audio_signal, type=2, norm='ortho')  # Calcula la DCT de la señal de audio
frequencies = np.linspace(0, fs / 2, len(dct_signal))  # Genera las frecuencias correspondientes a la DCT

# 3. Calcular la energía de cada frecuencia y la energía total
energies = np.abs(dct_signal)  # Calcula la energía de cada frecuencia (módulo  de la DCT)
total_energy = np.sum(energies)  # Calcula la energía total sumando todas las energías de las frecuencias

frec_NN_antes = np.count_nonzero(dct_signal)

print("frecuencias no nulas antes:", frec_NN_antes)

# 4. Ordenar las frecuencias por energía, de mayor a menor
sorted_indices = np.argsort(energies)[::-1]  # Ordena los índices de las frecuencias por energía, de mayor a menor
sorted_energies = energies[sorted_indices]  # Energías ordenadas
sorted_frequencies = frequencies[sorted_indices]  # Frecuencias ordenadas
sorted_dct_signal = dct_signal[sorted_indices]  # Señal DCT ordenada

# 5. Conservar un porcentaje específico de la energía total
percentage_energy = 0.75  # Porcentaje de energía que se desea conservar (por ejemplo, 75%)
cumulative_energy = np.cumsum(sorted_energies)  # Suma acumulativa de las energías ordenadas
threshold = percentage_energy * total_energy  # Umbral de energía que se desea conservar
kept_indices = cumulative_energy <= threshold  # Índices de frecuencias que cumplen con el umbral de energía

# Crear la señal comprimida en el dominio de la frecuencia, manteniendo solo las frecuencias con energía conservada
compressed_dct_signal = np.zeros_like(dct_signal)  # Crear un arreglo vacío para la señal comprimida
compressed_dct_signal[sorted_indices[kept_indices]] = sorted_dct_signal[kept_indices]  # Asignar solo las frecuencias conservadas

frec_NN_despues = np.count_nonzero(compressed_dct_signal)
print("frecuencias no nulas despues:", frec_NN_despues)

# 6. Reconstruir la señal comprimida usando la IDCT (Transformada Inversa del Coseno Discreto)
compressed_signal = idct(compressed_dct_signal, type=2, norm='ortho')  # Realiza la IDCT para obtener la señal comprimida en el dominio del tiempo

# 7. Normalizar y guardar la señal comprimida
compressed_signal = compressed_signal / np.max(np.abs(compressed_signal))  # Normaliza la señal comprimida
compressed_signal_int16 = np.int16(compressed_signal * 32767)  # Convierte la señal a formato int16 para guardarla como WAV
output_filename = 'trabajo/ej1-señal-comprimida.wav'  # Ruta de salida del archivo comprimido
wavfile.write(output_filename, fs, compressed_signal_int16)  # Guarda el archivo WAV comprimido

# 8. Visualizaciones
plt.figure(figsize=(12, 15))  # Establece el tamaño de la figura

# Espectro de frecuencias original
plt.subplot(4, 1, 1)  # Crea el primer subgráfico (1er gráfico de una columna de 4)
plt.plot(frequencies[:len(frequencies)//2], np.abs(dct_signal[:len(frequencies)//2]))  # Muestra el espectro de frecuencias de la señal original
plt.title("Espectro de Frecuencias Original")  # Título del gráfico
plt.xlabel("Frecuencia (Hz)")  # Etiqueta del eje x
plt.ylabel("Amplitud")  # Etiqueta del eje y
plt.grid(True)  # Muestra una cuadrícula

# Espectro de frecuencias comprimido
plt.subplot(4, 1, 2)  # Crea el segundo subgráfico
plt.plot(frequencies[:len(frequencies)//2], np.abs(compressed_dct_signal[:len(frequencies)//2]), color='orange')  # Muestra el espectro comprimido
plt.title("Espectro de Frecuencias Comprimido")  # Título del gráfico
plt.xlabel("Frecuencia (Hz)")  # Etiqueta del eje x
plt.ylabel("Amplitud")  # Etiqueta del eje y
plt.grid(True)  # Muestra una cuadrícula

# Comparación de las señales en el dominio del tiempo
plt.subplot(4, 1, 3)  # Crea el tercer subgráfico
plt.plot(audio_signal, label="Original")  # Muestra la señal original en el dominio del tiempo
plt.plot(compressed_signal, label="Comprimida", alpha=0.7)  # Muestra la señal comprimida
plt.title("Comparación en el Dominio del Tiempo")  # Título del gráfico
plt.xlabel("Muestras")  # Etiqueta del eje x
plt.ylabel("Amplitud")  # Etiqueta del eje y
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra una cuadrícula

plt.tight_layout()  # Ajusta el espacio entre los gráficos
plt.show()  # Muestra los gráficos

# 9. Calcular el ratio de compresión
compression_ratio = frec_NN_despues / frec_NN_antes  # Calcula el ratio de compresión

# Imprime la energía total, la energía de la señal comprimida, el porcentaje de energía conservada y el ratio de compresión
print(f"Energía total de la señal original: {total_energy:.2f}")
print(f"Energía total de la señal comprimida: {np.sum(np.abs(compressed_dct_signal)):.2f}")
print(f"Porcentaje de energía conservada: {100 * np.sum(np.abs(compressed_dct_signal)) / total_energy:.2f}%")
print(f"Ratio de compresión: {compression_ratio:.5f}")

# 10. Espectrograma en una imagen aparte
f, t, Sxx = spectrogram(audio_signal, fs)  # Calcula el espectrograma de la señal original

# Crear una figura separada para el espectrograma
plt.figure(figsize=(10, 6))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto')  # Muestra el espectrograma en escala logarítmica
plt.title("Espectrograma de la Señal Original")  # Título del gráfico
plt.xlabel("Tiempo (s)")  # Etiqueta del eje x
plt.ylabel("Frecuencia (Hz)")  # Etiqueta del eje y
plt.colorbar(label='Intensidad (dB)')  # Barra de color que indica la intensidad en dB
plt.grid(True)  # Muestra una cuadrícula

plt.tight_layout()  # Ajusta el espacio entre los gráficos
plt.show()  # Muestra el espectrograma

# 11. Explorar cómo cambia la señal reconstruida con diferentes porcentajes de energía conservada
percentages = [0.10, 0.25, 0.50, 0.75, 0.90, 1.00]  # Diferentes porcentajes de energía conservada

# Crear una figura con subgráficos para visualizar las señales reconstruidas con diferentes energías conservadas
fig, axes = plt.subplots(2, 3, figsize=(16, 8))  # 2x3 subgráficos
axes = axes.flatten()  # Convertir a una lista para iterar más fácilmente

for i, percentage in enumerate(percentages):  # Itera sobre cada porcentaje
    cumulative_energy = np.cumsum(sorted_energies)  # Suma acumulativa de las energías ordenadas
    threshold = percentage * total_energy  # Umbral de energía que se desea conservar
    kept_indices = cumulative_energy <= threshold  # Índices de frecuencias que cumplen con el umbral de energía
    compressed_dct_signal = np.zeros_like(dct_signal)  # Crear un arreglo vacío para la señal comprimida
    compressed_dct_signal[sorted_indices[kept_indices]] = sorted_dct_signal[kept_indices]  # Asignar solo las frecuencias conservadas
    compressed_signal = idct(compressed_dct_signal, type=2, norm='ortho')  # Realiza la IDCT para obtener la señal comprimida

    axes[i].plot(compressed_signal)  # Muestra la señal comprimida en el subgráfico
    axes[i].set_title(f"Comprimida (Energía {percentage * 100:.0f}%)")  # Título del subgráfico
    axes[i].grid(True)  # Muestra una cuadrícula

plt.tight_layout()  # Ajusta el espacio entre los subgráficos
plt.show()  # Muestra los subgráficos
