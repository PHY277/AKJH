import numpy as np
import matplotlib.pyplot as plt

data = np.array([ 403.508, 404.131, 404.353, 417.616, 422.774, 423.691, 423.705, 424.178, 443.274, 444.703, 453.041, 460.148, 460.716, 461.387, 462.139, 463.054, 464.308, 478.813, 480.329, 489.511, 498.737, 499.436, 500.148, 500.270, 500.515, 500.732, 501.062, 501.639, 502.566, 504.510, 549.567, 553.536, 566.663, 567.602, 567.956, 568.621, 571.077, 574.730, 592.781, 593.178, 594.024, 594.165, 595.239, 616.776, 637.962, 648.205, 661.056
    
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
plt.title('Known N2 Spectrum (Colored by Wavelength)')

plt.show()
