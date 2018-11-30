import sys
import ply.lex
import ply.yacc

tokens = [  'STRING',
            'LPAREN',
            'RPAREN',
            'LBRACE',
            'RBRACE',
            'COLON',
            'COMMA',
            'INTEGER',
            'FLOAT',
            'ID',
            'MAYOR',
            'MENOR',
            'MAYORIGUAL',
            'MENORIGUAL',
            'IGUAL']

reserved = {
    'datos' : 'DATOS',
    'funcion' : 'FUNCION',
    'average' : 'AVERAGE',
    'sumIf' : 'SUMIF'

}
tokens += reserved.values()

t_ignore = ' \t'
t_LPAREN = '\('
t_LBRACE = '\{'
t_RBRACE = '\}'
t_RPAREN = '\)'
t_COLON = '\:'
t_COMMA = '\,'
t_MAYOR = '\>'
t_MENOR = '\<'
t_MAYORIGUAL = '\>='
t_MENORIGUAL = '\<='
t_IGUAL = '\=='


#tomado del proyecto:


def t_ID(t):
    r'[a-zA-Z]+[0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_FLOAT(t):
    r'(\-)?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'(\-)?\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
  r'\'[^\']*\''
  t.value = t.value[:-1]
  t.value = t.value[1:]
  return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
    print ('Illegal character at line: ' + str(t.lexer.lineno))
    t.lexer.skip(1)


lexer = ply.lex.lex()