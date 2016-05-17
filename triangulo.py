print ("indique (1) para triangulo o (2) para cuadrado")
num= input ()
num= int (num) 
        
def triangulo (B,H):

    area = ((B*H)/2)
    return area

def cuadrado (N):
    area1 = (N**2)
    return area1

if num ==1:
    
    print ("diga la base")
    b= input ()
    b= int(b)
    print ("diga la altura")
    h= input ()
    h= int (h)

    print ("el area es:" , triangulo(b,h))
    
elif num==2:
        
    print ("indique uno de sus lados")
    n= input ()
    n= int (n)
    print ("el area es: " ,cuadrado(n))

else:
    print ("el numero ingresdo es incorrecto")




