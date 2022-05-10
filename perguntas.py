endereco = r"C:\Users\Daniel\Desktop\txts\perguntas raw.txt"
perg1 = []
n = 0
nn = 0
pergunta = None

arquivo = open(endereco, 'r')
for c in arquivo:
    if n < 6:
        if c != '\n':
            if n == 2:
                perg1.append(c)
                perg1.append('\n')
            if n == 3:
                perg1.append(c)
                perg1.append('\n')
            if n == 4:
                perg1.append(c)
            if n == 5:
                perg1.append('\n')
                perg1.append(c)
        else:
            n += 1
    else:
        nn += 1
        pergunta = open(f'pergunta{nn}.txt', 'w')
        for cc in perg1:
            pergunta.write(cc)
        pergunta.close()
        n = 0
        perg1.clear()

arquivo.close()
