import pandas as pd
import matplotlib.pyplot as plt
from rtc_utils import compute_drtc

# Lecture des données
data = pd.read_csv("sample_data.csv")

# Calcul D_RTC
data["D_RTC"] = compute_drtc(data["mass"], data["volume"], data["age"])

# Tracé
plt.plot(data["radius"], data["D_RTC"], label="D_RTC")
plt.xlabel("Rayon (kpc)")
plt.ylabel("D_RTC")
plt.legend()
plt.title("Profil RTC")
plt.savefig("drtc_profile.png")
plt.show()
