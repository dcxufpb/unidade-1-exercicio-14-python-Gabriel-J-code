# coding: utf-8

import cupom
import pytest


def verifica_campo_obrigatorio_objeto(mensagem_esperada, loja):
    with pytest.raises(Exception) as excinfo:
        loja.dados_loja()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)


# Todas as variaveis preenchidas
NOME_LOJA = "Loja 1"
LOGRADOURO = "Log 1"
NUMERO = 10
COMPLEMENTO = "C1"
BAIRRO = "Bai 1"
MUNICIPIO = "Mun 1"
ESTADO = "E1"
CEP = "11111-111"
TELEFONE = "(11) 1111-1111"
OBSERVACAO = "Obs 1"
CNPJ = "11.111.111/1111-11"
INSCRICAO_ESTADUAL = "123456789"

ENDERECO_COMPLETO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_COMPLETA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_LOJA_COMPLETA = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_loja_completa():
    assert (
        LOJA_COMPLETA.dados_loja() == TEXTO_ESPERADO_LOJA_COMPLETA
    )


LOJA_NOME_NULO = cupom.Loja(None, ENDERECO_COMPLETO, TELEFONE, OBSERVACAO,
                            CNPJ, INSCRICAO_ESTADUAL)

LOJA_NOME_VAZIO = cupom.Loja("", ENDERECO_COMPLETO, TELEFONE, OBSERVACAO, CNPJ,
                             INSCRICAO_ESTADUAL)

MENSAGEM_NOME_OBRIGATORIO = "O campo nome da loja é obrigatório"


def test_valida_nome():
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO,
                                      LOJA_NOME_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO,
                                      LOJA_NOME_VAZIO)


ENDERECO_LOGRADOURO_NULO = cupom.Endereco(None, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_LOGRADOURO_NULO = cupom.Loja(NOME_LOJA, ENDERECO_LOGRADOURO_NULO, 
                                  TELEFONE, OBSERVACAO, CNPJ, 
                                  INSCRICAO_ESTADUAL)

ENDERECO_LOGRADOURO_VAZIO = cupom.Endereco("", NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)
LOJA_LOGRADOURO_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_LOGRADOURO_VAZIO,
                                   TELEFONE, OBSERVACAO, CNPJ, 
                                   INSCRICAO_ESTADUAL)

MENSAGEM_LOGRADOURO_OBRIGATORIO = "O campo logradouro do endereço é obrigatório"


def test_valida_logradouro():
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOGRADOURO_OBRIGATORIO,
                                      LOJA_LOGRADOURO_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOGRADOURO_OBRIGATORIO,
                                      LOJA_LOGRADOURO_VAZIO)

ENDERECO_NUMERO_ZERO = cupom.Endereco(LOGRADOURO, 0, COMPLEMENTO, BAIRRO,
                                      MUNICIPIO, ESTADO, CEP)

LOJA_NUMERO_ZERO = cupom.Loja(NOME_LOJA, ENDERECO_NUMERO_ZERO, TELEFONE,
                              OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

ENDERECO_NUMERO_NULO = cupom.Endereco(LOGRADOURO, None, COMPLEMENTO, BAIRRO,
                                      MUNICIPIO, ESTADO, CEP)

LOJA_NUMERO_NULO = cupom.Loja(NOME_LOJA, ENDERECO_NUMERO_NULO, TELEFONE,
                              OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

ENDERECO_NUMERO_VAZIO = cupom.Endereco(LOGRADOURO, "", COMPLEMENTO, BAIRRO,
                                       MUNICIPIO, ESTADO, CEP)

LOJA_NUMERO_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_NUMERO_VAZIO, TELEFONE,
                               OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)


TEXTO_ESPERADO_SEM_NUMERO = """Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_numero():
    assert (LOJA_NUMERO_ZERO.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO)
    assert (LOJA_NUMERO_VAZIO.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO)
    assert (LOJA_NUMERO_NULO.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO)


ENDERECO_COMPLEMENTO_NULO = cupom.Endereco(LOGRADOURO, NUMERO, None, BAIRRO,
                                           MUNICIPIO, ESTADO, CEP)

LOJA_COMPLEMENTO_NULO = cupom.Loja(NOME_LOJA, ENDERECO_COMPLEMENTO_NULO, 
                                   TELEFONE, OBSERVACAO, CNPJ, 
                                   INSCRICAO_ESTADUAL)

ENDERECO_COMPLEMENTO_VAZIO = cupom.Endereco(LOGRADOURO, NUMERO, "", BAIRRO,
                                            MUNICIPIO, ESTADO, CEP)

LOJA_COMPLEMENTO_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_COMPLEMENTO_VAZIO, 
                                    TELEFONE, OBSERVACAO, CNPJ, 
                                    INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_COMPLEMENTO = """Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_complemento():
    assert (LOJA_COMPLEMENTO_NULO.dados_loja()
            == TEXTO_ESPERADO_SEM_COMPLEMENTO)
    assert (LOJA_COMPLEMENTO_VAZIO.dados_loja()
            == TEXTO_ESPERADO_SEM_COMPLEMENTO)


ENDERECO_BAIRRO_NULO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, None,
                                      MUNICIPIO, ESTADO, CEP)

LOJA_BAIRRO_NULO = cupom.Loja(NOME_LOJA, ENDERECO_BAIRRO_NULO, TELEFONE, 
                              OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

ENDERECO_BAIRRO_VAZIO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, "",
                                       MUNICIPIO, ESTADO, CEP)

LOJA_BAIRRO_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_BAIRRO_VAZIO, TELEFONE, 
                               OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_BAIRRO = """Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_bairro():
    assert (LOJA_BAIRRO_NULO.dados_loja()
            == TEXTO_ESPERADO_SEM_BAIRRO)
    assert (LOJA_BAIRRO_VAZIO.dados_loja()
            == TEXTO_ESPERADO_SEM_BAIRRO)


ENDERECO_MUNICIPIO_NULO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, 
                                         BAIRRO, None, ESTADO, CEP)

LOJA_MUNICIPIO_NULO = cupom.Loja(NOME_LOJA, ENDERECO_MUNICIPIO_NULO, TELEFONE,
                                 OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

ENDERECO_MUNICIPIO_VAZIO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, 
                                          BAIRRO, "", ESTADO, CEP)

LOJA_MUNICIPIO_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_MUNICIPIO_VAZIO, 
                                  TELEFONE, OBSERVACAO, CNPJ, 
                                  INSCRICAO_ESTADUAL)

def test_valida_municipio():
    verifica_campo_obrigatorio_objeto(
        "O campo município do endereço é obrigatório", LOJA_MUNICIPIO_NULO)
    verifica_campo_obrigatorio_objeto(
        "O campo município do endereço é obrigatório", LOJA_MUNICIPIO_VAZIO)


ENDERECO_ESTADO_NULO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                      MUNICIPIO, None, CEP)

LOJA_ESTADO_NULO = cupom.Loja(NOME_LOJA, ENDERECO_ESTADO_NULO, TELEFONE,
                              OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

ENDERECO_ESTADO_VAZIO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                       MUNICIPIO, "", CEP)

LOJA_ESTADO_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_ESTADO_NULO, TELEFONE,
                               OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)


def test_valida_estado():
    verifica_campo_obrigatorio_objeto(
        "O campo estado do endereço é obrigatório", LOJA_ESTADO_NULO)
    verifica_campo_obrigatorio_objeto(
        "O campo estado do endereço é obrigatório", LOJA_ESTADO_NULO)


ENDERECO_CEP_NULO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, None)

LOJA_CEP_NULO = cupom.Loja(NOME_LOJA, ENDERECO_CEP_NULO, TELEFONE, OBSERVACAO,
                           CNPJ, INSCRICAO_ESTADUAL)

ENDERECO_CEP_VAZIO = cupom.Endereco(LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, "")

LOJA_CEP_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_CEP_VAZIO, TELEFONE,
                            OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_CEP = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_cep():
    assert LOJA_CEP_NULO.dados_loja() == TEXTO_ESPERADO_SEM_CEP
    assert LOJA_CEP_VAZIO.dados_loja() == TEXTO_ESPERADO_SEM_CEP


LOJA_TELEFONE_NULO = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, None, OBSERVACAO,
                                CNPJ, INSCRICAO_ESTADUAL)
LOJA_TELEFONE_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, "", OBSERVACAO,
                                CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_TELEFONE = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_telefone():
    assert LOJA_TELEFONE_NULO.dados_loja() == TEXTO_ESPERADO_SEM_TELEFONE
    assert LOJA_TELEFONE_VAZIO.dados_loja() == TEXTO_ESPERADO_SEM_TELEFONE


LOJA_OBSERVACAO_NULA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, None,
                                  CNPJ, INSCRICAO_ESTADUAL)
LOJA_OBSERVACAO_VAZIA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE, "", 
                                   CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_OBSERVACAO = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_observacao():
    assert LOJA_OBSERVACAO_NULA.dados_loja() == TEXTO_ESPERADO_SEM_OBSERVACAO
    assert LOJA_OBSERVACAO_VAZIA.dados_loja() == TEXTO_ESPERADO_SEM_OBSERVACAO


LOJA_CNPJ_NULO = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE,
                            OBSERVACAO, None, INSCRICAO_ESTADUAL)
LOJA_CNPJ_VAZIO = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE,
                             OBSERVACAO, "", INSCRICAO_ESTADUAL)


def test_valida_cnpj():
    verifica_campo_obrigatorio_objeto(
        "O campo CNPJ da loja é obrigatório", LOJA_CNPJ_VAZIO)
    verifica_campo_obrigatorio_objeto(
        "O campo CNPJ da loja é obrigatório", LOJA_CNPJ_NULO)


LOJA_IE_NULA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE,
                          OBSERVACAO, CNPJ, None)
LOJA_IE_VAZIA = cupom.Loja(NOME_LOJA, ENDERECO_COMPLETO, TELEFONE,
                           OBSERVACAO, CNPJ, "")


def test_valida_inscricao_estadual():
    verifica_campo_obrigatorio_objeto(
        "O campo inscrição estadual da loja é obrigatório", LOJA_IE_NULA)
    verifica_campo_obrigatorio_objeto(
        "O campo inscrição estadual da loja é obrigatório", LOJA_IE_VAZIA)

ENDERECO_SEM_NUMERO_SEM_COMPLEMENTO = cupom.Endereco(LOGRADOURO, 0, None, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP)

LOJA_SEM_NUMERO_SEM_COMPLEMENTO = cupom.Loja(NOME_LOJA, ENDERECO_SEM_NUMERO_SEM_COMPLEMENTO,
                                             TELEFONE, OBSERVACAO, CNPJ,
                                             INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO = '''Loja 1
Log 1, s/n
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''


def test_valida_numero_e_complemento():
    assert LOJA_SEM_NUMERO_SEM_COMPLEMENTO.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO


ENDERECO_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO = cupom.Endereco(LOGRADOURO, 0, None, None,
                                   MUNICIPIO, ESTADO, CEP)
LOJA_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO = cupom.Loja(NOME_LOJA, 
                                                        ENDERECO_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO, 
                                                        TELEFONE, OBSERVACAO,
                                                        CNPJ, 
                                                        INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO = '''Loja 1
Log 1, s/n
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''


def test_valida_numero_complemento_e_bairro():
    assert LOJA_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO


def test_exercicio2_customizado():

    # Defina seus próprios valores para as variáveis a seguir
    nome_loja = ""
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    municipio = ""
    estado = ""
    cep = ""
    telefone = ""
    observacao = ""
    cnpj = ""
    inscricao_estadual = ""

    endereco_customizado = cupom.Endereco(logradouro, numero, complemento,
                                 bairro, municipio, estado, cep)
    loja_customizada = cupom.Loja(nome_loja, endereco_customizado, telefone,
                                 observacao, cnpj, inscricao_estadual)

    # E atualize o texto esperado abaixo
    assert (loja_customizada.dados_loja() == """
""")
