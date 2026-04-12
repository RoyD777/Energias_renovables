import streamlit as st

st.title("Simulador de pérdidas técnicas en renovables")

# Selección de fuente
fuente = st.selectbox("Selecciona la fuente de energía:", 
                      ["Hidroeléctrica", "Solar", "Eólica"])

# Imagen arriba
if fuente == "Hidroeléctrica":
    st.image("hidro.png", caption="Represa hidroeléctrica", use_container_width=False, width=400)
elif fuente == "Solar":
    st.image("solar.png", caption="Panel solar con inversor", use_container_width=False, width=400)
else:
    st.image("eolica.png", caption="Aerogenerador", use_container_width=False, width=400)

# Parámetros comunes
potencia = st.slider("Potencia instalada (MW)", 0.0, 100.0, 50.0)
eficiencia_conv = st.slider("Eficiencia de conversión (%)", 10, 100, 90)

# Ajuste de pérdidas según fuente
if fuente == "Hidroeléctrica":
    turbulencia = st.slider("Pérdidas por turbulencia (%)", 0, 20, 5)
    transporte = st.slider("Pérdidas por transporte de agua (%)", 0, 20, 5)
    eta_base = (eficiencia_conv/100) * (1 - turbulencia/100) * (1 - transporte/100)

elif fuente == "Solar":
    temperatura = st.slider("Pérdidas por temperatura (%)", 0, 20, 10)
    inversor = st.slider("Pérdidas por conversión DC/AC (%)", 0, 20, 5)
    eta_base = (eficiencia_conv/100) * (1 - temperatura/100) * (1 - inversor/100)

else:  # Eólica
    aerodinamicas = st.slider("Pérdidas aerodinámicas (%)", 0, 20, 8)
    variabilidad = st.slider("Pérdidas por variabilidad del viento (%)", 0, 20, 10)
    eta_base = (eficiencia_conv/100) * (1 - aerodinamicas/100) * (1 - variabilidad/100)

# --- Sección de transmisión (última) ---
st.header("Transmisión eléctrica")
st.write("(Estimando 0.01% de pérdida por kilómetro)")
distancia = st.slider("Distancia de transmisión (km)", 0, 500, 100)
coef_perdida = 0.0001  # 0.01% por km
perdida_transmision = distancia * coef_perdida
st.write(f"Pérdida por transmisión: {perdida_transmision*100:.2f}%")

# Aplicar transmisión como último factor
eta_total = eta_base * (1 - perdida_transmision)
energia_util = potencia * eta_total

# Resultados
st.subheader("Resultados finales")
st.write(f"Eficiencia total: {eta_total*100:.2f}%")
st.write(f"Energía útil: {energia_util:.2f} MW")
