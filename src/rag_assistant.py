"""Assistente RAG simplificado do OrbitaGuard AI.

Em produção, este módulo pode ser conectado a um vetor store como FAISS, ChromaDB
ou a uma API de LLM. Para a POC, a resposta é gerada por templates com base no alerta.
"""
from __future__ import annotations

import pandas as pd

KNOWLEDGE_BASE = {
    "ndvi": "NDVI é um índice usado para estimar vigor de vegetação a partir de bandas espectrais. Quedas relevantes podem indicar perda de vegetação, solo exposto, seca, queimada ou alteração de uso do solo.",
    "score": "O score de risco da POC combina queda de NDVI e regra de classificação para priorizar regiões que exigem validação.",
    "validacao": "O alerta gerado por satélite deve ser validado por fontes complementares, como vistoria local, dados meteorológicos, sensores terrestres ou bases oficiais."
}


def explain_alert(row: pd.Series) -> str:
    variacao = row.get("variacao_ndvi", row["ndvi_atual"] - row["ndvi_anterior"])
    return (
        f"A região {row['regiao']} foi classificada com risco {row['classe']} "
        f"e score {row['score_risco']}/100. O NDVI anterior era {row['ndvi_anterior']:.2f} "
        f"e o NDVI atual é {row['ndvi_atual']:.2f}, com variação de {variacao:.2f}. "
        f"{KNOWLEDGE_BASE['ndvi']} {KNOWLEDGE_BASE['validacao']}"
    )


def answer_question(question: str, alerts: pd.DataFrame) -> str:
    question_lower = question.lower()
    if "maior" in question_lower or "alto" in question_lower or "risco" in question_lower:
        row = alerts.sort_values("score_risco", ascending=False).iloc[0]
        return explain_alert(row)
    if "ndvi" in question_lower:
        return KNOWLEDGE_BASE["ndvi"]
    if "valid" in question_lower or "confirm" in question_lower:
        return KNOWLEDGE_BASE["validacao"]
    return "A POC analisa alertas ambientais por dados orbitais, calcula score de risco e explica os resultados com uma camada de IA Generativa/RAG simplificada."
