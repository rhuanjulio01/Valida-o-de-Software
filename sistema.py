alunos = []  # Lista de nomes de alunos cadastrados
reservas = []  # Lista de reservas realizadas
salas_disponiveis = ["Sala 1", "Sala 2", "Sala 3"]  # Salas disponíveis no sistema


def cadastrar_aluno(nome):
    """
    Cadastra um novo aluno no sistema.
    
    """
    if not isinstance(nome, str):
        raise ValueError("Nome deve ser uma string não vazia")
    
    nome = nome.strip()
    
    if not nome:
        raise ValueError("Nome deve ser uma string nao vazia")
    
    if nome in alunos:
        return False
    
    alunos.append(nome) 
    return True


def consultar_salas():
    """
    Consulta todas as salas disponíveis no sistema.
    
    Returns:
        list: Lista de nomes das salas disponíveis
    """
    return salas_disponiveis.copy()


def realizar_reserva(aluno, sala, horario):
    """
    Realiza uma reserva de sala para um aluno em um horário específico.
    
    Impede que a mesma sala seja reservada para o mesmo horário por diferentes alunos.
    
    Args:
        aluno (str): Nome do aluno que faz a reserva
        sala (str): Nome da sala a ser reservada
        horario (str): Horário da reserva (formato: "HH:MM")
        
    Returns:
        bool: True se reserva realizada com sucesso, False caso contrário
        
    Raises:
        ValueError: Se aluno não está cadastrado, sala não existe ou horário é inválido
    """
    # Validações
    if aluno not in alunos:
        raise ValueError(f"Aluno '{aluno}' não está cadastrado")
    
    if sala not in salas_disponiveis:
        raise ValueError(f"Sala '{sala}' não existe no sistema")
       
    if not horario or not isinstance(horario, str):
        raise ValueError("Horário deve ser uma string válida")
    
    # Verifica se já existe uma reserva para a mesma sala no mesmo horário
    for reserva in reservas:
        if reserva["sala"] == sala and reserva["horario"] == horario:
            return False
    
    # Cria e adiciona a nova reserva
    nova_reserva = {
        "aluno": aluno,
        "sala": sala,
        "horario": horario
    }
    reservas.append(nova_reserva)
    return True


def consultar_historico():
    """
    Consulta o histórico completo de reservas realizadas.
    
    Returns:
        list: Lista de todas as reservas realizadas (dicionários com aluno, sala e horario)
    """
    return reservas.copy()


def cancelar_reserva(aluno, sala, horario):
    """
    Cancela uma reserva existente.
    
    Args:
        aluno (str): Nome do aluno que fez a reserva
        sala (str): Nome da sala reservada
        horario (str): Horario da reserva
        
    Returns:
        bool: True se a reserva foi cancelada, False se nao foi encontrada
    """
    for reserva in reservas:
        if (
            reserva["aluno"] == aluno
            and reserva["sala"] == sala
            and reserva["horario"] == horario
        ):
            reservas.remove(reserva)
            return True

    return False


def limpar_dados():
    """
    Limpa todos os dados do sistema (utilitário para testes).
    
    Esta função é usada principalmente nos testes para resetar o sistema
    antes de cada caso de teste.
    """
    global alunos, reservas
    alunos.clear()
    reservas.clear()
