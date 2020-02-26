from datetime import datetime
from time import gmtime, strftime

def serious(f):
    def mostrar(): 
        arquivo = open(r'logs/arq'+ strftime("D%Y-%m-%dT%H.%M.%S", gmtime())+'.txt', 'w', encoding="utf8")
        arquivo.write('Função: ' + f.__name__ + ' : ' + str(datetime.now()))
        arquivo.close()

        return f()
    return mostrar