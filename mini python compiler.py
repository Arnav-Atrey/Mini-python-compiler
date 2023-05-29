import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'NAME', 'NUMBER','COMMA', 'COLON', 'QUOTE',
    'MINUS', 'TIMES', 'DIVIDE','MOD',
    'LPAREN', 'RPAREN','INDENT',
    'DOT', 'PLUS','EQUALS','NEWLINE'
]

t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_COLON = r':'
t_DOT = r'\.'
t_PLUS = r'\+'
t_QUOTE = r'\''
t_EQUALS = r'\='
t_NEWLINE = r'\n'
t_INDENT = r'\t'

reserved = {
    'with': 'WITH',
    'open': 'OPEN',
    'as': 'AS',
    'txt': 'TXT',
    'r': 'R',
    'a': 'A',
    'w': 'W',
    'lambda':'LAMBDA',
    'def':'DEF',
    'try':'TRY',
    'except':'EXCEPT',
    'return': 'RETURN',
    'for': 'FOR',
    'close':'CLOSE',
    'in' : 'IN',
    'range' : 'RANGE'
}

tokens = tokens + list(reserved.values())

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " "

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    # t.lexer.skip(1)
    exit(1)

lexer = lex.lex()

# lexer.input(s)
# for tok in lexer:
#     print(tok)

def p_main(p):
    '''main : def_func
            | lambada
            | Txt
            | try_except
            | for'''
    print("Input accepted!\n")

def  p_for(p):
    '''for : FOR NAME IN RANGE LPAREN tuple RPAREN COLON statement'''

def p_TUPLE(p):
    '''tuple : NUMBER
            | NUMBER COMMA NUMBER
            | NUMBER COMMA NUMBER COMMA NUMBER'''

def p_LAMBADA(p):
    '''lambada : LAMBDA names COLON statement'''

def p_FUNC(p):
    '''def_func : DEF NAME LPAREN names RPAREN COLON statement NEWLINE INDENT RETURN NAME'''

def p_NAMES(p):
    '''names : NAME COMMA names
             | NAME'''

def p_TE(p):
    '''try_except : TRY COLON statement EXCEPT COLON statement'''

def p_TXT(p):
    '''Txt : NAME EQUALS OPEN LPAREN QUOTE NAME DOT TXT QUOTE COMMA QUOTE mode QUOTE RPAREN NEWLINE cls
            | WITH OPEN LPAREN QUOTE NAME DOT TXT QUOTE COMMA QUOTE mode QUOTE RPAREN AS NAME COLON
            | WITH OPEN LPAREN QUOTE NAME DOT TXT QUOTE COMMA QUOTE mode QUOTE RPAREN COLON'''

def p_CLOSE(p):
    '''cls : NAME DOT CLOSE LPAREN RPAREN'''

def p_mode(p): 
    '''mode : R
            | W
            | A
            | R PLUS
            | W PLUS
            | A PLUS'''

def p_statement_assign(p):
    '''statement : NAME EQUALS statement
                 | statement PLUS statement
                 | statement PLUS EQUALS statement
                 | statement MINUS statement
                 | statement TIMES statement
                 | statement DIVIDE statement
                 | statement MOD statement
                 | LPAREN statement RPAREN
                 | NUMBER
                 | NEWLINE statement
                 | NEWLINE INDENT statement
                 | NAME
                 | '''

def p_error(p):
    print("Input not accepted!\n")
    exit(1)


yacc.yacc()

#s = '''def func(b): \n\t b+=8 \n\t return b'''
#s = '''with open('emp.txt','r'):'''
#s = '''for i in range(0,6):\n \t i+=1'''
#s = '''lambda x,y: x+y'''
s = '''try: x=5 exept: \n \t x=6'''
yacc.parse(s)