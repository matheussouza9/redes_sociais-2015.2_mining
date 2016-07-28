'''

@author: Matheus
'''

from mydb import getAllTweets
from pony.orm.core import db_session

@db_session
def main():
    foracunha = open('../foracunha.dl', 'w')
    ficacunha = open('../ficacunha.dl', 'w')
    
    foracunha.write('DL n=5\nformat = edgelist1\nlabels embedded:\ndata:\n')
    ficacunha.write('DL n=5\nformat = edgelist1\nlabels embedded:\ndata:\n')
    
    lista_tts = getAllTweets()
    
    for tt in lista_tts:
        lista_palavras = tt.text.split()
        palavra = lista_palavras.pop()
        if lista_palavras != None:
            for p in lista_palavras:
                linha = '{0} {1}\n'.format(palavra, p)
                print(linha)
                    
                if tt.hashtag == 1:
                    foracunha.write(linha)
                else:
                    ficacunha.write(linha)
    
    foracunha.close()
    ficacunha.close()
if __name__ == '__main__':
    main()