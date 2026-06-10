"""Pipeline demonstrativo do OrbitaGuard AI.

A versão local usa dados simulados para garantir que o MVP funcione sem chave de API.
Na evolução, este módulo deve consultar Sentinel Hub, Copernicus Data Space, NASA Earthdata
ou datasets Sentinel-2 no AWS Open Data.
"""
from __future__ import annotations

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "demo_alerts.csv"


def classify_risk(row: pd.Series) -> str:
    """Classifica o risco a partir do score calculado."""
    score = row["score_risco"]
    if score >= 70:
        return "Alto"
    if score >= 40:
        return "Médio"
    return "Baixo"


def calculate_score(ndvi_atual: float, ndvi_anterior: float) -> int:
    """Calcula score de risco com base na queda de NDVI.

    Quanto maior a queda de NDVI, maior o possível impacto em vegetação.
    A fórmula é simples porque o objetivo da POC é demonstrar o fluxo completo.
    """
    queda = max(0.0, ndvi_anterior - ndvi_atual)
    score = min(100, int(queda * 180 + 20))
    return score


def run_pipeline() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["variacao_ndvi"] = df["ndvi_atual"] - df["ndvi_anterior"]
    df["score_risco"] = [calculate_score(a, b) for a, b in zip(df["ndvi_atual"], df["ndvi_anterior"])]
    df["classe"] = df.apply(classify_risk, axis=1)
    df.to_csv(DATA_PATH, index=False)
    return df


if __name__ == "__main__":
    result = run_pipeline()
    print(result.to_string(index=False))
