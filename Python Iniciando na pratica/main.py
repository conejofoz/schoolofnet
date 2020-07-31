import getpass
import os

account_list = {
    '0001-02': {
        'password': '123456',
        'name': 'Silvio Coelho',
        'value': 500,
        'admin': True
    },
    '0002-02': {
        'password': '123456',
        'name': 'Dunha da silva',
        'value': 50,
        'admin': False
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5
}

while True:
    print("******************************************")
    print("***Caixa eletrônico - Banco Conejo***")
    print("******************************************")

    account_typed = input("Digite sua conta: ")
    password_typed = getpass.getpass("Digite sua senha: ")



    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        #if account_typed in account_list and password_typed == account_list['0001-02']['password']:
        # pega a conta digitada que deve corresponder com uma das chaves do dicionario
        #print('Conta válida')
        print('1 - Saldo')
        print('2 - Saque')
        if account_list[account_typed]['admin']:
            print('10 - Incluir cedulas')
        option_typed = input('Escolha uma opção')

        if option_typed == '1':
            print('Seu saldo é %s' % account_list[account_typed]['value'])
        elif option_typed == '10' and account_list[account_typed]['admin']:
            amount_typed =  input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cedula a ser inserida: ')
            #money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado')
            money_slips_user = {}
            value_int = int(value_typed)

            # se o resto da divisão do valor infomado for maior que zero
            #   descobre quantas notas de 100 precisa
            # e se essa quantidade de notas é menor ou igual a quantidade de notas de 100
            #   disponíveis no caixa
            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int //100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print('O Caixa não tem cédulas disponíveis para o valor informado')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                print('Pegue suas notas')
                print(money_slips_user)
    else:
        print('Acesso negado')

    input('Pressione Enter para continuar')
    '''if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')'''
    #operacao ternaria
    limpar = 'cls' if os.name == 'nt' else 'clear'
    os.system(limpar)
