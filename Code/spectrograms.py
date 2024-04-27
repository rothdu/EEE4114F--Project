import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import square, ShortTimeFFT
from scipy.signal.windows import gaussian
from scipy.io import wavfile


fs, data = wavfile.read("Sounds/Snares/1.wav")

x = data

T_x, N = 1 / fs, len(x)  # 20 Hz sampling rate for 50 s signal

t_x = np.arange(N) * T_x  # time indexes for signal


g_std = 200  # standard deviation for Gaussian window in samples

win = gaussian(1000, std=g_std, sym=True)  # symmetric Gaussian wind.

SFT = ShortTimeFFT(win, hop=200, fs=fs, mfft=16000, scale_to='psd')

Sx2 = SFT.spectrogram(x)  # calculate absolute square of STFT

# The rest is just plotting the spectrogram - we may not need to do this

fig1, ax1 = plt.subplots(figsize=(6., 4.))  # enlarge plot a bit

t_lo, t_hi = SFT.extent(N)[:2]  # time range of plot

ax1.set_title(rf"Spectrogram ({SFT.m_num*SFT.T:g}$\,s$ Gaussian " +

              rf"window, $\sigma_t={g_std*SFT.T:g}\,$s)")

ax1.set(xlabel=f"Time $t$ in seconds ({SFT.p_num(N)} slices, " +

               rf"$\Delta t = {SFT.delta_t:g}\,$s)",

        ylabel=f"Freq. $f$ in Hz ({SFT.f_pts} bins, " +

               rf"$\Delta f = {SFT.delta_f:g}\,$Hz)",

        xlim=(t_lo, t_hi))

Sx_dB = 10 * np.log10(np.fmax(Sx2, 1e-4))  # limit range to -40 dB

im1 = ax1.imshow(Sx_dB, origin='lower', aspect='auto',

                 extent=SFT.extent(N), cmap='magma')

ax1.plot(t_x, 'g--', alpha=.5, label='$f_i(t)$')

fig1.colorbar(im1, label='Power Spectral Density ' +

                         r"$20\,\log_{10}|S_x(t, f)|$ in dB")


# Shade areas where window slices stick out to the side:

for t0_, t1_ in [(t_lo, SFT.lower_border_end[0] * SFT.T),

                 (SFT.upper_border_begin(N)[0] * SFT.T, t_hi)]:

    ax1.axvspan(t0_, t1_, color='w', linewidth=0, alpha=.3)

for t_ in [0, N * SFT.T]:  # mark signal borders with vertical line

    ax1.axvline(t_, color='c', linestyle='--', alpha=0.5)

ax1.legend()

fig1.tight_layout()

plt.show()