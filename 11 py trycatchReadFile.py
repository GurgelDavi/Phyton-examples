def FileCheck(fn):
    try:
      open(fn, "rb")
      return 1
    except IOError:
      print ("Error: File does not appear to exist.")
      return 0
def ReadFile(fn):
    if FileCheck(fn) :
        try:
            f = open(fn, "r")
            texto = f.readlines()
            for linha in texto:
                print (linha)
            f.close()
        except IOError: 
           print ("Error2: File does not appear to exist.")
    else :
        f = open(fn, "wb")
        texto = bytearray()
        texto.append(b'Lista de moradores:\n')
        texto.append(b'Davi Antunes \n')
        texto.append(b'Vanessaura \n')
        texto.append(b'Ivossauro\n')
        texto.append(b'Iagobert\n')
        f.write(texto)
        f.close()
        print('\n Arquivo criado')
        ReadFile(fn)
    return 0 
    

print ('hi! Reading file')
ReadFile("tmp/ListaTesteTrab.txt")

