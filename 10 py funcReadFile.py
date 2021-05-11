def readFile():
    
    f = open("tmp/myfile.txt", "r")
    texto = f.readlines()
    for linha in texto:
        print (linha)
    f.close()
    
def readFile2():
    
    f = open("tmp/myfile.txt", "r")
    texto = f.read()
    print (texto)
    f.close()
    

print ('hi! Reading file')
readFile()
print ('hi! Reading file2')
readFile2()
