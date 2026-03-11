
"""
NOMBRE : CALCULADORA
ENTRADA : OPERACION, op1, op2
SALIDA : RESULTADO
restrcciones: numeros enteros y operacion de 1 a 4

"""

def calculadora(operacion, op1, op2):
    if  not (isinstance(op1, int)) or not (isinstance(op2, int)) or not  (isinstance(operacion, int)):
        return  "Ingrese un numero"
    elif operacion < 0 or  op1 < 0 or op2 < 0:
        return "deben ser mayores a 0"
    elif operacion < 1 or operacion > 4 :
        return False, "debe ser de uno a 4 operacion"
def calculadora_Aux(operacion, op1, op2):
    if (operacion == 1):
        print(op1 + op2)
    elif (operacion == 2):
        print(op1 - op2)
    elif (operacion == 3):
        print(op1 * op2)
    elif (operacion == 4):
        print(op1 // op2)
        
