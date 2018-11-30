import sys
import pprint
import ply.yacc

from lexer import tokens
from lexer import reserved


symbol_table = {}
lista = []
listaGeneral = [] 


def generarCodigo():
  cod = "no sé :("
  #fuente: https://chortle.ccsu.edu/AssemblyTutorial/Chapter-22/ass22_5.html
  '''cod = "\r .text\n"
  cod += "\r.globl  main \n"
  cod += "main:\n"
  cod += "\r li      $v0,4  \n"
  cod += "\r la      $a0,string\n"
  cod += "\r syscall \n"
  cod += "\r li      $v0,10 \n"
  cod += "\r syscall \n"
  cod += "\r .data \n"
  cod += 'string: .asciiz      "Hello SPIM!"'''


  file = open('output.s', 'w')
  file.write(cod)
  file.close()
#-----------------------------------------------------------------
def llenarTabla():
  global lista
  global symbol_table
  lA = []
  lB = []
  lC = []
  lD = []
  lE = []
  for i in range(25):
    sub = i%5
    if(sub == 0):
      lA.append(lista[0][i])
    elif(sub == 1):
      lB.append(lista[0][i])
    elif(sub == 2):
      lC.append(lista[0][i])
    elif(sub == 3):
      lD.append(lista[0][i])
    else:
      lE.append(lista[0][i])

  symbol_table["A"] = lA
  symbol_table["B"] = lB
  symbol_table["C"] = lC
  symbol_table["D"] = lD
  symbol_table["E"] = lE
  
  #print("Symbol Table Filled")
  #print(symbol_table)
#-------------------------------------------------------------
def getType(a):
  if(type(a) == type(3)):
    return "int"
  elif(type(a) == type(3.2)):
    return "double"
  elif(type(a) == type("str")):
    return "string"
#-------------------------------------------------------------
def analisisSematico():
  global listaGeneral
  global symbol_table
  #la funcion está en listaGeneral[3][0]
  #print(listaGeneral[3])
  if(listaGeneral[3][0] == "average"):
    if(len(listaGeneral[3][1]) == 2): #rango o (rango + numeros)
      r1 = listaGeneral[3][1][0][0]
      r2 = listaGeneral[3][1][0][3]
      if(r1 != r2):
        print("Error! Rango no válido")
        sys.exit()
      else:
        prom = 0
        n = 0
        for i in range(int(listaGeneral[3][1][0][1]),int(listaGeneral[3][1][0][4])+1):
          #print(symbol_table[r1][i])
          if(type(symbol_table[r1][i]) == type("str")):
            print("Error! Hay una letra o palabra dentro de ese rango")
            sys.exit()
          else:
            prom += symbol_table[r1][i]
            n+=1
        if(len(listaGeneral[3][1][1])>0):
            l = 0
            while(l<len(listaGeneral[3][1][1])):
              prom +=listaGeneral[3][1][1][l]
              l +=1
              n +=1
        prom = prom/(n)
        print(prom)
    else: #solo numeros
      prom = 0
      n = 0
      while(n < len(listaGeneral[3][1])):
        prom += listaGeneral[3][1][n]
        n +=1
      prom = prom/n
      print(prom)

  else: # sumIF
    if(len(listaGeneral[3][1]) == 2): #rango o (rango + numeros)
      r1 = listaGeneral[3][1][0][0]
      r2 = listaGeneral[3][1][0][3]
      if(r1 != r2):
        print("Error! Rango no válido")
        sys.exit()
      else:
        suma = 0
        for i in range(int(listaGeneral[3][1][0][1]),int(listaGeneral[3][1][0][4])+1):
          #print(symbol_table[r1][i])
          if(type(symbol_table[r1][i]) == type("str")):
            print("Error! Hay una letra o palabra dentro de ese rango")
            sys.exit()
          else:
            comparador = listaGeneral[3][2][0]
            if(comparador == ">"):
              if(symbol_table[r1][i] > listaGeneral[3][2][1]):
                suma += symbol_table[r1][i]
            elif(comparador == ">="):
              if(symbol_table[r1][i] >= listaGeneral[3][2][1]):
                suma += symbol_table[r1][i]
            elif(comparador == "<"):
              if(symbol_table[r1][i] < listaGeneral[3][2][1]):
                suma += symbol_table[r1][i]
            elif(comparador == "<="):
              if(symbol_table[r1][i] <= listaGeneral[3][2][1]):
                suma += symbol_table[r1][i]
            elif(comparador == "=="):
              if(symbol_table[r1][i] == listaGeneral[3][2][1]):
                suma += symbol_table[r1][i]
        n = 0
        #print(listaGeneral[3][1][1])
        while(n < len(listaGeneral[3][1][1])):
          if(comparador == ">"):
              if(listaGeneral[3][1][1][n] > listaGeneral[3][2][1]):
                suma += listaGeneral[3][1][1][n]
          elif(comparador == ">="):
              if(listaGeneral[3][1][1][n] >= listaGeneral[3][2][1]):
                suma += listaGeneral[3][1][1][n]
          elif(comparador == "<"):
              if(listaGeneral[3][1][1][n] < listaGeneral[3][2][1]):  
                suma += listaGeneral[3][1][1][n]
          elif(comparador == "<="):
              if(listaGeneral[3][1][1][n] <= listaGeneral[3][2][1]):
                suma += listaGeneral[3][1][1][n]
          elif(comparador == "=="):
              if(listaGeneral[3][1][1][n] == listaGeneral[3][2][1]):
                suma += listaGeneral[3][1][1][n]
          n += 1 
        print(suma)
    else: #solo numeros
      comparador = listaGeneral[3][2][0]
      suma = 0
      #print(listaGeneral[3][1])
      n = 0
      while(n<len(listaGeneral[3][1])):
        if(comparador == ">"):
          if(listaGeneral[3][1][n] > listaGeneral[3][2][1]):
            suma += listaGeneral[3][1][n]
        elif(comparador == ">="):
          if(listaGeneral[3][1][n] >= listaGeneral[3][2][1]):
            suma += listaGeneral[3][1][n]
        elif(comparador == "<"):
          if(listaGeneral[3][1][n] < listaGeneral[3][2][1]):  
            suma += listaGeneral[3][1][n]
        elif(comparador == "<="):
          if(listaGeneral[3][1][n] <= listaGeneral[3][2][1]):
            suma += listaGeneral[3][1][n]
        elif(comparador == "=="):
          if(listaGeneral[3][1][n] == listaGeneral[3][2][1]):
            suma += listaGeneral[3][1][n]
        n += 1 
      print(suma)



#-------------------------------------------------------------
def p_begin(p):
  ''' begin : DATOS LBRACE blockData RBRACE FUNCION LBRACE fn RBRACE
  '''
  #p[3] BloqueDat, p[7] funcion+params, 
  p[0] = ['datos',p[3],p[5],p[7]]
  global listaGeneral
  listaGeneral = p[0]
  #pp.pprint(listaGeneral)
  return p[0]
#-------------------------------------------------------------------

def p_blockData(p):
  ''' blockData : dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato dato
  '''
  p[0] = [p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],p[16],p[17],p[18],p[19],p[20],p[21],p[22],p[23],p[24],p[25]]
  global lista 
  lista.append(p[0])
  #print(lista)
  return p[0]

#-------------------------------------------------------------------------------

def p_dato(p):
  ''' dato : INTEGER
           | FLOAT
           | ID
  '''
  p[0] = p[1]
  return p[0]
#-------------------------------------------------------------------

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
  ''' rango : ID COLON ID moreNums
  '''
  if(p[4] == ''):
    p[1] += p[2]
    p[1] += p[3]
    p[0] = p[1]
  else:
    p[1] += p[2]
    p[1] += p[3]
    p[0] = [p[1],p[4]]
  return p[0]
#-------------------------------------------------------------------------------
def p_nums(p):
  ''' nums : INTEGER moreNums
           | FLOAT moreNums
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
  ''' condition : comp INTEGER
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
  #Tomado del proyecto
def p_epsilon(p):
  ''' epsilon : '''
  p[0] = ''
  return p[0]
  #Tomado del proyecto
#-------------------------------------------------------------------------------
  #Tomado del proyecto
def p_error(p):
  if p is not None:
    print("Syntax error at: \"" + str(p.value) + "\" line: " + str(p.lineno))
    sys.exit()
    #parser.errok()
  else:
    print("End of file")

#-----------------------------------------------------------------------------------

start = 'begin'

filename = sys.argv[1]

parser = ply.yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)

with open(filename, 'r') as f:
  input = f.read()
  #pp.pprint(parser.parse(input))
  parser.parse(input)
  #print("Compiled completed successfully!")
  llenarTabla() 
  analisisSematico()
  generarCodigo()
  

#----------------------------------------------------------------
 # EJECUTAR MARS java -jar Mars.jar 
