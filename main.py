letras = {'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z'}
numeros = {'0','1','2','3','4','5','6','7','8','9'};
simbolos = {'+','-','*','/','<','=','>','!',';',',','(',')','[',']','{','}' }

def manipula_estado(estado_atual, caracter, proxcaracter):
    
    novo_estado = ''
    token = ''
   
    ####################################################################
    if(caracter == ' '):
        novo_estado = 'inicial'
    elif(caracter == '+'):
        token = 'PLUS'
        novo_estado = 'inicial';

    elif(caracter == '-'):
        token = 'MINUS'
        novo_estado = 'inicial';

    elif(caracter == '*'):
        token = 'TIMES'
        novo_estado = 'inicial';

    elif(caracter == '/'):
        token = 'DIVIDE'
        novo_estado = 'inicial';
    
    elif(caracter == '<'):
        if(proxcaracter == '='):
            novo_estado = '<=';
        else:
            novo_estado = 'inicial';
            token = 'LESS';

    elif(caracter =='>'):
        if(proxcaracter == '='):
            novo_estado = '>=';
        else:
            novo_estado = 'inicial';
            token = 'GREATER';
            
    elif(caracter =='('):
        token = 'LPAREN'
        novo_estado = 'inicial';

    elif(caracter ==')'):
        token = 'RPAREN'
        novo_estado = 'inicial'

    elif(caracter =='['):
        token = 'LBRACKETS'
        novo_estado = 'inicial';
    
    elif(caracter ==']'):
        token = 'RBRACKETS'
        novo_estado = 'inicial';

    elif(caracter =='{'):
        token = 'LBRACES'
        novo_estado = 'inicial';

    elif(caracter =='}'):
        token = 'RBRACES'
        novo_estado = 'inicial';

    elif(caracter == '='):
        if(proxcaracter == '='):
            novo_estado = '==';
        else:
            token = 'ATTRIBUTION';
            novo_estado = 'inicial';

    elif( caracter == ';' ):
        token = 'SEMICOLON'
        novo_estado = 'inicial';

    elif( caracter == ',' ):
        token = 'COMMA'
        novo_estado = 'inicial';

    elif( caracter == '!' ):
        if(proxcaracter == '='):
            novo_estado = '!=';
        else:
            novo_estado = 'inicial';
        
    elif( caracter in numeros ):
        if (estado_atual == 'numero' or estado_atual == 'inicial'):
            if((proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')):
                novo_estado = 'inicial'
                token = 'NUMBER';
            else:
                novo_estado = 'numero';
        else:
            if((proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')):
                novo_estado = 'inicial'
                token = 'ID';
            else:
                novo_estado = 'variavel';
    
    elif(caracter == 'a'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
          ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'b'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'c'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'd'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'e'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        elif(proxcaracter == 'l'):
            novo_estado = 'el';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'f'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'g'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'h'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'i'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        elif(proxcaracter == 'f' or proxcaracter == 'n'):
            novo_estado = 'i'+proxcaracter;
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'j'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'k'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'l'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'm'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'n'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'o'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'p'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'q'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'r'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        elif(proxcaracter == 'e'):
            novo_estado = 're';
        else:
            novo_estado = 'variavel';

    elif(caracter == 's'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 't'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'u'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'v'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        elif(proxcaracter == 'o'):
            novo_estado = 'vo';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'w'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        elif(proxcaracter == 'h'):
            novo_estado = 'wh';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'w'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        elif(proxcaracter == 'h'):
            novo_estado = 'wh';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'x'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';
    
    elif(caracter == 'y'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    elif(caracter == 'z'):
        if(
            (proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL')
                and 
            (estado_atual == 'inicial' or estado_atual == 'variavel')
        ):
            novo_estado = 'inicial';
            token = 'ID';
        else:
            novo_estado = 'variavel';

    #####################################################################
    

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
    
#------------------ESTADO IF-----------------------------------------#  

    if(estado_atual == 'if'):
        if(proxcaracter == ' ' or proxcaracter == '(' or proxcaracter =='EOL'):
            token = 'IF';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

#--------------------------------------------------------------------#  

#------------------ESTADO INT-----------------------------------------#  
    if(estado_atual == 'in'):
        if(proxcaracter == 't'):
            novo_estado = 'int';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    
    if(estado_atual == 'int'):
        if(proxcaracter == ' ' or proxcaracter =='EOL'):
            token = 'INT';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    #---------------------------------------------------------------------#     

    #------------------ESTADOS ELSE-----------------------------------------#

    if(estado_atual == 'el'):
        if(proxcaracter == 's'):
            novo_estado = 'els';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    if(estado_atual == 'els'):
        if(proxcaracter == 'e'):
            novo_estado = 'else';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    
    if(estado_atual == 'else'):
        if(proxcaracter == ' ' or proxcaracter == '(' or proxcaracter =='EOL'):
            token = 'ELSE';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    #--------------------------------------------------------------------------#

    #------------------ESTADOS RETURN------------------------------------------#
    if(estado_atual == 're'):
        if(proxcaracter == 't'):
            novo_estado = 'ret';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    if(estado_atual == 'ret'):
        if(proxcaracter == 'u'):
            novo_estado = 'retu';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    
    if(estado_atual == 'retu'):
        if(proxcaracter == 'r'):
            novo_estado = 'retur';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    if(estado_atual == 'retur'):
        if(proxcaracter == 'n'):
            novo_estado = 'return';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    
    if(estado_atual == 'return'):
        if(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'RETURN';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    #--------------------------------------------------------------------------#


    #------------------ESTADOS VOID--------------------------------------------#
    if(estado_atual == 'vo'):
        if(proxcaracter == 'i'):
            novo_estado = 'voi';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    if(estado_atual == 'voi'):
        if(proxcaracter == 'd'):
            novo_estado = 'void';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    if(estado_atual == 'void'):
        if(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'VOID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';


    #--------------------------------------------------------------------------#

    #------------------ESTADOS WHILE-------------------------------------------#

    if(estado_atual == 'wh'):
        if(proxcaracter == 'i'):
            novo_estado = 'whi';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    
    if(estado_atual == 'whi'):
        if(proxcaracter == 'l'):
            novo_estado = 'whil';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';

    if(estado_atual == 'whil'):
        if(proxcaracter == 'e'):
            novo_estado = 'while';
        elif(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'ID';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    if(estado_atual == 'while'):
        if(proxcaracter == ' ' or ( proxcaracter in simbolos) or proxcaracter == 'EOL'):
            token = 'WHILE';
            novo_estado = 'inicial';
        else:
            novo_estado = 'variavel';
    #--------------------------------------------------------------------------#

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
