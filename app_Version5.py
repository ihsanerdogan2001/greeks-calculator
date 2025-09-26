import streamlit as st
from greeks_calculator import BlackScholesGreeks

st.title("Opsiyon Greeks Hesaplayıcı (Black-Scholes Modeli)")

st.sidebar.header("Parametreler")
S = st.sidebar.number_input("Spot fiyatı (S)", value=100.0)
K = st.sidebar.number_input("Kullanım fiyatı (K)", value=100.0)
T = st.sidebar.number_input("Vade (yıl cinsinden, T)", value=1.0)
r = st.sidebar.number_input("Faiz oranı (r)", value=0.05)
sigma = st.sidebar.number_input("Volatilite (σ)", value=0.2)
option_type = st.sidebar.selectbox("Opsiyon tipi", ["call", "put"])

if st.sidebar.button("Hesapla"):
    greeks = BlackScholesGreeks(S, K, T, r, sigma, option_type)
    st.subheader(f"{option_type.capitalize()} Opsiyonu Greeks Sonuçları")
    st.write(f"**Delta:** {greeks.delta():.4f}")
    st.write(f"**Gamma:** {greeks.gamma():.4f}")
    st.write(f"**Vega:** {greeks.vega():.4f}")
    st.write(f"**Theta:** {greeks.theta():.4f}")
    st.write(f"**Rho:** {greeks.rho():.4f}")