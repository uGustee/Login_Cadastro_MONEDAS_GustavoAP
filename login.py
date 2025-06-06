def fazer_login(contas):
    print("\n🔐 LOGIN BANCÁRIO")
    tentativas = 3
    while tentativas > 0:
        usuario = input("👤 Usuário: ").strip()
        senha = input("🔑 Senha: ").strip()

        if usuario in contas:
            if contas[usuario]['senha'] == senha:
                print(f"\n✅ Bem-vindo(a), {usuario}!")
                print(f"💰 Saldo: R${contas[usuario]['saldo']:.2f}")
                return True
            else:
                tentativas -= 1
                print(f"❌ Senha incorreta. Tentativas restantes: {tentativas}")
        else:
            tentativas -= 1
            print(f"❌ Usuário não encontrado. Tentativas restantes: {tentativas}")
        
        if tentativas == 0:
            print("🚫 Acesso bloqueado.")
            return False

def registrar_conta(contas):
    print("\n📝 ABRIR CONTA")
    while True:
        novo_usuario = input("👤 Novo usuário (ou 'sair' pra cancelar): ").strip()
        if novo_usuario.lower() == 'sair':
            print("🚫 Cadastro cancelado.")
            return False
        if not novo_usuario or ' ' in novo_usuario:
            print("⚠️ Nome inválido. Evite espaços ou campos vazios.")
            continue
        if novo_usuario in contas:
            print("⚠️ Usuário já existe.")
            continue
        break

    while True:
        senha = input("🔑 Crie uma senha: ").strip()
        if not senha or ' ' in senha:
            print("⚠️ Senha inválida. Evite espaços ou campos vazios.")
            continue
        confirmar = input("🔄 Confirme a senha: ").strip()
        if senha != confirmar:
            print("❌ Senhas diferentes. Tente de novo.")
            continue
        break

    contas[novo_usuario] = {
        'senha': senha,
        'saldo': 0.0
    }
    print(f"✅ Conta '{novo_usuario}' criada com sucesso!")
    return True

def main():
    contas = {
        "admin": {"senha": "12345", "saldo": 10000.00},
        "cliente1": {"senha": "senha123", "saldo": 250.75}
    }

    while True:
        print("\n🏦 BANCO MONEDAS - MENU")
        print("1️⃣  Entrar na conta")
        print("2️⃣  Criar nova conta")
        print("3️⃣  Sair")

        escolha = input("👉 Escolha uma opção: ").strip()

        if escolha == '1':
            fazer_login(contas)
        elif escolha == '2':
            registrar_conta(contas)
        elif escolha == '3':
            print("👋 Valeu por usar o Banco Monedas!")
            break
        else:
            print("❌ Opção inválida. Digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()
