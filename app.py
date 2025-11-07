import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Cálculo de Detracción", page_icon="💰", layout="centered")

# --- Encabezado ---
st.markdown("""
<h1 style='text-align: center; color: #2E86C1;'>💰 Cálculo de Detracción y Depósito</h1>
<p style='text-align: center; color: gray; font-size: 18px;'>
Simula el cálculo del monto total, detracción y monto a depositar según el IGV y el porcentaje que elijas.
</p>
""", unsafe_allow_html=True)

# --- Entradas del usuario ---
st.markdown("### 🧾 Ingrese los datos:")
col1, col2 = st.columns(2)

with col1:
    monto_usuario = st.number_input("Monto del usuario (S/):", min_value=0.0, format="%.2f")

with col2:
    porcentaje_detraccion = st.number_input("Porcentaje de detracción (%):", min_value=0.0, max_value=100.0, format="%.2f")

# --- Cálculos ---
if st.button("Calcular 💡"):
    if monto_usuario <= 0:
        st.error("⚠️ Ingrese un monto válido mayor que 0.")
    else:
        monto2 = monto_usuario + (monto_usuario * 0.18)
        igv = monto2 - monto_usuario
        monto_detraccion = monto2 * (porcentaje_detraccion / 100)
        monto_deposito = monto2 - monto_detraccion

        # --- Mostrar resultados dentro de una tarjeta ---
        st.markdown("""
        <hr>
        <h3 style='text-align:center; color:#1F618D;'>📊 Resultados del Cálculo</h3>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='background-color:#F8F9F9; border-radius:12px; padding:20px; box-shadow: 0px 0px 10px #D5D8DC;'>
            <p style='font-size:18px; color:#2E4053;'>💵 <b>Monto con IGV (18%)</b>: S/ {monto2:.2f}</p>
            <p style='font-size:18px; color:#2E4053;'>🧮 <b>IGV</b>: S/ {igv:.2f}</p>
            <p style='font-size:18px; color:#2E4053;'>🏦 <b>Detracción ({porcentaje_detraccion}%)</b>: S/ {monto_detraccion:.2f}</p>
            <p style='font-size:18px; color:#2E4053;'>💳 <b>Monto a Depositar</b>: S/ {monto_deposito:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

        st.success("✅ Cálculo realizado correctamente.")
else:
    st.info("Ingrese los datos y presione **Calcular 💡** para ver los resultados.")

# --- Pie de página ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Desarrollado por <b>Frank Montero</b> ⚙️</p>", unsafe_allow_html=True)
