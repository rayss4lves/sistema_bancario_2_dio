import conta as fco
import banco as fb
import clientes as fc


def menu():
    try:
        print('\n=============================================')
        print('=\tInforme o que deseja fazer:         =')
        print('= \t1 - Depositar                       =\n= \t2 - Sacar                           =\n= \t3 - Extrato                         =\n= \t4 - Cadastrar cliente               =\n= \t5 - Criar conta                     =\n= \t6 - consultar conta                 =\n= \t7 - consultar cliente               =\n= \t8 - Listar contas                   =\n= \t9 - listar clientes                 =\n= \t10 - Sair                           =')
        print('=============================================\n')
        return int(input('= '))
    except:
        print('\n')

      
def main(): 
    clientes = []
    contas = []
    extrato = []
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    saldo = 0
    AGENCIA = '0001'
    
    
    while True:   
        op = menu()
        
        if op == 1:
            print('\n-------------------------------------------------------------------\n')

            conta_encontrada = False
            try:
                num_conta = int(input('Informe o numero da conta: '))
                
                conta = fco.verifica_numero_conta(contas, num_conta)
                
                if conta:
                    conta_encontrada = True
                    valor = float(input('Informe o valor que deseja depositar: '))
                    conta['saldo'], conta['extrato'] = fb.depositar(valor, conta['saldo'], conta['extrato'])
                                                            
                if not conta_encontrada:
                    print('Falha na operação!\nCrie uma conta primeiro!\n')     
            except: 
                print('Valor errado!\n')   
            print('\n-------------------------------------------------------------------\n')
        elif op == 2:
            print('\n-------------------------------------------------------------------\n')
            conta_encontrada = False
            try:
                num_conta = int(input('Informe o numero da conta: '))
                
                conta = fco.verifica_numero_conta(contas, num_conta)
                
                if conta:
                    if conta['Numero_saques'] <= LIMITE_SAQUES:
                        conta_encontrada = True
                        conta['saldo'], conta['extrato'], conta['Numero_saques'] = fb.sacar(conta['saldo'], conta['extrato'], conta['Numero_saques'], LIMITE_SAQUES, limite)
                if not conta_encontrada:
                    print('\nFalha na operação!\nCrie uma conta primeiro!\n')   
            except ValueError:
                print('Valor errado!\n')
                 
            print('\n-------------------------------------------------------------------\n')
        elif op == 3:
    
            fb.imprimir_extrato(contas)
            
        elif op == 4:
            print('\n-------------------------------------------------------------------\n')
            fc.cadastrar_cliente(clientes)
            
            print(clientes)
            
            print('\n-------------------------------------------------------------------\n')   
        elif op == 5:
            print('\n-------------------------------------------------------------------\n')
            
            fco.criar_conta(AGENCIA, contas, clientes, saldo, extrato, numero_saques)
            
            print(contas)
            
            print('\n-------------------------------------------------------------------\n')
        elif op == 6:
            print('\n-------------------------------------------------------------------\n')

            fco.consultar_conta(contas)
            
            print('\n-------------------------------------------------------------------\n')
        elif op == 7:
            print('\n-------------------------------------------------------------------\n')

            fc.consultar_cliente(clientes)
            
            print('\n-------------------------------------------------------------------\n')
        elif op == 8:
            print('\n-------------------------------------------------------------------\n')
            
            fco.listar_contas(contas)
            
            print('\n-------------------------------------------------------------------\n')
        elif op == 9:
            print('\n-------------------------------------------------------------------\n')

            fc.listar_clientes(clientes) 
            
            print('\n-------------------------------------------------------------------\n')   
        elif op == 10:
            print('Programa encerrado...\n ')
            break
        else:
            print('Opção inválida!!\n')

main()