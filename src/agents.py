"""Exemplo de desenho multiagente para a POC."""
from __future__ import annotations

from dataclasses import dataclass
import pandas as pd


@dataclass
class AgentResult:
    agent: str
    message: str


class ColetaAgent:
    def run(self) -> AgentResult:
        return AgentResult("ColetaAgent", "Coletou dados orbitais ou dados demonstrativos locais.")


class AnaliseAgent:
    def run(self, df: pd.DataFrame) -> AgentResult:
        high = int((df["classe"] == "Alto").sum())
        return AgentResult("AnaliseAgent", f"Encontrou {high} regiões de alto risco.")


class ComunicacaoAgent:
    def run(self) -> AgentResult:
        return AgentResult("ComunicacaoAgent", "Gerou explicações para dashboard e relatório executivo.")
