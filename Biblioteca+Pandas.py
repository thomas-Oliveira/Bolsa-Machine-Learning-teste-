
# coding: utf-8

# O pandas é um pacote Python que fornece estruturas de dados rápidas, flexíveis e expressivas, projetadas para tornar o trabalho com dados “relacionais” ou “rotulados” fáceis e intuitivos. 
# Fácil manuseio de dados perdidos (representados como NaN) em ponto flutuante, bem como dados de ponto não flutuante
# Mutabilidade de tamanho: colunas podem ser inseridas e excluídas do DataFrame e objetos dimensionais maiores
# Alinhamento de dados automático e explícito : os objetos podem ser explicitamente alinhados a um conjunto de rótulos, ou o usuário pode simplesmente ignorar os rótulos e deixar que o Series , o DataFrame , etc. automaticamente alinhem os dados para você em cálculos
# Ferramentas de E / S robustas para carregar dados de arquivos simples (CSV e delimitados), arquivos do Excel, bancos de dados e salvamento / carregamento de dados a partir do formato HDF5 ultra- rápido
# 
# As duas estruturas primárias do pandas é as  séries e os DataFrames. Série é um array de uma dimensão e o DataFrame é como uma matriz, tem linhas e colunas
# 

# In[138]:


import pandas as pd
import numpy as np


# Geralmente temos uma tabela com todas os dados que vão servir para treinar o modelo e assim ele “aprender” a reconhecer novas entradas. 
# 
# Para ler tabelas em arquivos CSV usasse o .read_csv(arquivo.csv, names= nomes das colunas) 
# 
# !Existem mais parametros, mas para esse exemplo vamos mostrar apenas esses.
# 
# !Lembrando que esse arquivo tem que estar na mesma pasta onde você esta desenvolvendo o algoritmo
# 

# In[139]:


nomesColunas = ['sepal_comprimento','sepal_largura','petal_comprimento',
           'petal_largura','tipo']
df = pd.read_csv('iris.csv', names=nomesColunas)


# In[140]:


df.head(10) #.head(n) retorna as n primeiras linhas


# In[141]:


df.shape #.shape retorna uma tupla com as dimensoes do df


# In[142]:


#.loc[] mostra as informaçãoes que contem os rótulos passados.
df.loc[(df['tipo'] == "Iris-setosa") & (df['petal_comprimento'] == 1.4)]


# In[143]:


#pode-se fazer assim também, que não mostra todas as informações
df.loc[(df['tipo'] == "Iris-setosa") & (df['petal_comprimento'] == 1.4) , ['tipo', 'petal_comprimento']]


# .drop(labels = None, axis = 0, columns = None) onde 
#     
#     - labels é o indice ou o nome que quer excluir
#     - axis = 0 exclui rótulos que correspondem aquele label e = 1 exclui a coluna que corresponde aquele label
#     - columns é as colunas que quer excluir ex: df.drop(columns = [ 'B' ,  'C' ])
# 
#     
# ! Lembrando que existem mais parametro nessa função    

# In[144]:


df = df.drop('tipo', axis=1) 
df.head(10)


# In[145]:


df.min() #.min() retorna o menor valor do df


# In[146]:


df.max() #.max() retorna o maior valor do df


# In[147]:


#.describe() retorna resumo estatístico
df.describe() 

