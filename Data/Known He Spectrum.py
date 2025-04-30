import numpy as np
import matplotlib.pyplot as plt

data = np.array([ 381.96074, 381.96074, 381.96074, 381.96074, 381.96074, 383.3554, 387.1791, 388.8648, 388.8648, 393.5912, 396.47291, 402.3973, 402.61914, 402.61914, 402.61914, 402.61914, 402.61914, 412.08154, 412.08154, 414.3761, 416.8967, 438.79296, 443.7551, 447.14802, 447.14802, 447.14802, 447.14802, 447.14802, 471.31457, 471.31457, 492.19313, 501.56783, 504.7738, 587.5621, 587.5621, 587.5621, 587.5621, 667.8151
])

def wavelength_to_rgb(wavelength):
    gamma = 0.8
    intensity_max = 255
    factor = 0.0
    R = G = B = 0.0

    if 380 <= wavelength <= 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 < wavelength <= 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 < wavelength <= 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 < wavelength <= 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 < wavelength <= 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 < wavelength <= 780:
        R = 1.0
        G = 0.0
        B = 0.0

    if 380 <= wavelength <= 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 < wavelength <= 700:
        factor = 1.0
    elif 700 < wavelength <= 780:
        factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 700)
    else:
        factor = 0.0

    def correct(color, factor):
        if color == 0.0:
            return 0
        return round(intensity_max * pow(color * factor, gamma))

    return (correct(R, factor)/255, correct(G, factor)/255, correct(B, factor)/255)

counts, bins = np.histogram(data, bins=34)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
bin_widths = np.diff(bins)

colors = [wavelength_to_rgb(wl) for wl in bin_centers]

for i in range(len(bin_centers)):
    plt.bar(bin_centers[i], counts[i], width= 1, color=colors[i], edgecolor='black', linewidth=0.5)

plt.xlabel('Wavelength (nm)')
plt.xlim(380, 700)
plt.title('Known He Spectrum (Colored by Wavelength)')

plt.show()
