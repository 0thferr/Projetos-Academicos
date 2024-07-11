...
200011735 Daniel Evanio 
200011514 Thais Ferreira
...

arq = open("integrantes_familia.txt","r")

while True:
    line = arq.readline()
    if not line:
        break
    print(line)

arq.close()