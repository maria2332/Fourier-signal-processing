<h1 align="center">🎧 Audio Signal Processing with DCT (Fourier Techniques)</h1>

<p align="center">
  Academic project focused on <strong>Discrete Cosine Transform (DCT)</strong> for
  <strong>audio compression, noise filtering and equalization</strong>, implemented in Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Scientific-3776AB?logo=python&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Signal%20Processing-DCT-6A4C93?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Fourier-Analysis-FFB703?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Audio-WAV-2A9D8F?style=for-the-badge"/>

  <a href="https://deepwiki.com/maria2332/Fourier-signal-processing" target="_blank">
    <img src="https://img.shields.io/badge/DeepWiki-Documentation-purple?style=for-the-badge"/>
  </a>
  
</p>

---

## 📚 Project Documentation (External)

An automatically generated documentation view of this repository is available via DeepWiki:

👉 https://deepwiki.com/maria2332/Fourier-signal-processing

---

## 👩‍🎓 Academic Context

- **Student:** María Arribas Ballesteros  
- **Degree:** Ingeniería Matemática  
- **Course:** Variable Compleja / Fourier Analysis  

This project explores the application of **Fourier-related techniques** to real audio signals,
using the **Discrete Cosine Transform (DCT)** as a practical tool for:

- Signal compression
- Noise removal
- Frequency-based equalization

---

## 🎯 Project Objectives

- Apply the **Discrete Cosine Transform (DCT)** to audio signals
- Analyze signals in the **frequency domain**
- Perform:
  - Energy-based compression
  - Noise filtering in selected frequency bands
  - Audio equalization (low / mid / high frequencies)
- Reconstruct signals using **Inverse DCT (IDCT)**
- Visualize results in both time and frequency domains

---

## 🧠 Overview of the Exercises

### 🔹 Exercise 1 — Audio Compression using DCT
- Compute the DCT of an audio signal
- Rank frequency coefficients by energy
- Retain a fixed percentage of total energy
- Zero out low-energy coefficients
- Reconstruct the compressed signal using IDCT
- Measure:
  - Number of non-zero coefficients
  - Compression ratio
  - Energy preservation
- Visualize:
  - Original vs compressed spectra
  - Time-domain comparison
  - Spectrogram of the original signal
  - Reconstruction with different energy thresholds

📌 This exercise illustrates how **most signal energy is concentrated in a small number of DCT coefficients**, enabling efficient compression.

---

### 🔹 Exercise 2 — Noise Filtering and Equalization
- Apply DCT to a noisy audio signal
- Remove noise by thresholding coefficients in specific frequency ranges
- Reconstruct the filtered signal
- Apply frequency-based equalization:
  - Boost low frequencies
  - Attenuate mid and high frequencies
- Save:
  - Filtered signal
  - Equalized signal
- Visualize:
  - Original signal
  - DCT spectrum before filtering
  - DCT spectrum after filtering
  - Final equalized signal

📌 This exercise demonstrates **manual frequency-domain filtering and equalization** using DCT coefficients.

---

## 🛠️ Technologies Used

- **Python 3**
- **NumPy**
- **SciPy**
  - `scipy.fftpack.dct`, `idct`
  - `scipy.io.wavfile`
- **Matplotlib**
- WAV audio format

---

## 📁 Repository Structure

```text
trabajo-fourier-dct-audio/
├── ej1_compresion_dct.py
├── ej2_filtrado_ecualizacion_dct.py
├── data/                  # (optional) small example WAV files
├── output/                # generated audio files (ignored by git)
├── README.md
├── requirements.txt
└── .gitignore
````

---

## ⚙️ Installation & Requirements

Install dependencies using:

```bash
pip install numpy scipy matplotlib
```

---

## ▶️ How to Run

### Exercise 1 — Compression

```bash
python ej1_compresion_dct.py
```

### Exercise 2 — Filtering & Equalization

```bash
python ej2_filtrado_ecualizacion_dct.py
```

> Output WAV files will be generated locally and are not tracked by Git.

---

## 📊 Key Concepts Illustrated

* Discrete Cosine Transform (DCT)
* Energy compaction
* Frequency-domain filtering
* Signal reconstruction
* Compression ratio
* Audio equalization
* Time vs frequency domain interpretation

---

## 🔍 Final Remarks

This project provides a **practical and intuitive application of Fourier-related techniques**
to real audio signals.

It highlights how mathematical concepts such as **orthogonal transforms and energy distribution**
can be used for:

* Data compression
* Noise reduction
* Signal enhancement

The project bridges **theoretical mathematics** and **applied signal processing** through
clear, reproducible Python implementations.


