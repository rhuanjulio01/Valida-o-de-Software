# Sistema de Reserva de Salas de Estudo

Um sistema Python completo para gerenciar reservas de salas de estudo, desenvolvido com modularização e testes automatizados.

## 📋 Descrição

O Sistema de Reserva de Salas de Estudo permite que:
- Alunos sejam cadastrados no sistema
- Salas disponíveis sejam consultadas
- Alunos façam reservas de salas em horários específicos
- O sistema impeça reservas duplicadas (mesma sala, mesmo horário)
- O histórico de reservas seja consultado

## 🏗️ Estrutura do Projeto

```
projeto/
├── sistema.py          # Implementação principal do sistema
├── test_sistema.py     # Testes automatizados com pytest
├── requirements.txt    # Dependências do projeto
└── README.md          # Documentação (este arquivo)
```

## 🚀 Como Instalar

### 1. Clonar ou copiar o projeto

```bash
cd Projeto
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

**No Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**No Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 📖 Como Usar

### Exemplo Básico

```python
import sistema

# Cadastrar alunos
sistema.cadastrar_aluno("João Silva")
sistema.cadastrar_aluno("Maria Santos")

# Consultar salas disponíveis
salas = sistema.consultar_salas()
print(salas)  # ['Sala 1', 'Sala 2', 'Sala 3']

# Realizar reservas
sistema.realizar_reserva("João Silva", "Sala 1", "14:00")
sistema.realizar_reserva("Maria Santos", "Sala 2", "15:00")

# Consultar histórico
historico = sistema.consultar_historico()
print(historico)

# Tentar fazer uma reserva duplicada
resultado = sistema.realizar_reserva("João Silva", "Sala 1", "14:00")
print(resultado)  # False - sala já está reservada neste horário
```

## 🧪 Como Executar os Testes

### Executar todos os testes

```bash
pytest test_sistema.py
```

### Executar testes com saída detalhada

```bash
pytest test_sistema.py -v
```

### Executar testes com cobertura de código

```bash
pytest test_sistema.py --cov=sistema
```

### Executar um teste específico

```bash
pytest test_sistema.py::test_cadastrar_aluno -v
```

## 📊 Cobertura de Testes

O projeto possui **10 testes automatizados** que cobrem:

1. **test_cadastrar_aluno** - Cadastro bem-sucedido de aluno
2. **test_cadastrar_aluno_duplicado** - Bloqueio de cadastro duplicado
3. **test_consultar_salas** - Consulta das salas disponíveis
4. **test_realizar_reserva_sucesso** - Realização bem-sucedida de reserva
5. **test_bloqueio_reserva_duplicada** - Bloqueio de reserva em horário ocupado
6. **test_consultar_historico** - Consulta do histórico de reservas
7. **test_reserva_aluno_nao_cadastrado** - Validação de aluno cadastrado
8. **test_reserva_sala_inexistente** - Validação de sala válida
9. **test_cadastrar_aluno_nome_vazio** - Validação de entrada (nome)
10. **test_reservas_diferentes_horarios** - Múltiplas reservas no mesmo dia

## 📋 API do Sistema

### `cadastrar_aluno(nome: str) -> bool`

Cadastra um novo aluno no sistema.

**Parâmetros:**
- `nome` (str): Nome do aluno a cadastrar

**Retorna:**
- `True` se cadastrado com sucesso
- `False` se aluno já existe

**Exceções:**
- `ValueError` se nome estiver vazio ou inválido

---

### `consultar_salas() -> list`

Retorna a lista de salas disponíveis.

**Retorna:**
- Lista com os nomes de todas as salas

---

### `realizar_reserva(aluno: str, sala: str, horario: str) -> bool`

Realiza uma reserva de sala para um aluno.

**Parâmetros:**
- `aluno` (str): Nome do aluno (deve estar cadastrado)
- `sala` (str): Nome da sala (deve existir no sistema)
- `horario` (str): Horário da reserva (formato: "HH:MM")

**Retorna:**
- `True` se reserva realizada com sucesso
- `False` se horário já está ocupado

**Exceções:**
- `ValueError` se aluno não está cadastrado, sala não existe ou horário é inválido

---

### `consultar_historico() -> list`

Retorna o histórico de todas as reservas realizadas.

**Retorna:**
- Lista de dicionários com estrutura: `{"aluno": str, "sala": str, "horario": str}`

---

### `limpar_dados()`

Limpa todos os dados do sistema (utilitário para testes).

**Uso:** Chamado automaticamente antes de cada teste pela função `setup_function()`.

## 🔧 Dependências

- **pytest** (>=7.0.0) - Framework para testes
- **pytest-cov** (>=4.0.0) - Plugin de cobertura de testes

## 💾 Armazenamento de Dados

O sistema armazena dados em memória utilizando:
- `alunos` - Lista de nomes dos alunos cadastrados
- `reservas` - Lista de dicionários com informações das reservas
- `salas_disponiveis` - Lista de salas do sistema

**Nota:** Os dados são perdidos quando a aplicação é encerrada. Para persistência, seria necessário implementar um banco de dados.

## 🎯 Requisitos Atendidos

### Requisitos Funcionais
- ✅ Cadastrar um novo aluno
- ✅ Consultar as salas disponíveis
- ✅ Permitir que um aluno realize uma reserva de sala
- ✅ Impedir reservas para horários já ocupados
- ✅ Consultar o histórico de reservas realizadas

### Requisitos Não Funcionais
- ✅ Implementado em Python
- ✅ Código modularizado e bem estruturado
- ✅ Código bem comentado com docstrings
- ✅ Testes automatizados com pytest
- ✅ Suporte a cobertura de código

## 👨‍💻 Autor

Sistema desenvolvido como exemplo educacional de boas práticas em Python.

## 📝 Licença

Este projeto é fornecido como exemplo educacional.
