import os
import time
from array import *

quantidadeAlunos = 0
notasAluno = []

# Limpa a tela
def limpaTela():
  time.sleep(2)
  os.system('cls') or None


# Tela inicial, referente à urna
def telaInicial():
  global quantidadeAlunos

  print('\n╔══════════════════════════════════════════╗')
  print('║        Bem vindo à sala de aula!         ║')
  print('╚══════════════════════════════════════════╝')

  quantidadeAlunos = input("Digite a quantidade de alunos que a sala possui: ")

def AdicionaNomes():
  global quantidadeAlunos
  nomeAluno = []

  for i in reversed(range(int(quantidadeAlunos))):
    nomeAluno.append(input(f"Digite o nome do aluno nº {i + 1}: "))

  notasAluno.insert(0, nomeAluno)

def AdicionaNotas():
  global quantidadeAlunos
  notaAluno = []

  for i in reversed(range(int(quantidadeAlunos))):
    notaAluno.append(input(f"Digite a nota do(a) {notasAluno[0][i-1]}: "))

  notasAluno.insert(len(notasAluno), notaAluno)

    

def main():
  limpaTela()
  telaInicial()
  limpaTela()
  AdicionaNomes()
  limpaTela()
  AdicionaNotas()
  limpaTela()
  AdicionaNotas()
  print(notasAluno)

main()