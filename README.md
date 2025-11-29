🏦 Sistema Bancário com Lista de Contas (Python / POO)

Este projeto é uma implementação simples de um sistema bancário utilizando Programação Orientada a Objetos (POO) em Python.
O sistema permite:

Cadastrar contas

Creditar valores

Debitar valores

Verificar saldo

Transferir entre contas

Simular operações no final do arquivo

Todo o gerenciamento das contas é feito por uma lista interna com limite de 100 contas.

📁 Estrutura do Projeto
📦 Projeto
├── bancoList.py
├── contasDobanco.py

🔹 contasDobanco.py — Classe ContasP

Define uma conta bancária com número e saldo inicial.

Métodos da classe:
Método	Descrição
get_numero()	Retorna o número da conta
get_saldo()	Retorna o saldo atual
debitar(valor)	Debita um valor da conta, se houver saldo
creditar(valor)	Credita um valor na conta
Validações feitas internamente:

Valor deve ser positivo

No débito, o saldo deve ser suficiente

🔹 bancoList.py — Classe bancoLista

Gerencia um conjunto de contas bancárias.

Atributos:

contas: lista com 100 posições

indice: controla quantas contas foram cadastradas

Métodos:
Método	Função
cadastrar(conta)	Adiciona a conta no banco
procurar_conta(numero)	Retorna uma conta pelo número
debitar(num, valor)	Debita da conta informada
creditar(num, valor)	Credita na conta informada
saldo(num)	Retorna o saldo da conta
transferir(origem, destino, valor)	Transfere valores entre contas
A transferência inclui validações:

Verificação de conta de origem e destino

Verificação de saldo

Verificação de valor válido
