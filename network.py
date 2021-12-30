#!/usr/bin/env python
#   -*-   coding:   cp936   -*-  使用中文
import networkx as nx
import matplotlib.pyplot as plt
nG=nx.Graph();#创建一个空的图
nG


import pandas as pd   
#分解信息
def list_split(content,separator): 
    new_list=[]
    for i in range(len(content)):
        new_list.append(list(filter(None,content[i].split(separator))))#以separator为分隔符
    return new_list
#清除信息中的空格
def list_replace(content,old,new):            
    return[content[i].replace(old,new) for i in range(len(content))]

WXdata=pd.read_excel('PyDm_data.xlsx','WXdata');

def find_words(content,pattern): #寻找关键词
    return[content[i] for i in range(len(content)) if (pattern in content[i])==True]
    
def search_university(content,pattern):#寻找大学
    return len([find_words(content[i],pattern) for i in range(len(content))
               if find_words(content[i],pattern)!=[]])
university=pd.read_excel('PyDm_data.xlsx','university');
#university1=sum(university,[])

organ=list_split(WXdata['Organ'],';')

data1=pd.DataFrame([[i,search_university(organ,i)] for i in university['学校名称']])

keyword=list_split(WXdata['Keyword'].dropna(axis=0,how='all').tolist(),';;')
keyword1=sum(keyword,[])
author=list_replace(WXdata['Author'].dropna(axis=0,how='all').tolist(),',',';')
author1=list_split(author,';')
author2=sum(author1,[])
data1;


#获取前30名的高频数据
data_author=pd.DataFrame(author2)[0].value_counts()[:30].index.tolist()

data_keyword=pd.DataFrame(keyword1)[0].value_counts()[:30].index.tolist()

data_university=data1.sort_values(by = 1,ascending=False,axis=0)[0:30][0].tolist()
#data_university=data1.sort_values(by=1，ascending=False,axis=0)[0:30]['学校名称'].tolist()
data_university;



```python
def occurence(data,document): #定义共现矩阵
    empty1=[];empty2=[];empty3=[]
    for a in data:
        for b in data:
            count = 0
            for x in document:
                if [a in i for i in x].count(True)>0 and [b in i for i in x].count(True)>0:
                    count=count+1
            empty1.append(a);empty2.append(b);empty3.append(count)#append() 方法向列表的尾部添加一个新的元素。只接受一个参数
    df=pd.DataFrame({'from':empty1,'to':empty2,'weight':empty3})
    #具有标注轴（行和列）的二维大小可变的表格数据结构
    G=nx.from_pandas_edgelist(df,'from','to','weight')
    #返回包含边列表的图形
    return (nx.to_pandas_adjacency(G,dtype=int))#注意对齐


Matrix1=occurence(data_author,author1)
Matrix1;
Matrix2=occurence(data_university,organ)
Matrix2;
Matrix3=occurence(data_keyword,keyword)
Matrix3;

