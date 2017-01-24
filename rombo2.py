import sys

def es_par(numero):
    return (numero % 2 == 0)

def dibujar_rombo(lineas):
    lineas = int(lineas)
    if es_par(lineas):
        print ('El numero de lineas es par, no puedo escribir un rombo perfecto')
    else:
        espacios = int(lineas / 2)
        disminuyo = False
        cantidad = 1
        stra = ''
        for i in xrange(lineas):
            for n in xrange(espacios):
                stra += ' '
            for n in xrange(cantidad):
                stra += '*'
            print (stra)
            if len(stra) == lineas:
                disminuyo = True
            if disminuyo:
                cantidad -= 2
                espacios += 1
            else:
                cantidad += 2
                espacios -= 1
            stra = ''
if __name__ == '__main__':
    #dibujar_rombo(sys.argv[1])
    dibujar_rombo(9)
