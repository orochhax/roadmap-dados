"""Testes-exercício do ciclo de vida do modelo."""

import pytest


@pytest.mark.skip(reason="Exercício: testar limites pré-declarados de drift.")
def test_monitoramento_aplica_limites_congelados():
    assert False


@pytest.mark.skip(reason="Exercício: registrar decisão champion/challenger.")
def test_promocao_ou_retencao_e_auditavel():
    assert False


@pytest.mark.skip(reason="Exercício: restaurar artefato anterior.")
def test_rollback_restaura_versao_sem_apagar_historico():
    assert False

