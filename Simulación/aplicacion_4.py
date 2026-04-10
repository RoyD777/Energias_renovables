import streamlit as st
import matplotlib.pyplot as plt

st.title("Comparador de energías renovables")

# Descripción del problema
st.markdown("""
### Descripción del problema
Se requiere abastecer una comunidad con energía renovable. 
El usuario puede ajustar parámetros de hidroeléctrica, solar y eólica 
para comparar la potencia útil de cada una y la potencia total combinada.
""")

# --- Hidroeléctrica ---
st.header("Hidroeléctrica")
st.image("hidro.png", caption="Represa hidroeléctrica", use_container_width=False, width=300)
pot_hidro = st.slider("Potencia instalada (MW)", 0, 100, 80, step=1, key="ph")
ef_hidro = st.slider("Eficiencia de conversión (%)", 10, 100, 90, key="eh")
turb = st.slider("Pérdidas por turbulencia (%)", 0, 20, 5, key="th")
transp = st.slider("Pérdidas por transporte de agua (%)", 0, 20, 5, key="trh")
eta_hidro = (ef_hidro/100) * (1 - turb/100) * (1 - transp/100)
energia_hidro = pot_hidro * eta_hidro

# --- Solar ---
st.header("Solar")
st.image("solar.png", caption="Panel solar con inversor", use_container_width=False, width=300)
pot_solar = st.slider("Potencia instalada (MW)", 0, 100, 30, step=1, key="ps")
ef_solar = st.slider("Eficiencia de conversión (%)", 10, 25, 18, key="es")
temp = st.slider("Pérdidas por temperatura (%)", 0, 20, 10, key="ts")
inv = st.slider("Pérdidas por conversión DC/AC (%)", 0, 20, 5, key="ivs")
eta_solar = (ef_solar/100) * (1 - temp/100) * (1 - inv/100)
energia_solar = pot_solar * eta_solar

# --- Eólica ---
st.header("Eólica")
st.image("eolica.png", caption="Aerogenerador", use_container_width=False, width=300)
pot_eolica = st.slider("Potencia instalada (MW)", 0, 100, 40, step=1, key="pe")
ef_eolica = st.slider("Eficiencia de conversión (%)", 30, 50, 40, key="ee")
aero = st.slider("Pérdidas aerodinámicas (%)", 0, 20, 8, key="ae")
variab = st.slider("Pérdidas por variabilidad del viento (%)", 0, 20, 10, key="ve")
eta_eolica = (ef_eolica/100) * (1 - aero/100) * (1 - variab/100)
energia_eolica = pot_eolica * eta_eolica

# --- Comparación ---
st.subheader("Resultados")
st.write(f"Potencia útil Hidroeléctrica: {energia_hidro:.2f} MW")
st.write(f"Potencia útil Solar: {energia_solar:.2f} MW")
st.write(f"Potencia útil Eólica: {energia_eolica:.2f} MW")
st.write(f"**Potencia total combinada: {energia_hidro + energia_solar + energia_eolica:.2f} MW**")

# --- Gráfico comparativo ---
fig, ax = plt.subplots()
labels = ["Hidroeléctrica", "Solar", "Eólica", "Total combinado"]
values = [energia_hidro, energia_solar, energia_eolica, energia_hidro + energia_solar + energia_eolica]

ax.bar(labels, values, color=["blue", "blue", "blue", "green"])
ax.set_ylabel("Potencia útil (MW)")
ax.set_title("Comparación de potencia útil")

# Etiquetas encima de cada barra
for i, v in enumerate(values):
    ax.text(i, v + 0.5, f"{v:.2f}", ha='center')

st.pyplot(fig)
