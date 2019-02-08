#programinha pra facilitar meus commmits
import os
if os.system('git add .') == 0:
    print('files added')
    #as aspas duplas dentro das aspas simples
    # sao para indicar para o os, que o input é uma string
    messenge = input('Insira o comment:')
    if os.system('git commit --m "{}"'.format(messenge)) == 0:
        print('files commited')
    else:
        print('failed to commit files')
    os.system('git push')
else:
    print('failed to add files')


