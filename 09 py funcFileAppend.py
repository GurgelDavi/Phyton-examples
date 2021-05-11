def appendFile():
    f = open("tmp/myfile.txt", "a")
    texto=[]
    texto.append('teste')
    f.writelines(texto)
    f.close
    
print ('hi!reading file')
appendFile()
