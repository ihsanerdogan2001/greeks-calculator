# greeks-calculator
Opsiyon Greeks Hesaplayıcı
import streamlit as st
import math
from scipy.stats import norm

st.set_page_config(page_title="Opsiyon Greeks Hesaplayıcı", layout="centered")

st.title("📈 Opsiyon Greeks Hesaplayıcı")
st.markdown("Black-Scholes modeline göre Delta, Gamma, Theta, Vega ve Rho hesaplaması")

# Girdi alanları
S = st.number_input("Hisse Fiyatı (S)", value=100.0)
K = st.number_input("Kullanım Fiyatı (K)", value=100.0)
T = st.number_input("Vade Süresi (Yıl)", value=1.0)
r = st.number_input("Risksiz Faiz Oranı (%)", value=5.0) / 100
sigma = st.number_input("Volatilite (%)", value=20.0) / 100
option_type = st.selectbox("Opsiyon Türü", ["call", "put"])

# Hesaplama fonksiyonu
def calculate_greeks(S, K, T, r, sigma, option_type):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        delta = norm.cdf(d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T))) - r * K * math.exp(-r * T) * norm.cdf(d2)
        rho = K * T * math.exp(-r * T) * norm.cdf(d2)
    else:
        delta = -norm.cdf(-d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T))) + r * K * math.exp(-r * T) * norm.cdf(-d2)
        rho = -K * T * math.exp(-r * T) * norm.cdf(-d2)

    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(T))
    vega = S * norm.pdf(d1) * math.sqrt(T)

    return {
        'Delta': delta,
        'Gamma': gamma,
        'Theta': theta,
        'Vega': vega / 100,
        'Rho': rho / 100
    }

# Hesapla butonu
if st.button("Hesapla"):
    greeks = calculate_greeks(S, K, T, r, sigma, option_type)
    st.subheader("📊 Sonuçlar")
    for greek, value in greeks.items():
        st.write(f"**{greek}**: {value:.4f}")
