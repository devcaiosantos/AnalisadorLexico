alphabet = {'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z',
            '0','1','2','3','4','5','6','7','8','9',
            '+','-','*','/','<','=','>','!',';',','
            '(',')','[',']','{','}' }

def manipula_estado(estado_atual, caracter, proxcaracter):
    ##print(estado_atual, caracter, proxcaracter+'\n')
    novo_estado = ''
    token = ''
    if(estado_atual == 'inicial'):
        if(caracter == ' '):
            novo_estado = 'inicial'
        else:
            novo_estado = caracter;

    if(estado_atual == 'variavel'):
        if(proxcaracter != ' ' or proxcaracter != 'EOL'):
            token = 'ID'
            novo_estado = 'inicial';
        else:
            novo_estado = estado_atual;
            
    if(caracter == '+'):
        token = 'PLUS'
        novo_estado = 'inicial';

    if(caracter == '-'):
        token = 'MINUS'
        novo_estado = 'inicial';

    if(caracter == '*'):
        token = 'TIMES'
        novo_estado = 'inicial';

    if(caracter == '/'):
        token = 'DIVIDE'
        novo_estado = 'inicial';
    
    if(caracter == '<'):
        if(proxcaracter == '='):
            novo_estado = '<=';
        else:
            novo_estado = 'inicial';
            token = 'LESS';

    if(caracter =='>'):
        if(proxcaracter == '='):
            novo_estado = '>=';
        else:
            novo_estado = 'inicial';
            token = 'GREATER';
    
    if(caracter =='('):
        token = 'LPAREN'
        novo_estado = 'inicial';

    if(caracter ==')'):
        token = 'RPAREN'
        novo_estado = 'inicial'

    if(caracter =='['):
        token = 'LBRACKETS'
        novo_estado = 'inicial';
    
    if(caracter ==']'):
        token = 'RBRACKETS'
        novo_estado = 'inicial';

    if(caracter =='{'):
        token = 'LBRACES'
        novo_estado = 'inicial';

    if(caracter =='}'):
        token = 'RBRACES'
        novo_estado = 'inicial';

    if(caracter == '='):
        if(proxcaracter == '='):
            novo_estado = '==';
        else:
            token = 'ATTRIBUTION';
            novo_estado = 'inicial';

    if( caracter == ';' ):
        token = 'SEMICOLON'
        novo_estado = 'inicial';

    if( caracter == ',' ):
        token = 'COMMA'
        novo_estado = 'inicial';

    if( caracter == '!' ):
        if(proxcaracter == '='):
            novo_estado = '!=';
        else:
            novo_estado = 'inicial';

    if(estado_atual =='!='):
        token= 'DIFFERENT';
        novo_estado = 'inicial';

    if(estado_atual =='<='):
        token = 'LESS_EQUAL'
        novo_estado = 'inicial';

    if(estado_atual =='>='):
        token = 'GREATER_EQUAL'
        novo_estado = 'inicial';
    
    if(estado_atual =='=='):
        token = 'EQUALS'
        novo_estado = 'inicial';
    
    if(estado_atual == 'i'):
        novo_estado = 'i'+caracter;

    if(estado_atual == 'if'):
        if(caracter == ' ' or caracter == '('):
            token = 'IF';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    # if(estado_atual == 'int'):
    #     if(proxcaracter == ' ' or proxcaracter == 'EOL'):
    #         token = 'INT';
    #         novo_estado = 'inicial';
    #     else:
    #         novo_estado = 'variavel';
    
    
    return novo_estado,token

                

                
        

def main():
    linhas = []
    estado_atual = 'inicial';
    tokens = []
    with open('texto.c') as f:
        linhas = f.readlines()
    #Lendo linha a linha para não ter os '\n'
    for linha in linhas:
        for i in range(0, len(linha), 1):
            caracter = linha[i]
            if(i+1>=len(linha)):
                proxcaracter = 'EOL' #Final da linha
            else:
                proxcaracter = linha[i+1]
            novo_estado, token = manipula_estado(estado_atual, caracter, proxcaracter)
            print('novo_estado: '+novo_estado, 'token: '+token)

            estado_atual = novo_estado;
            if(token != ''):
                tokens.append(token)
            ##estado_atual = response['novo_estado']
            # if(response['token']):
            #     tokens.append(response['token']);

    print(tokens);
            
main()



# if(linha[i] == 'a'):
            # if(linha[i] == 'b'):
            # if(linha[i] == 'c'):
            # if(linha[i] == 'd'):
            # if(linha[i] == 'e'):
            # if(linha[i] == 'f'):
            # if(linha[i] == 'g'):
            # if(linha[i] == 'h'):
            # if(linha[i] == 'i'):
            # if(linha[i] == 'j'):
            # if(linha[i] == 'k'):
            # if(linha[i] == 'l'):
            # if(linha[i] == 'm'):
            # if(linha[i] == 'n'):
            # if(linha[i] == 'o'):
            # if(linha[i] == 'p'):
            # if(linha[i] == 'q'):
            # if(linha[i] == 'r'):
            # if(linha[i] == 's'):
            # if(linha[i] == 't'):
            # if(linha[i] == 'u'):
            # if(linha[i] == 'v'):
            # if(linha[i] == 'w'):
            # if(linha[i] == 'x'):
            # if(linha[i] == 'y'):
            # if(linha[i] == 'z'):
            # if(linha[i] == '0'):
            # if(linha[i] == '1'):
            # if(linha[i] == '2'):
            # if(linha[i] == '3'):
            # if(linha[i] == '4'):
            # if(linha[i] == '5'):
            # if(linha[i] == '6'):
            # if(linha[i] == '7'):
            # if(linha[i] == '8'):
            # if(linha[i] == '9'):
            # if(linha[i] == '+'):
            # if(linha[i] == '-'):
            # if(linha[i] == '*'):
            # if(linha[i] == '/'):
            # if(linha[i] == '<'):
            # if(linha[i] == '='):
            # if(linha[i] == '>'):
            # if(linha[i] == '!'):
            # if(linha[i] == ';'):
            # if(linha[i] == ','):
            # if(linha[i] == '('):
            # if(linha[i] == ')'):
            # if(linha[i] == '['):
            # if(linha[i] == ']'):
            # if(linha[i] == '{'):
            # if(linha[i] == '}'):