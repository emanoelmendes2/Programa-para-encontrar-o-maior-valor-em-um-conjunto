import time
inicio = time.time()

arq = open('dataset-2-e.csv', 'r')
texto = arq.readlines()
maior=-1
for i in texto:
    if maior==None:
        maior=int(i)
    elif maior<int(i):
        maior=int(i)
        
arq.close()
segundos = time.time()
milissegundos = segundos * 1000
arq1 = open('lista_maior-e.txt', 'w')
arq1.write(str(maior)+'\n'+str(milissegundos))
arq1.close()
