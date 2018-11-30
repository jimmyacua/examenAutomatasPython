import sys
import pprint
import ply.yacc

from lexer import tokens
from lexer import reserved


symbol_table = {}
lista = []

def p_begin(p):
  ''' begin : DATOS LBRACE blockData RBRACE FUNCION LBRACE fn RBRACE
  '''
  #p[3] BloqueDat, p[7] funcion+params, 
  p[0] = ['datos',p[3],p[5],p[7]]
  return p[0]
#-------------------------------------------------------------------

def p_blockData(p):
  ''' blockData : ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID ID
  '''
  p[0] = [p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],p[24],p[25]]
  return p[0]

#-------------------------------------------------------------------------------
def p_fn(p):
  ''' fn : avg
         | sum
  '''
  p[0] = p[1]
  return p[0]

#-------------------------------------------------------------------------------
def p_avg(p):
   ''' avg : AVERAGE LPAREN params RPAREN
   '''
   p[0] = ['average', p[3]]
   return p[0]
#-------------------------------------------------------------------------------
def p_sum(p):
  ''' sum : SUMIF LPAREN params condition RPAREN
  '''
  p[0] = ['sumIf', p[3],p[4]]
  return p[0]
#-------------------------------------------------------------------------------

def p_params(p):
  ''' params : rango
             | nums
  '''
  p[0] = p[1]
  return p[0]

#-------------------------------------------------------------------------------
def p_rango(p):
  ''' rango : ID COLON ID
  '''
  p[1] += p[2]
  p[1] += p[3]
  p[0] = p[1]
  return p[0]
#-------------------------------------------------------------------------------
def p_nums(p):
  ''' nums : ID moreNums
  '''
  p[0] = [p[1]] + p[2]
  return p[0]
#-------------------------------------------------------------------------------

def p_moreNums(p):
  ''' moreNums : COMMA nums
               | epsilon
  '''
  if(len(p) > 2):
      p[0] = p[2]
  else:
    p[0] = []
  return p[0]

#-------------------------------------------------------------------------------
def p_condition(p):
  ''' condition : comp ID
  '''
  p[0] = [p[1],p[2]]
  return p[0]

#-------------------------------------------------------------------------------
def p_comp(p):
  ''' comp : MAYOR
           | MENOR
           | MAYORIGUAL
           | MENORIGUAL
           | IGUAL
  '''
  p[0] = p[1]
  return p[0]
#-------------------------------------------------------------------------------
def p_epsilon(p):
  ''' epsilon : '''
  p[0] = ''
  return p[0]
#-------------------------------------------------------------------------------
def p_error(p):
  if p is not None:
    print("Syntax error at: \"" + str(p.value) + "\" line: " + str(p.lineno))
    sys.exit()
    #parser.errok()
  else:
    print("End of file")



start = 'begin'

filename = sys.argv[1]

parser = ply.yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)

with open(filename, 'r') as f:
  input = f.read()
  pp.pprint(parser.parse(input))
  parser.parse(input)
  #llenar tabla
  #analizar semantica
  #generar codigo
  #print("ANALISIS COMPLETADO PERRO\n")

#----------------------------------------------------------------
  ##saber el tipo de variable
#a = "a"
#if(type(a) == type(3)):
#    print ('int')
#elif(type(a) == type(3.2)):
#    print ("double")
#else:
 #   print("nada")