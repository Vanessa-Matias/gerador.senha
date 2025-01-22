import random
import string

#Quantidade agrupada de opções que o programa pode ter de escolhas para a senha
def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation 
    option = ascii_options + number_options + punt_options

#Escolha aleatória
    password_user = ""

    for i in range(0, len_pass):
        digit = random.choice(option)
        password_user = password_user + digit

    return password_user

print('\033[1;33m==========    G E R A D O R - D E - S E N H A    ===========\033[m')
choice_user = input('\033[1;32mCOLOQUE A QUANTIDADE DE DIGITOS: \033[m')
print('------------------------------------------------------------\n')

#coletando resposta do usuário

if choice_user.isdigit():
    choice_user = int(choice_user)
#Caso o usuário coloque uma quantidade de caracter zero, menor que 8 ou maior que 32, uma mensagem de alerta será exibida
    if choice_user == 0:
        print('\033[1;31mQUANTIDADE INVÁLIDA DE CARACTERES.\nPOR FAVOR, DIGITE OUTRO NÚMERO!\033[m')
        print('\033[1;33m=============================================================\033[m')
    elif choice_user < 8:
        print('\033[1;31mSENHA MUITO FRACA!\nCOLOQUE UMA QUANTIDADE MAIOR DE CARACTERES!\033[m')
        print('\033[1;33m============================================================\033[m')
    elif choice_user > 30:
        print('\033[1;31mSENHA MUITO LONGA!\nDIGITE UMA QUANTIDADE MENOR DE CARACTERES!\033[m')
        print('\033[1;33m============================================================\033[m')
    else:
        reponse = password_generator(len_pass = choice_user)
        print(f'\033[1;32mSENHA GERADA:\033[m {reponse}\n')
        print('\033[1;33m============================================================\033[m')
else:
    print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
    print('\033[1;33m============================================================\033[m')
    