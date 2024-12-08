#Vref>Vin ise Vo=Vcc
#Vin>Vref ise V0=Vee
import numpy as np
import matplotlib.pyplot as plt

# Parametreler
Vref = 7  # Referans voltajı (7V)
Vcc = 12  # Yüksek voltaj (pozitif doyma)
Vee = 0   # Düşük voltaj (negatif doyma)

# Zaman dilimi
t = np.linspace(0, 10, 1000)  # 0 ile 10 saniye arasında 1000 veri noktası

# Giriş voltajı (Vin) fonksiyonu - burada sinusoidal bir değişim kullanıyoruz
Vin = 6 + 6 * np.sin(2 * np.pi * 0.1 * t)  # 6V'dan başlayıp 12V'a kadar dalgalanacak

# Çıkış voltajı (Vo) hesaplaması
Vo = np.where(Vin > Vref, Vee, Vcc)  # Eğer Vref > Vin ise Vo = Vcc (12V), aksi halde Vo = Vee (0V)

# Grafiği çizme
plt.figure(figsize=(10, 6))
plt.plot(t, Vin, label="Giriş Voltajı (Vin)", color="b", linestyle='-', linewidth=2)
plt.plot(t, Vo, label="Çıkış Voltajı (Vo)", color="r", linestyle='--', linewidth=2)
plt.axhline(y=Vref, color='g', linestyle=':', label="Referans Voltajı (Vref = 7V)")
plt.title("Op-Amp Kontrolör Çıkışı \n G220100027")
plt.xlabel("Zaman (s)")
plt.ylabel("Voltaj (V)")
plt.legend()
plt.grid(True)
plt.show()