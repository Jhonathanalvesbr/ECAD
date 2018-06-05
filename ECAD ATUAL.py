import string
entrada = open('C:\Jhonathan\musicas.txt', 'r')
saida = open('C:\Jhonathan\planilha.xls', 'w')
arquivo = entrada.readlines()
i = 0
data = []
d = 0
cantor = []
tab = '\t'
frase = []
m = 0
cantor = 0
musica = 0
compositor = 0
cortador = []
contador = ''
count = 1
while (len(arquivo) > i):
    if (len(arquivo[i]) > 3):
        arquivo[i] = arquivo[i].upper() 
        if (string.find(arquivo[i],'201') > -1):
            data.append(arquivo[i])
            data[d] = data[d].replace(' - ','/').replace('\n','')
            arquivo[i] = data[d]
            d += 1
        if (arquivo[i] != '\n' and (arquivo[i] != '---------------------------------------------------\n')):
            arquivo[i] = arquivo[i].replace(' ./. ',tab).replace(' /./ ',tab).replace('\n','')
            frase.append(arquivo[i])
            if (frase[m].count(tab) == 2):
                contador = str(count)
                count += 1
                cortador = frase[m].split(tab)
                cantor,musica,compositor = cortador
                saida.write('BALANÇO GERAL'+tab+data[d-1]+tab+tab+tab+tab+tab+tab+tab+tab+musica+tab+'BIBLIOTECA MUSICAL'+tab+compositor+tab+cantor+tab+tab+tab+tab+tab+tab+tab+'AO VIVO'+'\n')
            elif (frase[m].count(tab) == 0 and data[d-1] != frase[m]):
                contador = str(count)
                count += 1
                saida.write(contador+tab+data[d-1]+tab+frase[m]+'\n')
                saida.write('BALANÇO GERAL'+tab+data[d-1]+tab+tab+tab+tab+tab+tab+tab+tab+tab+tab+'BIBLIOTECA MUSICAL'+tab+tab+tab+frase[m]+tab+tab+tab+tab+tab+tab+'AO VIVO'+'\n')
            elif (data[d-1] != frase[m]):
                contador = str(count)
                count += 1
                cortador = frase[m].split(tab)
                cantor,musica = cortador
                saida.write('BALANÇO GERAL'+tab+data[d-1]+tab+tab+tab+tab+tab+tab+tab+tab+musica+tab+'BIBLIOTECA MUSICAL'+tab+tab+cantor+tab+tab+tab+tab+tab+tab+tab+'AO VIVO'+'\n')
            m += 1

        
    i += 1
entrada.close()
saida.close()
