import streamlit as st

st.title("Simulador de pérdidas técnicas en renovables")

# Selección de fuente
fuente = st.selectbox("Selecciona la fuente de energía:", 
                      ["Hidroeléctrica", "Solar", "Eólica"])

# Mostrar imagen arriba (tamaño reducido)
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
    eta_total = (eficiencia_conv/100) * (1 - turbulencia/100) * (1 - transporte/100)

elif fuente == "Solar":
    temperatura = st.slider("Pérdidas por temperatura (%)", 0, 20, 10)
    inversor = st.slider("Pérdidas por conversión DC/AC (%)", 0, 20, 5)
    eta_total = (eficiencia_conv/100) * (1 - temperatura/100) * (1 - inversor/100)

else:  # Eólica
    aerodinamicas = st.slider("Pérdidas aerodinámicas (%)", 0, 20, 8)
    variabilidad = st.slider("Pérdidas por variabilidad del viento (%)", 0, 20, 10)
    eta_total = (eficiencia_conv/100) * (1 - aerodinamicas/100) * (1 - variabilidad/100)

# Cálculo de energía útil
energia_util = potencia * eta_total

# Resultados
st.subheader("Resultados")
st.write(f"Eficiencia total: {eta_total*100:.2f}%")
st.write(f"Energía útil: {energia_util:.2f} MW")
