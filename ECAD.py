import string
py = open('C:\Jhonathan\musicas.txt', 'r')
pyy = open('C:\Jhonathan\planilha.xls', 'w')
contador = 1
contadorstr = ''
tab = '\t'
for line in py:
    contadorstr = str(contador)
    l = line.replace('./.', tab).replace('/./', tab).replace('---------------------------------------------------', '')
    if (string.find(l,'2016') and len(l) == 15):
        abc = l
    elif (string.find(l,'2017') and len(l) == 15):
        abc = l
    if ((len(l) > 4) and (abc != l)):
        l = l.upper()
        pyy.write(contadorstr+tab+abc[0:14]+tab+l)
        print(contadorstr+tab+abc[0:14]+tab+l)
        contador += 1
py.close()
pyy.close()
