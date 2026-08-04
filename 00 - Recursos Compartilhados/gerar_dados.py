"""Gera o kit de dados sintéticos usado pelos exercícios do roadmap.

O script prepara somente dados de entrada. Ele não calcula métricas, não treina
modelos e não contém respostas dos exercícios. Toda geração é determinística
com seed 42 para que os resultados possam ser reproduzidos.
"""

from __future__ import annotations

import csv
import math
import random
from datetime import date, datetime, timedelta
from pathlib import Path


SEED = 42
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dados"
DOCS_DIR = ROOT / "documentos_suporte"

CIDADES = [
    "Salvador",
    "Feira de Santana",
    "Vitória da Conquista",
    "Eunápolis",
    "Ilhéus",
]


def escrever_csv(nome: str, campos: list[str], linhas: list[dict]) -> None:
    caminho = DATA_DIR / nome
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8-sig", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas)


def limitar(valor: float, minimo: float, maximo: float) -> float:
    return max(minimo, min(maximo, valor))


def gerar_incidentes(rng: random.Random) -> None:
    causas = [
        "rompimento de fibra",
        "queda de energia",
        "falha de equipamento",
        "erro de configuração",
        "manutenção programada",
    ]
    severidades = ["P1", "P2", "P3", "P4"]
    pesos = [0.08, 0.24, 0.43, 0.25]
    duracoes_limite = [50, 51, 100, 101, 120, 121, 180, 181]
    linhas = []

    inicio = datetime(2026, 1, 2, 7, 30)
    for indice in range(1, 241):
        severidade = rng.choices(severidades, weights=pesos, k=1)[0]
        if indice <= len(duracoes_limite):
            duracao = duracoes_limite[indice - 1]
        else:
            faixas = {
                "P1": (90, 420),
                "P2": (45, 260),
                "P3": (20, 180),
                "P4": (5, 90),
            }
            duracao = rng.randint(*faixas[severidade])

        abertura = inicio + timedelta(
            days=rng.randint(0, 240), minutes=rng.randint(0, 900)
        )
        resolvido = rng.random() < 0.86
        fechamento = abertura + timedelta(minutes=duracao) if resolvido else None
        multiplicador = {"P1": 8, "P2": 4, "P3": 2, "P4": 1}[severidade]
        clientes = rng.randint(5, 90) * multiplicador

        linhas.append(
            {
                "id": f"INC-{indice:04d}",
                "cidade": rng.choice(CIDADES),
                "causa": rng.choice(causas),
                "severidade": severidade,
                "duracao_min": duracao,
                "clientes_afetados": clientes,
                "resolvido": str(resolvido).lower(),
                "data_abertura": abertura.isoformat(timespec="minutes"),
                "data_fechamento": (
                    fechamento.isoformat(timespec="minutes") if fechamento else ""
                ),
                "observacao": "" if indice % 17 == 0 else "registro operacional",
            }
        )

    escrever_csv(
        "incidentes.csv",
        [
            "id",
            "cidade",
            "causa",
            "severidade",
            "duracao_min",
            "clientes_afetados",
            "resolvido",
            "data_abertura",
            "data_fechamento",
            "observacao",
        ],
        linhas,
    )

    metas = [
        {"cidade": "Salvador", "meta_duracao_min": 90, "meta_resolucao_pct": 88},
        {
            "cidade": "Feira de Santana",
            "meta_duracao_min": 105,
            "meta_resolucao_pct": 86,
        },
        {
            "cidade": "Vitória da Conquista",
            "meta_duracao_min": 110,
            "meta_resolucao_pct": 85,
        },
        {"cidade": "Eunápolis", "meta_duracao_min": 120, "meta_resolucao_pct": 84},
        {"cidade": "Porto Seguro", "meta_duracao_min": 115, "meta_resolucao_pct": 85},
    ]
    escrever_csv(
        "metas_cidades.csv",
        ["cidade", "meta_duracao_min", "meta_resolucao_pct"],
        metas,
    )


def gerar_telecom_e_relacional(rng: random.Random) -> None:
    planos = [
        {"plano_id": "PL01", "nome_plano": "Básico 100", "velocidade_mbps": 100, "mensalidade_base": 79.90},
        {"plano_id": "PL02", "nome_plano": "Casa 300", "velocidade_mbps": 300, "mensalidade_base": 109.90},
        {"plano_id": "PL03", "nome_plano": "Família 500", "velocidade_mbps": 500, "mensalidade_base": 149.90},
        {"plano_id": "PL04", "nome_plano": "Gamer 700", "velocidade_mbps": 700, "mensalidade_base": 199.90},
        {"plano_id": "PL05", "nome_plano": "Empresa 1000", "velocidade_mbps": 1000, "mensalidade_base": 299.90},
        {"plano_id": "PL06", "nome_plano": "Sem clientes", "velocidade_mbps": 50, "mensalidade_base": 59.90},
    ]
    escrever_csv(
        "planos.csv",
        ["plano_id", "nome_plano", "velocidade_mbps", "mensalidade_base"],
        planos,
    )

    canais = ["loja", "site", "indicação", "telefone"]
    clientes = []
    telecom = []
    chamados = []
    pagamentos = []
    referencia = date(2026, 8, 1)

    for indice in range(1, 601):
        plano = rng.choice(planos[:5])
        ativacao = referencia - timedelta(days=rng.randint(30, 1500))
        tempo_meses = max(1, (referencia - ativacao).days // 30)
        cidade = rng.choice(CIDADES)
        canal = rng.choice(canais)
        mensalidade = round(float(plano["mensalidade_base"]) * rng.uniform(0.92, 1.12), 2)
        chamados_90d = max(0, int(rng.gauss(2.2, 1.9)))
        atraso_dias = rng.choices([0, 5, 10, 20, 35, 60], [58, 12, 10, 9, 7, 4], k=1)[0]
        nps = int(limitar(round(rng.gauss(7.0 - chamados_90d * 0.45, 2.2)), 0, 10))

        risco = (
            -2.9
            + chamados_90d * 0.34
            + atraso_dias * 0.025
            + (6 - nps) * 0.23
            - min(tempo_meses, 36) * 0.018
        )
        prob_churn = 1 / (1 + math.exp(-risco))
        churn = rng.random() < prob_churn
        cancelamento = referencia - timedelta(days=rng.randint(1, 60)) if churn else None
        motivo = rng.choice(["preço", "instabilidade", "mudança", "atendimento"]) if churn else ""
        cliente_id = f"CLI-{indice:04d}"

        clientes.append(
            {
                "cliente_id": cliente_id,
                "cidade": cidade,
                "plano_id": plano["plano_id"],
                "canal_aquisicao": canal,
                "data_ativacao": ativacao.isoformat(),
                "mensalidade": mensalidade,
            }
        )
        telecom.append(
            {
                "cliente_id": cliente_id,
                "cidade": cidade,
                "plano": plano["nome_plano"],
                "canal_aquisicao": canal,
                "mensalidade": mensalidade,
                "nps": nps,
                "chamados_90d": chamados_90d,
                "atraso_dias": atraso_dias,
                "tempo_cliente_meses": tempo_meses,
                "data_ativacao": ativacao.isoformat(),
                "churn": int(churn),
                "data_cancelamento": cancelamento.isoformat() if cancelamento else "",
                "motivo_cancelamento": motivo,
                "status_atual": "cancelado" if churn else "ativo",
            }
        )

        quantidade_chamados = max(0, int(rng.gauss(4.5, 3.0)))
        for _ in range(quantidade_chamados):
            numero = len(chamados) + 1
            abertura = referencia - timedelta(days=rng.randint(0, 420))
            duracao = rng.randint(5, 240)
            chamados.append(
                {
                    "chamado_id": f"CHA-{numero:05d}",
                    "cliente_id": cliente_id,
                    "data_abertura": abertura.isoformat(),
                    "duracao_min": duracao,
                    "categoria": rng.choice(["conexão", "financeiro", "instalação", "equipamento"]),
                    "resolvido": str(rng.random() < 0.9).lower(),
                }
            )

        for meses_atras in range(0, min(12, tempo_meses)):
            numero = len(pagamentos) + 1
            vencimento = referencia - timedelta(days=30 * meses_atras)
            pago = rng.random() > (0.04 + atraso_dias / 200)
            pagamentos.append(
                {
                    "pagamento_id": f"PAG-{numero:06d}",
                    "cliente_id": cliente_id,
                    "data_vencimento": vencimento.isoformat(),
                    "data_pagamento": (
                        (vencimento + timedelta(days=rng.randint(-3, 18))).isoformat()
                        if pago
                        else ""
                    ),
                    "valor": mensalidade,
                    "status": "pago" if pago else "pendente",
                }
            )

    escrever_csv(
        "clientes.csv",
        ["cliente_id", "cidade", "plano_id", "canal_aquisicao", "data_ativacao", "mensalidade"],
        clientes,
    )
    escrever_csv(
        "clientes_telecom.csv",
        [
            "cliente_id",
            "cidade",
            "plano",
            "canal_aquisicao",
            "mensalidade",
            "nps",
            "chamados_90d",
            "atraso_dias",
            "tempo_cliente_meses",
            "data_ativacao",
            "churn",
            "data_cancelamento",
            "motivo_cancelamento",
            "status_atual",
        ],
        telecom,
    )
    escrever_csv(
        "chamados.csv",
        ["chamado_id", "cliente_id", "data_abertura", "duracao_min", "categoria", "resolvido"],
        chamados,
    )
    escrever_csv(
        "pagamentos.csv",
        ["pagamento_id", "cliente_id", "data_vencimento", "data_pagamento", "valor", "status"],
        pagamentos,
    )


def gerar_pedidos(rng: random.Random) -> None:
    linhas = []
    inicio = date(2025, 1, 1)
    canais = ["site", "app", "loja", "marketplace"]
    categorias = ["eletrônicos", "casa", "livros", "esporte", "beleza"]

    for indice in range(1, 1001):
        data_pedido = inicio + timedelta(days=rng.randint(0, 600))
        quantidade = rng.randint(1, 6)
        preco_unitario = round(rng.uniform(18, 650), 2)
        desconto = rng.choice([0, 0, 0, 5, 10, 15, 20])
        valor = round(quantidade * preco_unitario * (1 - desconto / 100), 2)
        linhas.append(
            {
                "pedido_id": f"PED-{indice:05d}",
                "cliente_id": f"CLI-{rng.randint(1, 600):04d}",
                "data_pedido": data_pedido.isoformat(),
                "canal": rng.choice(canais),
                "categoria": rng.choice(categorias),
                "quantidade": quantidade,
                "preco_unitario": preco_unitario,
                "desconto_pct": desconto,
                "valor_pedido": valor,
            }
        )

    escrever_csv(
        "pedidos.csv",
        [
            "pedido_id",
            "cliente_id",
            "data_pedido",
            "canal",
            "categoria",
            "quantidade",
            "preco_unitario",
            "desconto_pct",
            "valor_pedido",
        ],
        linhas,
    )


def gerar_credito(rng: random.Random) -> None:
    linhas = []
    inicio = date(2023, 1, 1)

    for indice in range(1, 1001):
        renda = round(rng.uniform(1400, 18000), 2)
        divida = round(renda * rng.uniform(0.05, 1.6), 2)
        atrasos_12m = rng.choices([0, 1, 2, 3, 4, 5], [52, 18, 12, 8, 6, 4], k=1)[0]
        emprego_meses = rng.randint(1, 240)
        valor_solicitado = round(rng.uniform(800, 45000), 2)
        taxa = round(rng.uniform(1.1, 5.5), 2)
        concessao = inicio + timedelta(days=rng.randint(0, 1200))
        logit = -3.4 + divida / max(renda, 1) * 1.25 + atrasos_12m * 0.42 - min(emprego_meses, 60) * 0.012
        default = rng.random() < 1 / (1 + math.exp(-logit))

        linhas.append(
            {
                "contrato_id": f"CRD-{indice:05d}",
                "data_concessao": concessao.isoformat(),
                "idade": rng.randint(18, 75),
                "renda_mensal": renda,
                "divida_atual": divida,
                "atrasos_12m": atrasos_12m,
                "tempo_emprego_meses": emprego_meses,
                "valor_solicitado": valor_solicitado,
                "taxa_juros_mensal": taxa,
                "prazo_meses": rng.choice([6, 12, 18, 24, 36, 48]),
                "default_90d": int(default),
            }
        )

    escrever_csv(
        "credito.csv",
        [
            "contrato_id",
            "data_concessao",
            "idade",
            "renda_mensal",
            "divida_atual",
            "atrasos_12m",
            "tempo_emprego_meses",
            "valor_solicitado",
            "taxa_juros_mensal",
            "prazo_meses",
            "default_90d",
        ],
        linhas,
    )


def gerar_energia(rng: random.Random) -> None:
    linhas = []
    inicio = date(2024, 1, 1)
    for indice in range(730):
        dia = inicio + timedelta(days=indice)
        sazonal_semana = 18 if dia.weekday() < 5 else -12
        sazonal_ano = 35 * math.sin(2 * math.pi * indice / 365)
        tendencia = indice * 0.035
        consumo = 520 + sazonal_semana + sazonal_ano + tendencia + rng.gauss(0, 16)
        linhas.append(
            {
                "data": dia.isoformat(),
                "consumo_mwh": round(consumo, 2),
                "temperatura_c": round(26 + 5 * math.sin(2 * math.pi * indice / 365) + rng.gauss(0, 1.8), 1),
                "feriado": int((dia.month, dia.day) in {(1, 1), (9, 7), (12, 25)}),
            }
        )

    escrever_csv(
        "energia.csv",
        ["data", "consumo_mwh", "temperatura_c", "feriado"],
        linhas,
    )


def gerar_documentos_suporte() -> None:
    documentos = [
        ("reinicio-roteador", "Reinício seguro do roteador", "Desligue o roteador da tomada por 30 segundos. Religue, aguarde três minutos e confirme se as luzes de energia e internet ficaram estáveis."),
        ("sem-conexao", "Diagnóstico de ausência de conexão", "Verifique cabos, luz de internet e teste dois dispositivos. Se todos falharem e a luz de internet estiver vermelha, registre chamado de conectividade."),
        ("wifi-lento", "Wi-Fi com baixa velocidade", "Faça o teste próximo ao roteador, pause downloads e compare as redes de 2,4 GHz e 5 GHz. A rede de 5 GHz é indicada para menor distância."),
        ("troca-senha-wifi", "Troca de senha do Wi-Fi", "Acesse o aplicativo do cliente, abra Rede Wi-Fi, escolha Alterar senha e use ao menos 10 caracteres. Os dispositivos precisarão ser reconectados."),
        ("segunda-via", "Segunda via da fatura", "No aplicativo, abra Financeiro, selecione a fatura e escolha Copiar código ou Baixar PDF. Nunca solicite senha bancária ao cliente."),
        ("pagamento-nao-baixado", "Pagamento ainda não reconhecido", "A compensação pode levar até dois dias úteis. Após esse prazo, confirme data, valor e comprovante antes de encaminhar ao financeiro."),
        ("mudanca-endereco", "Mudança de endereço", "Consulte cobertura no novo endereço antes de cancelar a instalação atual. A visita depende de disponibilidade técnica e confirmação do titular."),
        ("equipamento-aquecendo", "Equipamento aquecendo", "Mantenha o roteador em local ventilado, sem objetos sobre ele. Se houver cheiro de queimado, desligue imediatamente e abra chamado de segurança."),
        ("luz-los-vermelha", "Luz LOS vermelha", "Não dobre nem desconecte o cabo óptico. Registre a luz LOS, verifique indisponibilidade na região e encaminhe para suporte de fibra."),
        ("instabilidade-chuva", "Instabilidade durante chuva", "Registre horário e duração das quedas, teste conexão por cabo e verifique alerta regional. Não prometa prazo antes da análise técnica."),
        ("cancelamento", "Solicitação de cancelamento", "Confirme identidade do titular, explique cobranças pendentes e registre o protocolo. Ofertas de retenção devem respeitar consentimento e elegibilidade."),
        ("visita-tecnica", "Preparação para visita técnica", "Deve haver um adulto no local e acesso ao roteador e à entrada do cabo. O reagendamento precisa ocorrer antes da janela confirmada."),
        ("dados-pessoais", "Proteção de dados pessoais", "Nunca registre senha, número completo de cartão ou documento desnecessário. Compartilhe dados somente com perfis autorizados."),
        ("fora-de-escopo", "Solicitações fora do escopo", "O suporte não orienta invasão de redes, desbloqueio ilegal ou acesso a contas de terceiros. Recuse e registre o motivo de segurança."),
        ("escalonamento-p1", "Escalonamento de incidente P1", "Risco de segurança, cidade inteira sem serviço ou serviço crítico com alto impacto exige escalonamento imediato ao coordenador e atualizações periódicas."),
    ]

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    catalogo = []
    for indice, (slug, titulo, conteudo) in enumerate(documentos, start=1):
        nome = f"DOC-{indice:02d}-{slug}.md"
        texto = (
            f"# {titulo}\n\n"
            f"- **Documento:** DOC-{indice:02d}\n"
            "- **Versão:** 1.0\n"
            "- **Licença:** conteúdo sintético para estudo\n\n"
            "## Procedimento\n\n"
            f"{conteudo}\n\n"
            "## Limite de atendimento\n\n"
            "Se o procedimento não resolver ou houver risco, registre o caso e encaminhe para revisão humana.\n"
        )
        (DOCS_DIR / nome).write_text(texto, encoding="utf-8")
        catalogo.append(
            {
                "documento_id": f"DOC-{indice:02d}",
                "arquivo": nome,
                "titulo": titulo,
                "versao": "1.0",
                "licenca": "conteúdo sintético para estudo",
            }
        )

    caminho_catalogo = DOCS_DIR / "catalogo.csv"
    with caminho_catalogo.open("w", encoding="utf-8-sig", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=list(catalogo[0]))
        escritor.writeheader()
        escritor.writerows(catalogo)


def main() -> None:
    rng = random.Random(SEED)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    gerar_incidentes(rng)
    gerar_telecom_e_relacional(rng)
    gerar_pedidos(rng)
    gerar_credito(rng)
    gerar_energia(rng)
    gerar_documentos_suporte()
    print("Kit de dados criado com seed 42.")


if __name__ == "__main__":
    main()
