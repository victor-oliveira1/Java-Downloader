#!/bin/python3
from os import remove, access
from urllib.request import urlretrieve, urlopen
from re import findall

def progresso_download(block, read, total):
    porcentagem = round(block * read / total * 100)
    print('{}% - {}Kb de {}Kb'.format(porcentagem, block * read, total), end='\r')

url = 'https://www.java.com/pt_BR/download/manual.jsp'

html = urlopen(url).read().decode()

url_down = findall('Windows Off-line.*', html)[0]
url_down = findall('http://.*', url_down)[0]
url_down = url_down.split('"')[0]

nome_java = urlopen(url_down).url
nome_java = findall('jre[-\w\.]+', nome_java)[0]

if access(nome_java, 0) == True:
	print('Arquivo: {} já existe!'.format(nome_java))
	exit()

try:
    print('Fazendo download do arquivo: {}'.format(nome_java))
    urlretrieve(url_down, nome_java, progresso_download)
except:
    print('\nCancelando download e apagando arquivo...')
    remove(nome_java)
