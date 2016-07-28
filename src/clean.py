'''
@author: Matheus
'''

from palavras import palavras_adicionais
from nltk.corpus import stopwords
from unidecode import unidecode
from pony.orm import db_session
from mydb import getAllTweets
from pony.orm.core import CommitException
import re

stop_words = set(stopwords.words('portuguese') + palavras_adicionais + ['rt', 'via', 'cun', 'cunha'])

@db_session
def main():
    lista_tts = getAllTweets()
    for tt in lista_tts:
        # recebe tweet cru e transforma em minusculo
        texto = tt.text.lower()
        
        print(texto)
        
        tt.hashtag = 1 if '#foracunha' in texto else 2
        
        # retira pontuacao, mencoes, hashtags e (kkkkkk, hahaha, hehehe, affs)    retira acentos e espacos nas extremidades
        texto = re.sub(r'\B[@#]\S+\b|[^a-zA-Z]|k+|(ha|he)\S{2,}|a+f+(\s|$)', ' ', unidecode(texto)).strip()
        # remove espacos repetidos entre palavras
        texto = re.sub(r'\s+', ' ', texto)
        
        t = texto.split(' ')
        # remove stopwords
        for palavra in t[:]:
            if palavra in stop_words:                
                t.remove(palavra)
        
        # junta lista de palavras e as separa por espaco
        t = ' '.join(t)
        
        print('final:', t)
        
        # atualiza tweet na base de dados
        try:
            if t != '':
                tt.text = t
            else:
                tt.delete()
        except CommitException:
            pass

if __name__ == '__main__':
    main()