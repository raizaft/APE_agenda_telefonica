import os
import sys
from pyfiglet import Figlet
from termcolor import colored, cprint

#Dupla: Raiza Andrade e Venilson Neves


#Função de limpar o terminal
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


#Função verificar telefone - Venilson
def telefone_valido():
  while True:
    #remore espaços, parenteses e hifens do numero
    numero = input('Telefone (DDD + 9 + número): ').replace(' ', '').replace(
      '(', '').replace(')', '').replace('-', '')
    if numero == 'exit':
      cls()
      return 'exit'
    #verifica se é numero e se possui 11 digitos
    if len(numero) == 11 and numero.isnumeric():
      return numero
    else:
      cls()
      print('Telefone inválido. Digite novamente.')
      print()


#Função adicionar contato - Venilson
def adicionar(agenda):
  print('Digite \'exit\' p/ cancelar.')
  nome = input('\nNome: ')
  if nome == 'exit':
    cls()
    return
  else:
    numero = telefone_valido()
    #adiciona o novo contato na agenda do usuário
    with open(agenda + '.agenda.txt', 'a') as f:
      f.write(nome + ';' + numero + '\n')
      f.close()
    cls()
    print('\nContato adicionado com sucesso!')
    return


#Função listar contatos - Venilson
def listar(agenda):
  with open(agenda + '.agenda.txt', 'r') as f:
    lista = f.read()
    lista = lista.splitlines()
    #apresenta a lista em ordem alfabética
    lista.sort()
    if len(lista) > 0:
      for linha in lista:
        nome, num = linha.split(';')
        print(f'Nome: {nome}')
        print(f'Número: {num}')
        print()
    else:
      cls()
      print('Nenhum contato cadastrado.')
  return


#Função pesquisar contatos - Raiza
def pesquisar(agenda):
  print('Digite \'exit\' p/ cancelar.')
  pesq = input('\nInsira o nome ou parte do nome: ')
  if pesq == 'exit':
    return
  else:
    with open(agenda + '.agenda.txt', 'r') as f:
      lista = f.read()
      cls()
      #se o nome estiver no arquivo, entra no for para imprimir o contato correspondente
      if pesq in lista:
        lista = lista.splitlines()
        lista.sort()
        for linha in lista:
          if pesq in linha:
            nome, num = linha.split(';')
            print(f'Nome: {nome}')
            print(f'Número: {num}')
            print()
        return
      else:
        print('\nContato não encontrado.')
        return


#Função para remover contato - Raiza
def remover(agenda):
  print('Digite \'exit\' p/ cancelar.')
  pesq = input('\nInsira o nome do contato a ser removido: ')
  if pesq == 'exit':
    return
  else:
    with open(agenda + '.agenda.txt', 'r') as f:
      lista = f.read()
      cls()
      #verifica se o nome está no arquivo
      if pesq in lista:
        lista = lista.splitlines()
        for linha in lista:
          linha = linha.replace('\n', '')
        tam = len(lista)
        for i in range(0, tam):
          nome = lista[i].split(';')
          if pesq == nome[0]:
            del lista[i]
            f.close
          #reescreve a agenda sem o contato removido
          with open(agenda + '.agenda.txt', 'w') as f:
            for i in lista:
              f.write(i + '\n')
              f.close
        print('\nContato removido.')
        return
      else:
        print('\nContato não encontrado.')
        return


#Função alterar contato - Venilson
def alterar(agenda):
  pesq = input('\nInsira o nome do contato a ser alterado: ')
  with open(agenda + '.agenda.txt', 'r') as f:
    lista = f.read()
    if pesq in lista:
      print('Insira o novo número de telefone. Digite \'exit\' p/ cancelar. ')
      num = telefone_valido()
      lista = lista.splitlines()
      for linha in lista:
        linha = linha.replace('\n', '')
      for i in range(len(lista)):
        nome = lista[i].split(';')
        if pesq == nome[0]:
          lista[i] = pesq + ';' + num
          f.close
        with open(agenda + '.agenda.txt', 'w') as f:
          for i in lista:
            f.write(i + '\n')
            f.close
      cls()
      print('\nContato alterado.')
      return
    else:
      print('\nContato não encontrado.')
      return


#Função excluir conta - Raiza
def excluir(agenda):
  while True:
    confirma = input('Deseja mesmo excluir a conta (s/n): ').lower()
    if confirma == 's':
      os.remove(agenda + '.agenda.txt')
      with open('usuarios.txt', 'r') as f:
        lista = f.read()
        lista = lista.splitlines()
        for linha in lista:
          linha = linha.replace('\n', '')
          for i in range(len(lista)):
            log = lista[i].split(';')
            if agenda == log[0]:
              del lista[i]
              f.close
            with open('usuarios.txt', 'w') as f:
              for i in lista:
                f.write(i + '\n')
                f.close
      cls()
      break
    elif confirma == 'n':
      cls()
      return
    else:
      cls()
      print('Opção inválida. Tente novamente!')


#Função para verificar se a senha é alphanumerica e tem 6 caracteres - Raiza
def senha_valida(senha):
  return senha.isalnum() and len(senha) == 6


#Função para verificar se o login já é cadastrado - Venilson
def login_existe(login):
  if os.path.isfile('usuarios.txt'):
    with open("usuarios.txt", "r") as f:
      linhas = f.readlines()
      for linha in linhas:
        num = linha.split(";")
        if num[0] == login:
          return True


#Função registrar - Raiza
def registrar():
  while True:
    print('Digite \'exit\' p/ cancelar.')
    print()
    login = telefone_valido()
    if login == 'exit':
      break
    else:
      senha = input('Senha (6 dígitos: letra+número): ')
      if not login_existe(login) and senha_valida(senha):
        #Cria uma agenda pro novo usuário
        with open(login + '.agenda.txt', 'w') as f:
          f.close()
        #Adiciona o novo usuário na lista de usuários
        with open("usuarios.txt", "a") as f:
          f.write(login + ";" + senha + "\n")
          f.close()
          cls()
          break
      elif login_existe(login):
        cls()
        print('Telefone já cadastrado. Tente novamente!')
        print()
      elif not senha_valida(senha):
        cls()
        print('Senha inválida. Tente novamente!')
        print()


#Função menu principal - Raiza
def menu_principal(agenda):
  while True:
    print('''
╔══════════════════════════════╗
║ [1] Adicionar Contato        ║
║ [2] Listar Contatos          ║
║ [3] Pesquisar Contato        ║
║ [4] Remover Contato          ║
║ [5] Alterar Contato          ║
║ [6] Excluir Conta do Usuário ║
║ [7] Sair                     ║
╚══════════════════════════════╝
    ''')
    escolha = int(input('Escolha a opção desejada: '))
    if escolha == 1:
      cls()
      adicionar(agenda)
    elif escolha == 2:
      cls()
      listar(agenda)
    elif escolha == 3:
      cls()
      pesquisar(agenda)
    elif escolha == 4:
      cls()
      remover(agenda)
    elif escolha == 5:
      cls()
      alterar(agenda)
    elif escolha == 6:
      cls()
      excluir(agenda)
      break
    elif escolha == 7:
      cls()
      break
    else:
      cls()
      print('\nA opção escolhida não existe. Tente outra vez!')
    print()


#Função verificar login - Raiza
def verificar_login(login, senha):
  with open("usuarios.txt", "r") as f:
    linhas = f.readlines()
    for linha in linhas:
      num = linha.split(";")
      sen = num[1][0:6]
      if num[0] == login and sen == senha:
        return True


#Função login - Raiza
def login():
  if not os.path.isfile('usuarios.txt'):
    print('Nenhum usuário cadastrado.')
    return
  else:
    while True:
      print('Digite \'exit\' p/ cancelar.')
      login = input("\nLogin: ")
      if login == "exit":
        cls()
        return
        break
      else:
        senha = input('Senha: ')
        #Verificar se login e senha são válidos
        if verificar_login(login, senha):
          cls()
          menu_principal(login)
          break
        else:
          cls()
          print('\nLogin inválido. Tente novamente!')
          print()


#Função menu inicial - Raiza
def menu_inicial():
  while True:
    f = Figlet(font='big')
    print(colored(f.renderText('iGend@'), 'green', attrs=["bold"]))
    print('''
╔═══════════════════════╗
║ [1] Entrar            ║
║ [2] Registrar Usuário ║
║ [3] Sair              ║
╚═══════════════════════╝
      ''')
    escolha = int(input('Escolha a opção desejada: '))
    print()
    if escolha == 1:
      cls()
      login()
    elif escolha == 2:
      cls()
      registrar()
    elif escolha == 3:
      cls()
      print('''
Programa encerrado!
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
      ''')
      return
    else:
      print('\nOpção inválida! Escolha outra opção.')
    print()


#Função principal
menu_inicial()
