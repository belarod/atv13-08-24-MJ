import re

def buscar_ingr():
    ingredientes = input('Digite alguns ingredientes:').lower()
    ingr_clean = re.sub(",", "", ingredientes).split()
    
    termo = input('Digite algum ingrediente:').split()
    for x in ingr_clean:
        for y in termo:
            if x == y:
                print('O ingrediente {} está na lista.'.format(y))
    

buscar_ingr()