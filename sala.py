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

def adicionaNomes():
  nomeAluno = []

  for i in reversed(range(int(quantidadeAlunos))):
    nomeAluno.append(input(f"Digite o nome do aluno nº {i + 1}: "))

  notasAluno.insert(0, nomeAluno)

def adicionaNotas():
  global quantidadeAlunos
  notaAluno = []

  for i in reversed(range(int(quantidadeAlunos))):
    notaAluno.append(input(f"Digite a nota do(a) {notasAluno[0][i-1]}: "))

  notasAluno.insert(len(notasAluno), notaAluno)

def tabelaAlunos():
  print('\n╔════════════════════════════════════════════════════════════════╗')
  print("| Nome | Nota 1º trimestre | Nota 2º trimestre | Média das notas |")
  print('╚════════════════════════════════════════════════════════════════╝')

  for i in reversed(range(int(quantidadeAlunos))):
    mediaNotaAluno = (int(notasAluno[1][i]) + int(notasAluno[2][i]))/2
    print("| ", notasAluno[0][i], ": ", notasAluno[1][i] , " | ", notasAluno[2][i], " | ", mediaNotaAluno, " |", "\n") 

def tabelaAlunosRecuperacao():
  print("  recuperação\n\n")
  print('\n╔══════════════╗')
  print("| Nome | Média |")
  

  for i in reversed(range(int(quantidadeAlunos))):
    mediaNotaAluno = (int(notasAluno[1][i]) + int(notasAluno[2][i]))/2

    if mediaNotaAluno < 6:
      print(notasAluno[0][i], "|", mediaNotaAluno, "\n") 
      
  print('╚══════════════╝')

def adicionaNotasRecuperacao():
  global quantidadeAlunos
  notasRecuperacao = []

  for i in range(int(quantidadeAlunos)):
    
    mediaNotaAluno = (int(notasAluno[1][i]) + int(notasAluno[2][i]))/2

    if mediaNotaAluno < 6:
      notasRecuperacao.append(input(f"Digite a nota da prova de recuperacao de {notasAluno[0][i]}: "))
    else:
      notasRecuperacao.append('')  

  notasAluno.insert(len(notasAluno), notasRecuperacao)
  print(notasAluno)

def tabelaNotaFinal():
  print('\n╔══════════════════════════════════════════════════════════════════════════════════╗')
  print("| Nome | Nota 1º trimestre | Nota 2º trimestre | Nota Recuperação | Média das notas |")
  print('╚═══════════════════════════════════════════════════════════════════════════════════╝')

  for i in reversed(range(int(quantidadeAlunos))):
    if notasAluno[3][i] != '':
      mediaNotaAluno = (int(notasAluno[1][i]) + int(notasAluno[2][i]) + int(notasAluno[3][i]))/3
    else:
      mediaNotaAluno = (int(notasAluno[1][i]) + int(notasAluno[2][i]))/2

    print("| ", notasAluno[0][i], ": ", notasAluno[1][i] , " | ", notasAluno[2][i], " | ", notasAluno[3][i] ," | ", mediaNotaAluno, " |", "\n")

def main():
  limpaTela()

  telaInicial()
  limpaTela()

  adicionaNomes()
  limpaTela()

  # Notas primeiro trimestre
  adicionaNotas()
  limpaTela()

  # Notas segundo trimestre
  adicionaNotas()
  limpaTela()

  tabelaAlunos()
  limpaTela()

  tabelaAlunosRecuperacao()
  limpaTela()

  adicionaNotasRecuperacao()
  limpaTela()

  tabelaNotaFinal()
  
main()