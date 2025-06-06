def fazer_login(usuarios_pre_cadastrados):
    print("\n--- FAZER LOGIN ---")
    tentativas = 3
    while tentativas > 0:
        nome_usuario = input("Digite seu nome de usuário: ").strip()
        senha_digitada = input("Digite sua senha: ").strip()

        if nome_usuario in usuarios_pre_cadastrados:
            if usuarios_pre_cadastrados[nome_usuario] == senha_digitada:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {nome_usuario}!")
                return True  # Retorna True para indicar login de sucesso
            else:
                tentativas -= 1
                print(f"Senha incorreta. Você tem mais {tentativas} tentativas.")
        else:
            tentativas -= 1
            print(f"Usuário '{nome_usuario}' não encontrado. Você tem mais {tentativas} tentativas.")

        if tentativas == 0:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")
            return False # Retorna False se o login falhar

def registrar_usuario(usuarios_pre_cadastrados):
    print("\n--- REGISTRAR NOVO USUÁRIO ---")
    while True:
        novo_usuario = input("Digite o nome de usuário desejado (ou 'sair' para cancelar): ").strip()
        if novo_usuario.lower() == 'sair':
            print("Registro cancelado.")
            return False
        if not novo_usuario:
            print("Nome de usuário não pode ser vazio.")
            continue
        if ' ' in novo_usuario: # Remove a verificação de vírgula já que não é salva em arquivo
            print("Nome de usuário não pode conter espaços.")
            continue
        if novo_usuario in usuarios_pre_cadastrados:
            print(f"O usuário '{novo_usuario}' já existe. Escolha outro nome.")
        else:
            break # Nome de usuário válido

    while True:
        nova_senha = input("Digite a senha desejada: ").strip()
        if not nova_senha:
            print("Senha não pode ser vazia.")
            continue
        if ' ' in nova_senha: # Remove a verificação de vírgula
            print("Senha não pode conter espaços.")
            continue
        confirmar_senha = input("Confirme a senha: ").strip()

        if nova_senha == confirmar_senha:
            usuarios_pre_cadastrados[novo_usuario] = nova_senha # Adiciona ao dicionário em memória
            print(f"Usuário '{novo_usuario}' registrado com sucesso!")
            print("Atenção: Este registro é temporário e não será salvo após o programa ser encerrado.")
            return True # Retorna True para indicar registro de sucesso
        else:
            print("As senhas não coincidem. Tente novamente.")

def main():
    usuarios_cadastrados = {
        "admin": "12345",
        "usuario1": "senha123",
        "teste": "abcde"
    }
    while True:
        print("\n--- MENU DE LOGIN ---")
        print("1. Fazer Login")
        print("2. Registrar Novo Usuário")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            if fazer_login(usuarios_cadastrados):
                print("Você está na área restrita!")
                pass 
        elif opcao == '2':

            registrar_usuario(usuarios_cadastrados)

        elif opcao == '3':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
if __name__ == "__main__":
    main()
