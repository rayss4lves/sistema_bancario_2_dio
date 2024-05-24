import conta as fco
import time as t

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        horario = t.localtime()
        formatted_time = t.strftime("%H:%M:%S -- %Y-%m-%d", horario)


        extrato.append(f'Deposito de: {valor:.2f} as {formatted_time}')
        print('Deposito relizado com sucesso!\n')
               
    else:
        print('\nFalha na operação!\n')
    return saldo, extrato


#função para sacar o valor de uma determinada conta
def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    
    saque_excedido = numero_saques >= LIMITE_SAQUES
    if saque_excedido == False:
        try:
            valor = float(input('Informe o valor que deseja sacar: '))
            
            saldo_excedido = valor > saldo
            limite_excedido = valor > limite
                    
            if saldo_excedido: 
                print('\nFalha na operação!\nSaldo insuficiente!\n ')
            elif limite_excedido:
                print('\nFalha na operação!\nExcedeu o limite de saque!\n ')   
            else:
                saldo-=valor
                horario = t.localtime()
                formatted_time = t.strftime("%H:%M:%S -- %Y-%m-%d", horario)

                extrato.append(f'Saque de: {valor:.2f} as {formatted_time}')
                numero_saques+=1 
                print('Saque realizado com sucesso!')
        except:
            print('Valor errado!')
    else:
        print('\nFalha na operação!\nO numero de saques permitidos foi excedido!\n ')

    return saldo, extrato, numero_saques
 
 
def imprimir_extrato(contas):
    num_conta = int(input('Informe o numero da conta: '))
            
    conta = fco.verifica_numero_conta(contas, num_conta)
    if conta:
        print('\n-------------------EXTRATO-------------------\n')
        for i in conta['extrato']:
            print(i)
        print(conta['saldo'])
        
        print('\n---------------------------------------------\n')
    else:
        print('\nFalha na operação!\nConta não encontrada!')
 