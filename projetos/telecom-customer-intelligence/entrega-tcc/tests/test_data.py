"""Testes-exercício da fase de dados."""

import pytest


@pytest.mark.skip(reason="Exercício: validar schema e marcação sintética.")
def test_piloto_declara_origem_sintetica_em_todas_as_linhas():
    assert False


@pytest.mark.skip(reason="Exercício: provar determinismo do gerador.")
def test_mesma_seed_reproduz_o_mesmo_piloto():
    assert False


@pytest.mark.skip(reason="Exercício: impedir vazamento temporal.")
def test_features_estavam_disponiveis_na_data_de_decisao():
    assert False


@pytest.mark.skip(reason="Exercício: preservar janela de monitoramento.")
def test_splits_temporais_nao_se_sobrepoem_indevidamente():
    assert False

