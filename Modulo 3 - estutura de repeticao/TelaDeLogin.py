### Criar uma tela de login e senha

usuarios = 'daniel'
senhas = 123456
digiteUsuario = input("Digite o usuário de login: ")
digiteSenha = int(input("Digite sua senha: "))
if usuarios != digiteUsuario:
    cadastro = input("Usuario não existe, deseja cadastrar: (S/N)")
    if cadastro == 'S':
        digiteUsuario = input("Digite o usuário de login: ")
        digiteSenha = int(input("Digite sua senha: "))
        usuarios = digiteUsuario
        senhas = digiteSenha
        login = input("Deseja fazer o login?: (S/N): ")
        if cadastro == 'S':
            digiteUsuario = input("Digite o usuário de login: ")
            digiteSenha = int(input("Digite sua senha: "))
            if senhas == digiteSenha:
                print("Voce logou")
            else:
                print("Usuário ou senha invalida ")
        else:
            exit
    else:
        print("Usuário ou senha invalida ")
else:
    if senhas == digiteSenha:
        print("Voce logou")
        salario = float(input('Digite o salário atual: '))
        salarioNovo = float(input('Digite o novo salário: '))
        valorAumento = (salarioNovo - salario) 
        porcentagem = (valorAumento/salario) * 100
        print(f'O aumento foi de : R$ {valorAumento: .2f}')
        print(f'Você teve um aumento de : R$ {porcentagem: .4f}%')
    else:
        print("Usuário ou senha invalida ")