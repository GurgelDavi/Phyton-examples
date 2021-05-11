while True:
    line = input('Digite algo e pressione Enter (p para terminar)>')
    if line == "p":
        print ("parando \n")
        break
    if line == '#' :
        continue #sem imprimir nada
    
    print (line)
print ('Finalizado')
input()
