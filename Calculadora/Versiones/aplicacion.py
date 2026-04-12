import streamlit as st

st.title("Simulador de pérdidas técnicas en renovables")

# Hidroeléctrica
st.header("Hidroeléctrica")
hidro_potencia = st.slider("Potencia hidro (MW)", 0.0, 100.0, 50.0)
hidro_conv = st.slider("Eficiencia conversión hidro (%)", 50, 100, 90)
hidro_turbulencia = st.slider("Pérdidas por turbulencia (%)", 0, 20, 5)
hidro_transporte = st.slider("Pérdidas por transporte de agua (%)", 0, 20, 5)

hidro_eta = (hidro_conv/100) * (1 - hidro_turbulencia/100) * (1 - hidro_transporte/100)
hidro_util = hidro_potencia * hidro_eta
st.write(f"Eficiencia total hidro: {hidro_eta*100:.2f}%")
st.write(f"Energía útil hidro: {hidro_util:.2f} MW")
st.image("hidro.png", caption="Diagrama de represa hidroeléctrica")

# Solar
st.header("Solar")
solar_potencia = st.slider("Potencia solar (MW)", 0.0, 100.0, 30.0)
solar_conv = st.slider("Eficiencia conversión solar (%)", 10, 25, 18)
solar_temp = st.slider("Pérdidas por temperatura (%)", 0, 20, 10)
solar_inversor = st.slider("Pérdidas por conversión DC/AC (%)", 0, 20, 5)

solar_eta = (solar_conv/100) * (1 - solar_temp/100) * (1 - solar_inversor/100)
solar_util = solar_potencia * solar_eta
st.write(f"Eficiencia total solar: {solar_eta*100:.2f}%")
st.write(f"Energía útil solar: {solar_util:.2f} MW")
st.image("solar.png", caption="Diagrama de panel solar con inversor")

# Eólica
st.header("Eólica")
eolica_potencia = st.slider("Potencia eólica (MW)", 0.0, 100.0, 40.0)
eolica_conv = st.slider("Eficiencia conversión eólica (%)", 30, 50, 40)
eolica_aero = st.slider("Pérdidas aerodinámicas (%)", 0, 20, 8)
eolica_variab = st.slider("Pérdidas por variabilidad del viento (%)", 0, 20, 10)

eolica_eta = (eolica_conv/100) * (1 - eolica_aero/100) * (1 - eolica_variab/100)
eolica_util = eolica_potencia * eolica_eta
st.write(f"Eficiencia total eólica: {eolica_eta*100:.2f}%")
st.write(f"Energía útil eólica: {eolica_util:.2f} MW")
st.image("eolica.png", caption="Diagrama de aerogenerador")
