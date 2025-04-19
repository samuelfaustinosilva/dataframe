#!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd


# #### Criando DataFrames

# In[104]:


df1 = pd.DataFrame()


# In[105]:


df1


# In[106]:


type(df1)


# In[107]:


# Olhá só como foi importante aprender sobre dicionários 

dict1= {'identificação': [1,2,3,4,5],
       'nome': ['Sandra', 'Sebastião','Samuel', 'Ismeria', 'Hinata']}


# In[108]:


dict1


# In[109]:


df2 = pd.DataFrame(data = dict1, index = [1,2,3,4,5])


# In[110]:


df2


# In[111]:


serie1 = pd.Series([1,2,3])


# In[112]:


serie1


# In[113]:


type(serie1)


# In[114]:


serie2 = pd.Series(['a','b','c'])


# In[115]:


df4 = pd.DataFrame({'coluna1': serie1,
                   'coluna2': serie2})


# In[116]:


df4


# In[117]:


import numpy as np


# In[118]:


array1 = np.array([[1,2,3,],
                  ['São Paulo', 'Rio de Janeiro', 'Minas Gerias'],
                  ['SP', 'RJ', 'MG']])


# In[119]:


array1


# In[120]:


type(array1)


# In[121]:


df5 = pd.DataFrame(data= array1.transpose(),
                  index = ['linha1', 'linha2', 'linha3'],
                  columns = ['Identificação', 'Cidade', 'Estado'])


# In[122]:


df5


# In[123]:


matriz1 = np.matrix([[1,2,3,],
                  ['São Paulo', 'Rio de Janeiro', 'Minas Gerias'],
                  ['SP', 'RJ', 'MG']])


# In[124]:


type(matriz1)


# In[125]:


matriz1


# In[126]:


df6 = pd.DataFrame(data= matriz1.transpose(),
                  index = ['linha1', 'linha2', 'linha3'],
                  columns = ['Identificação', 'Cidade', 'Estado'])


# In[127]:


df6


# ### Selecionando DataFrames

# In[128]:


df2


# In[129]:


df2['identificação_mais_5'] = df2['identificação'] + 5


# In[130]:


df2


# In[131]:


df2['index'] = 0


# In[132]:


df2


# In[133]:


df2['nome']


# In[134]:


df2.nome


# In[135]:


df2.index


# In[136]:


df2[['nome', 'index']]


# In[137]:


df2[df2.identificação % 2 == 0 ]


# In[138]:


df2[df2.nome.str.contains('r')]


# In[139]:


df2[df2.nome.str.contains('r') & df2.identificação ==1]


# In[140]:


df2[df2.nome.str.contains('r') | df2.identificação == 4]


# - loc: localizar pelo NOME dos índices ou colunas
# - iloc: localizar pela POSIÇÃO dos índices ou colunas

# In[141]:


df2


# In[142]:


df2.loc[1]


# In[143]:


df2.iloc[1]


# In[144]:


df2.loc[1:5]


# In[145]:


df2.iloc[1:5]


# In[146]:


df2.loc[5:1:-1]


# In[147]:


df2


# In[148]:


df2.loc[:,'nome']


# In[149]:


df2.iloc[:,1]


# In[150]:


df2.loc[2,'nome']


# In[151]:


df2.iloc[3,1]


# In[152]:


df2.loc[2,'nome'] = 'Tiãozinho'


# In[153]:


df2


# In[154]:


df2.iloc[-1]


# In[155]:


df2.iloc[-1,-2]


# In[156]:


df2


# In[157]:


df2.loc[[1,2]]


# In[158]:


df2.iloc[[1,2]]


# ### Atributos de DataFrame 

# In[159]:


df2


# In[160]:


df2.dtypes


# In[161]:


df2.identificação = df2.identificação.astype(str)


# In[162]:


df2.dtypes


# In[163]:


df2['Teste'] = [None, 2, 4, None, 10]


# In[164]:


df2


# In[165]:


df2.dtypes


# In[166]:


df2.columns


# In[167]:


df2.columns = ['identificação', 'nome', 'identificação_mais_5', 'index_MODIFICADO', 'Teste']


# In[168]:


df2


# In[169]:


df2.index


# In[170]:


df2.shape


# In[171]:


df2.values


# ### Métodos I

# #### combine_first

# In[172]:


df2


# In[173]:


df2.Teste.combine_first(df2['identificação_mais_5'])


# #### copy

# In[174]:


df100 = df2.copy()


# In[175]:


df100


# In[176]:


#### count


# In[177]:


df100.count()


# #### drop

# In[178]:


df2


# In[179]:


df2.drop(columns =['index_MODIFICADO'])


# In[180]:


df2


# In[183]:


df2 = df2.drop(columns =['index_MODIFICADO'])


# In[182]:


df2.drop(columns = ['index_MODIFICADO'], inplace=True)


# In[185]:


df2.drop(index = [1], inplace=True)


# In[186]:


df2


# #### drop_duplicates

# In[189]:


df7 = pd.concat([df100, df100])


# In[190]:


df7


# In[191]:


df7.drop_duplicates(inplace=True)


# In[192]:


df7


# #### dropna

# In[193]:


df8 = df7.copy()


# In[194]:


df8


# In[196]:


df8.dropna(inplace=True)


# In[197]:


df8


# #### fillna

# In[198]:


df7


# In[199]:


df7.fillna('Nulo', inplace=True)


# In[200]:


df7


# #### head

# In[202]:


df7.head(2)


# #### tail

# In[203]:


df7.tail(2)


# #### groupby

# In[204]:


df10 = pd.concat([df100, df100])


# In[205]:


df10


# In[206]:


df10.groupby(['nome']).identificação_mais_5.sum()


# ### Módulos II

# In[207]:


df2


# #### isin

# In[208]:


df2.isin([2,4])


# In[210]:


df2.isin(['2','4'])


# In[212]:


df2[df2.isin(['2','4']) == True]


# In[213]:


df2[df2.identificação.isin(['2','4']) == True]


# In[214]:


df2[df2.Teste.isin([2, 4]) == True]


# #### operações

# In[215]:


df2


# In[216]:


df2.identificação_mais_5.min()


# In[217]:


df2.identificação_mais_5.max()


# In[218]:


df2.identificação_mais_5.mean()


# In[219]:


df2.identificação_mais_5.median()


# In[220]:


df2.identificação_mais_5.sum()


# In[221]:


df2.identificação_mais_5.std()


# #### notnull

# In[222]:


df2


# In[223]:


df2.Teste.notnull()


# In[224]:


df2[df2.Teste.notnull() == True]


# #### rename

# In[225]:


df2


# In[227]:


df2.rename(columns={'nome': 'Nome'}, inplace=True)


# In[228]:


df2


# In[229]:


df2.rename(index={5:60}, inplace=True)


# In[230]:


df2


# #### replace

# In[231]:


df2


# In[233]:


df2.Nome.replace('Tiãozinho', 'Sebastião', inplace=True)


# In[234]:


df2


# #### round

# In[235]:


df2['teste2'] = [1.25, 3.75, 4.95, 5.25]


# In[236]:


df2


# In[237]:


df2.teste2.round(0)


# In[238]:


df2.teste2.round(1)


# In[239]:


df2.teste2 = df2.teste2.round(1)


# In[240]:


df2


# #### to_clipboard()

# In[241]:


df2.to_clipboard()


# In[242]:


df2.to_clipboard(index=False)


# In[ ]:




