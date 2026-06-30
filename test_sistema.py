"""
Testes Automatizados para o Sistema de Reserva de Salas de Estudo

Este módulo contém os testes unitários para o sistema de reserva de salas.
Utiliza pytest para execução e cobertura de código.
"""

import pytest
import sistema


def setup_function():
    """
    Função de setup que é executada antes de cada teste.
    
    Limpa todos os dados do sistema para garantir que cada teste
    seja executado em um estado limpo e independente.
    """
    sistema.limpar_dados()


# Teste 1: Cadastro de Aluno
def test_cadastrar_aluno():
    """
    Testa o cadastro de um novo aluno no sistema.
    
    Verifica se um aluno pode ser cadastrado com sucesso e se a função
    retorna True quando o cadastro é bem-sucedido.
    """
    resultado = sistema.cadastrar_aluno("João Silva")
    assert resultado is True
    assert "João Silva" in sistema.alunos


# Teste 2: Cadastro de Aluno Duplicado
def test_cadastrar_aluno_duplicado():
    """
    Testa a tentativa de cadastro de um aluno com nome já existente.
    
    Verifica se o sistema impede o cadastro duplicado retornando False
    e se a lista de alunos não é alterada.
    """
    sistema.cadastrar_aluno("Maria Santos")
    resultado = sistema.cadastrar_aluno("Maria Santos")
    assert resultado is False
    assert sistema.alunos.count("Maria Santos") == 1


# Teste 3: Consulta de Salas
def test_consultar_salas():
    """
    Testa a consulta das salas disponíveis no sistema.
    
    Verifica se o sistema retorna todas as três salas esperadas
    (Sala 1, Sala 2 e Sala 3).
    """
    salas = sistema.consultar_salas()
    assert salas == ["Sala 1", "Sala 2", "Sala 3"]
    assert len(salas) == 3


# Teste 4: Reserva Realizada com Sucesso
def test_realizar_reserva_sucesso():
    """
    Testa a realização bem-sucedida de uma reserva de sala.
    
    Verifica se:
    - Um aluno cadastrado pode fazer uma reserva
    - A função retorna True indicando sucesso
    - A reserva é adicionada ao histórico
    """
    # Primeiro, cadastra um aluno
    sistema.cadastrar_aluno("Pedro Costa")
    
    # Realiza uma reserva
    resultado = sistema.realizar_reserva("Pedro Costa", "Sala 1", "14:00")
    assert resultado is True
    
    # Verifica se a reserva foi registrada
    reservas = sistema.consultar_historico()
    assert len(reservas) == 1
    assert reservas[0]["aluno"] == "Pedro Costa"
    assert reservas[0]["sala"] == "Sala 1"
    assert reservas[0]["horario"] == "14:00"


# Teste 5: Bloqueio de Reserva Duplicada
def test_bloqueio_reserva_duplicada():
    """
    Testa o bloqueio de reserva duplicada no mesmo horário e sala.
    
    Verifica se:
    - Uma segunda tentativa de reserva da mesma sala no mesmo horário
      é bloqueada (retorna False)
    - Apenas uma reserva é mantida no histórico
    - Alunos diferentes não podem reservar a mesma sala no mesmo horário
    """
    # Cadastra dois alunos
    sistema.cadastrar_aluno("Ana Silva")
    sistema.cadastrar_aluno("Bruno Costa")
    
    # Ana faz a primeira reserva
    resultado1 = sistema.realizar_reserva("Ana Silva", "Sala 2", "15:00")
    assert resultado1 is True
    
    # Bruno tenta fazer uma reserva no mesmo horário e sala
    resultado2 = sistema.realizar_reserva("Bruno Costa", "Sala 2", "15:00")
    assert resultado2 is False
    
    # Verifica que apenas uma reserva foi registrada
    reservas = sistema.consultar_historico()
    assert len(reservas) == 1
    assert reservas[0]["aluno"] == "Ana Silva"


# Teste 6: Consulta do Histórico de Reservas
def test_consultar_historico():
    """
    Testa a consulta do histórico completo de reservas realizadas.
    
    Verifica se:
    - O histórico retorna todas as reservas realizadas
    - O histórico está vazio quando nenhuma reserva foi feita
    - Múltiplas reservas são corretamente listadas
    """
    # Verifica se o histórico começa vazio
    assert sistema.consultar_historico() == []
    
    # Cadastra alunos e faz reservas
    sistema.cadastrar_aluno("Carlos Silva")
    sistema.cadastrar_aluno("Lucia Santos")
    
    sistema.realizar_reserva("Carlos Silva", "Sala 1", "10:00")
    sistema.realizar_reserva("Lucia Santos", "Sala 2", "11:00")
    sistema.realizar_reserva("Carlos Silva", "Sala 3", "12:00")
    
    # Consulta o histórico
    historico = sistema.consultar_historico()
    assert len(historico) == 3
    
    # Verifica se as reservas estão corretas
    assert historico[0]["aluno"] == "Carlos Silva"
    assert historico[1]["aluno"] == "Lucia Santos"
    assert historico[2]["sala"] == "Sala 3"


# Teste 7: Tentativa de Reserva com Aluno Não Cadastrado
def test_reserva_aluno_nao_cadastrado():
    """
    Testa a tentativa de fazer uma reserva com um aluno não cadastrado.
    
    Verifica se o sistema levanta um erro (ValueError) quando tenta-se
    realizar uma reserva com um aluno que não está cadastrado no sistema.
    """
    with pytest.raises(ValueError, match="não está cadastrado"):
        sistema.realizar_reserva("Desconhecido", "Sala 1", "14:00")


# Teste 8: Tentativa de Reserva com Sala Inexistente
def test_reserva_sala_inexistente():
    """
    Testa a tentativa de fazer uma reserva em uma sala que não existe.
    
    Verifica se o sistema levanta um erro (ValueError) quando tenta-se
    realizar uma reserva em uma sala que não está no sistema.
    """
    sistema.cadastrar_aluno("Fernando Silva")
    
    with pytest.raises(ValueError, match="não existe"):
        sistema.realizar_reserva("Fernando Silva", "Sala 999", "14:00")


# Teste 9: Validação de Entrada - Nome Vazio
def test_cadastrar_aluno_nome_vazio():
    """
    Testa a validação de entrada ao tentar cadastrar um aluno com nome vazio.
    
    Verifica se o sistema levanta um erro (ValueError) quando tenta-se
    cadastrar um aluno com nome vazio ou inválido.
    """
    with pytest.raises(ValueError, match="Nome deve ser"):
        sistema.cadastrar_aluno("")


# Teste 10: Reservas Independentes por Horário
# Teste 10: Validacao de Entrada - Nome Apenas com Espacos
def test_cadastrar_aluno_nome_apenas_espacos():
    """
    Testa a validação de entrada ao tentar cadastrar um aluno com nome
    formado apenas por espaços.
    """
    with pytest.raises(ValueError, match="Nome deve ser"):
        sistema.cadastrar_aluno("   ")


# Teste 11: Validacao de Entrada - Tipo Invalido
def test_cadastrar_aluno_nome_tipo_invalido():
    """
    Testa a validação de entrada ao tentar cadastrar aluno com tipo inválido.
    """
    with pytest.raises(ValueError, match="Nome deve ser"):
        sistema.cadastrar_aluno(None)


# Teste 12: Validacao de Entrada - Horario Invalido
def test_realizar_reserva_horario_invalido():
    """
    Testa a validação de entrada ao tentar realizar uma reserva sem horário.
    """
    sistema.cadastrar_aluno("Isabela Rocha")

    with pytest.raises(ValueError, match="Hor"):
        sistema.realizar_reserva("Isabela Rocha", "Sala 1", "")


# Teste 13: Reservas Independentes por Horario
def test_reservas_diferentes_horarios():
    """
    Testa a realização de múltiplas reservas da mesma sala em horários diferentes.
    
    Verifica se:
    - A mesma sala pode ser reservada em horários diferentes
    - Não há conflito entre reservas em horários diferentes
    """
    sistema.cadastrar_aluno("Gabriel Lima")
    sistema.cadastrar_aluno("Helena Rocha")
    
    # Gabriel reserva Sala 1 às 10:00
    resultado1 = sistema.realizar_reserva("Gabriel Lima", "Sala 1", "10:00")
    assert resultado1 is True
    
    # Helena reserva Sala 1 às 11:00 (horário diferente)
    resultado2 = sistema.realizar_reserva("Helena Rocha", "Sala 1", "11:00")
    assert resultado2 is True
    
    # Verifica que ambas as reservas foram registradas
    historico = sistema.consultar_historico()
    assert len(historico) == 2
