"""Testes-exercício da fase de modelos."""

import pytest


@pytest.mark.skip(reason="Exercício: garantir treino apenas no período permitido.")
def test_modelos_nao_acessam_teste_ou_monitoramento():
    assert False


@pytest.mark.skip(reason="Exercício: validar probabilidades e chaves.")
def test_scores_de_risco_possuem_contrato_valido():
    assert False


@pytest.mark.skip(reason="Exercício: impedir desfecho futuro nas features.")
def test_estimador_incremental_nao_recebe_contrafactual_ou_desfecho_futuro():
    assert False

