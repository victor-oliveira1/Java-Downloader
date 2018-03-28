#!/bin/python3
#victor.oliveira@gmx.com
from urllib.request import urlopen
from html.parser import HTMLParser
from re import findall

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.java = dict()
    def handle_starttag(self, tag, attrib):
        try:
            if 'title' in attrib[0][0]:
                if 'download' in attrib[0][1]:
                    java_title = attrib[0][1]
                    java_url = attrib[1][1]
                    self.java.update({java_title : java_url})
        except IndexError:
            pass

def DownloadJava(numero):
    buffer = 1000
    url = versoes[numero][1]
    req = urlopen(url)
    tamanho = req.length
    nome = findall('jre[-\w\.]+', req.url)[0]
    print('Realizando o download do arquivo:', nome)
    print('Tamanho:', '{:.2f}MB'.format(tamanho / 1000 / 1000))
    with open(nome, 'wb') as arquivo:
        c = 0
        while True:
            tmp = req.read(buffer)
            if tmp:
                arquivo.write(tmp)
                c += 1
                print('{:.1f}%'.format((c * buffer / tamanho) * 100), end='\r')
            else:
                break
        print()

url = 'https://www.java.com/pt_BR/download/manual.jsp'
download_page = urlopen(url).read().decode()
html_parser = MyHTMLParser()
html_parser.feed(download_page)
versoes = list(html_parser.java.items())
print('== Java Downloader ==')
print()
print('Escolha a ação desejada:')
n = 0
for java in versoes:
    print('{}- {}'.format(n, java[0]))
    n+=1
try:
    escolha = int(input('> '))
    DownloadJava(escolha)
except ValueError:
    print('Não é uma escolha válida!')
