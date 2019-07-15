#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Documentação
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

import matplotlib.pyplot as plt
import os
import sys
import csv
import pandas as pd
import numpy as np


# In[5]:


#Usando matplotlib
#ex:1
#indicando eixos
x=[1,3]
y=[2,4]


plt.plot(x,y) #função para plotar o grafico com os respectivos eixos
plt.show() #não é obrigatório mas melhora o código


# In[18]:


#Gráfico de Linhas
#Lembrando que toda função aqui tem que ser idetidade e injetora
x=[1,5,10,15]
y=[1,5,7,11]
plt.plot(x,y)
#Titulo do Gráfico
plt.title("Gráfico 01")
#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


# In[21]:


#Gráfico de barras

x=[1,5,10,15]
y=[1,5,7,11]
#Ao invez de plot usamos o bar
plt.bar(x,y)
#Titulo do Gráfico
plt.title("Gráfico 01")
#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


# In[25]:


#Gráfico de barras comparativo

#Primeiro Set
x=[1,2,3,4,5]
y=[5,6,7,8,9]

#Segundo Set
x1 = [2,4,6,8,10]
y1 = [3,7,9,11,15]

#Apenas vamos adicionando as medidas que ele plota tudo no mesmo gráfico
plt.bar(x,y, label = "Grupo 1" )
plt.bar(x1,y1, label = "Grupo 2")
#Titulo do Gráfico
plt.title("Gráfico 01")
#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
#Legendas
plt.legend()# Chamando os labels
plt.show()


# In[32]:


#Escater plot ou Gráfico de disperção 

x=[1,5,10,15]
y=[1,5,7,11]
x1 = [2,4,6,8,10]
y1 = [3,7,9,11,15]

#usar scatter 
plt.scatter(x,y, label = "Grupo 1")
plt.scatter(x1,y1, label = "Grupo 2")
#Titulo do Gráfico
plt.title("Gráfico 01")
#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend() # Chamando os labels


# In[76]:


#Ligando pontos (comportamento)

x=[1,5,10,15]
y=[1,5,7,11]
z = [2,3,4,8]
x1 = [2,4,6,8,10]
y1 = [3,7,9,11,15]
w = [11,15,16,19,25] 
tamanho = [100,100,3000,100] #posso customizar o tamanho de cada ponto individualmente

#usar scatter 
plt.scatter(x,y, label = "Grupo 1" , color = "red")#alterei as cores dos pontos
plt.scatter(x1,y1, label = "Grupo 2" , marker = "^" ,s = 150) #Rever tipos de marcadores (linha bola strela dentre varios outros )
plt.scatter(z,y, s = tamanho)
plt.plot(x,y)
plt.plot(w,linestyle = ":", color="K") #k igual a black, -- colocar linha tracejada entre outros

#Titulo do Gráfico
plt.title("Gráfico 01")
#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend() # Chamando os labels
#Atribuindo o grafico em uma variavel
grafico = plt.gcf()
plt.show()#chamando o Gráfico
plt.draw()#chamando o desenho
#Salvando a imagem 
#plt.savefig("C:/Users/Diego/Desktop/exemploGraf.png")
#ou melhor assim
grafico.savefig("C:/Users/Diego/Desktop/exemploGraf.png",dpi=100)#dpi = qualidade da imagem (impressao = dpi = 300)
#Salvando em pdf Alta resolução
grafico.savefig("C:/Users/Diego/Desktop/exemploGraf.pdf")#Se não declarar o caminho vai salvar na pasta sourcer


#marker = mudar os marcadores (dos pontos)
#color = cor dos marcadores ou da linha
#s = 150 tamanho do marcador
###Tambpem aceita cores hexadecimais do tipo color="#FF2569"


# In[25]:


#Exercicio: Fazendo um gráfico de barras para o grupo de dados
#foi necessário fazer um etl antes,a base estava em apenas uma coluna com ";" de separador
#esta em uma coluna df.columns

df = pd.read_csv("C:/Users/Diego/Downloads/populacao-brasileira.csv")
dfset = df['ano;population'] = df['ano;population'].str.split(';',n = 1,expand = True) #n = 1 é pra fazer o split uma vez
#Definindo a posição das colunas (do nome da coluna)
dfset["Ano"] = dfset[0]
dfset["População"] = dfset[1]
dfset
#Agora vamos tirar as colunas antigas
dfset.drop(columns =[0,1], inplace = True) 
#Retornando
dfset.head()#não tá mostrando tudo



# In[11]:


#Gráfico
#nessa coso é melhor usar o plotly ou fazer um parse das datas e agregar

x = dfset['Ano']
y = dfset['População']

plt.bar(x,y)
plt.show





# In[14]:


#Mesmo Gráfico de cima
#/Mas com o matlib precisa varrer os dados

dados = open("C:/Users/Diego/Downloads/populacao-brasileira.csv").readlines()

x= []
y= []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
                           
plt.plot(x,y) 
plt.title("CRescimento população Brasileira")
plt.xlabel("Ano")
plt.ylabel("população * 1x10^8")
plt.legend()
plt.show()


# In[4]:


#Mesmo Gráfico de cima
#/Mas com o matlib precisa varrer os dados

dados = open("C:/Users/Diego/Downloads/populacao-brasileira.csv").readlines()

x= []
y= []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
                           
plt.bar(x,y, color = "#e4e4e4") 
plt.plot(x,y, color = "black", linestyle="--")
plt.title("CRescimento população Brasileira")
plt.xlabel("Ano")
plt.ylabel("população * 1x10^8")
plt.show()


# In[9]:


#boxplot - Gerando dados aleatórios
# box plot é uma ferramenta gráfica para representar a variação de dados observados de uma variável numérica por meio de quartis 
#https://pt.wikipedia.org/wiki/Diagrama_de_caixa
#verificar distribuição e dados importantes esse é só um exemplo
import random
vetor = []
for i in range(100):
    numero_random = random.randint(0,50)
    vetor.append(numero_random)
plt.title("BoxPLot", color = "Red")    
plt.boxplot(vetor)    
plt.show()

