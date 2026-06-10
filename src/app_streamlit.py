from __future__ import annotations

from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from rag_assistant import answer_question, explain_alert

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "demo_alerts.csv"
ASSET_PATH = Path(__file__).resolve().parents[1] / "assets" / "arquitetura_orbitaguard.png"

st.set_page_config(page_title="OrbitaGuard AI", layout="wide")
st.title("OrbitaGuard AI")
st.caption("Monitoramento inteligente de riscos ambientais com dados orbitais, visão computacional e IA Generativa")

alerts = pd.read_csv(DATA_PATH)
if "variacao_ndvi" not in alerts.columns:
    alerts["variacao_ndvi"] = alerts["ndvi_atual"] - alerts["ndvi_anterior"]

col1, col2, col3 = st.columns(3)
col1.metric("Regiões monitoradas", len(alerts))
col2.metric("Alertas de alto risco", int((alerts["classe"] == "Alto").sum()))
col3.metric("Maior score", int(alerts["score_risco"].max()))

st.subheader("Mapa de alertas")
st.map(alerts.rename(columns={"lat": "latitude", "lon": "longitude"})[["latitude", "longitude"]])

st.subheader("Tabela de regiões monitoradas")
st.dataframe(alerts, use_container_width=True)

st.subheader("Score de risco por região")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(alerts["regiao"], alerts["score_risco"])
ax.set_ylabel("Score de risco")
ax.set_ylim(0, 100)
ax.tick_params(axis="x", rotation=30)
st.pyplot(fig)

st.subheader("Explicação automática do alerta")
selected = st.selectbox("Selecione uma região", alerts["regiao"].tolist())
row = alerts[alerts["regiao"] == selected].iloc[0]
st.info(explain_alert(row))

st.subheader("Pergunte ao assistente OrbitaGuard")
question = st.text_input("Exemplo: qual região tem maior risco?")
if question:
    st.write(answer_question(question, alerts))

with st.expander("Arquitetura da solução"):
    st.image(str(ASSET_PATH), use_container_width=True)
