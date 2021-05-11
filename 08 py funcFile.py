def createFile():
    f = open("tmp/myfile.txt", "w")
    texto = []
    texto.append('Lista de moradores:\n')
    texto.append('Davi Antunes \n')
    texto.append('Vanessaura \n')
    texto.append('Ivossauro\n')
    texto.append('Iagobert\n')
    f.writelines(texto)
    print(f)
    f.close()
    input('\n Arquivo criado')
print ('hi! creating file')
createFile()
