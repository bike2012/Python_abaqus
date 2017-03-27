# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:18:29 2017

@author: nasty
"""
from random import random,randint,choice
from copy import deepcopy
import numpy as np 
# 定义树的基本结构
class fwrapper:
    def __init__(self,function,childcount,name):
        self.function=function
        self.childcount=childcount
        self.name=name
 
class node:
    def __init__(self,fw,children):
        self.function=fw.function
        self.name=fw.name
        self.children=children
    def evaluate(self,inp):
        results=[n.evaluate(inp) for n in self.children]
        return self.function(results)
    def display(self,indent=0):
        print (' '*indent)+self.name
        for c in self.children:
            c.display(indent+1)
 
class paramnode:
    def __init__(self,idx):
        self.idx=idx
    def evaluate(self,inp):
        return inp[self.idx]
    def display(self,indent=0):
        print ('%sp%d' % (' '*indent,self.idx))
 
class constnode:
    def __init__(self,v):
        self.v=v
    def evaluate(self,inp):
        return self.v
    def display(self,indent=0):
        print ('%s%d' % (' '*indent,self.v))
#其中fwrapper代表着一种运算，它接受三个参数：函数的定义，
#函数里参数的个数，函数的名字。node就是一个节点，它的evaluate函数可以接受子节点的输入，
#并把fawapper定义的函数运用在子节点上，得到输出结果。它的display函数可以打印出节点以下的树的形式，
#方便我们分析程序内部表达的函数。paramnode是参数节点，总是返回输入的参数idx，constnode是常数节点，
#不管输入时什么，总是返回一个常数。
#接下来我们定义一些基本的运算：
addw=fwrapper(lambda l:l[0]+l[1],2,'add')
subw=fwrapper(lambda l:l[0]-l[1],2,'subtract')
mulw=fwrapper(lambda l:l[0]*l[1],2,'multiply')

def iffunc(l):
    if l[0]>0: return l[1]
    else: return l[2]
ifw=fwrapper(iffunc,3,'if')
 
def isgreater(l):
    if l[0]>l[1]: return 1
    else: return 0
gtw=fwrapper(isgreater,2,'isgreater')
 
flist=[addw,mulw,ifw,gtw,subw]
#其中加减乘都可以使用lambda一句话实现，但分段函数和比较函数要先定义一个函数，然后再用fwrapper。
#在flist里我们把这些函数都装起来，以便将来使用。
#有了这些函数，其实我们已经可以定义一个示例树并观察其运算后果了
#def exampletree( ):
#    return node(ifw,[
#    node(gtw,[paramnode(0),constnode(3)]),
#    node(addw,[paramnode(1),constnode(5)]),
#    node(subw,[paramnode(1),constnode(2)]),
#     ]
# )
# 
#exampletree=exampletree( )
#exampletree.evaluate([2,3])
#exampletree.evaluate([5,3])
#exampletree.display()

##
def makerandomtree(pc,maxdepth=4,fpr=0.5,ppr=0.6):
     if random( )<fpr and maxdepth>0:
         f=choice(flist)
         children=[makerandomtree(pc,maxdepth-1,fpr,ppr)
         for i in range(f.childcount)]
         return node(f,children)
     elif random( )<ppr:
         return paramnode(randint(0,pc-1))
     else:
         return constnode(randint(0,10))
 
#random1=makerandomtree(2)
#random1.evaluate([7,1])
#random1.evaluate([2,4])
#random2=makerandomtree(2)
#random2.evaluate([5,3])
#random2.evaluate([5,20])
#random1.display( )
#random2.display( )

#
def mutate(t,pc,probchange=0.1):
     if random( )<probchange:
         return makerandomtree(pc)
     else:
         result=deepcopy(t)
         if isinstance(t,node):
             result.children=[mutate(c,pc,probchange) for c in t.children]
         return result
 
def crossover(t1,t2,probswap=0.7,top=1):
     if random( )<probswap and not top:
         return deepcopy(t2)
     else:
         result=deepcopy(t1)
         if isinstance(t1,node) and isinstance(t2,node):
             result.children=[crossover(c,choice(t2.children),probswap,0) for c in t1.children]
     return result
 
 
#random2.display( )
#muttree=mutate(random2,2)
#muttree.display( )
#cross=crossover(random1,random2)
#cross.display( )

#
def hiddenfunction(x,y):
     return x**2+2*y+3*x+5
 
def buildhiddenset( ):
     rows=[]
     for i in range(200):
         x=randint(0,10)
         y=randint(0,10)
         rows.append([x,y,hiddenfunction(x,y)])
     return rows
 
def scorefunction(tree,s):
     dif=0
     for data in s:
         v=tree.evaluate([data[0],data[1]])
         dif+=abs(v-data[2])
     return dif
 
def getrankfunction(dataset):
     def rankfunction(population):
         scores=[(scorefunction(t,dataset),t) for t in population]
         scores.sort( )
         return scores
     return rankfunction
 
#hiddenset=buildhiddenset( )
#scorefunction(random2,hiddenset)
#scorefunction(random1,hiddenset)

#
def evolve(pc,popsize,rankfunction,maxgen=500,
     mutationrate=0.1,breedingrate=0.4,pexp=0.7,pnew=0.05):
     # Returns a random number, tending towards lower numbers. The lower pexp
     # is, more lower numbers you will get
     def selectindex( ):
         return int(np.log(random( ))/np.log(pexp))
     # Create a random initial population
     population=[makerandomtree(pc) for i in range(popsize)]
     for i in range(maxgen):
         scores=rankfunction(population)
         print(scores[0][0])
         if scores[0][0]==0: break
         # The two best always make it
         newpop=[scores[0][1],scores[1][1]]
         # Build the next generation
         while len(newpop)<popsize:
             if random( )>pnew:
                 newpop.append(mutate(
                 crossover(scores[selectindex( )][1],
                 scores[selectindex( )][1],
                 probswap=breedingrate),
                 pc,probchange=mutationrate))
             else:
                 # Add a random node to mix things up
                 newpop.append(makerandomtree(pc))
         population=newpop
     scores[0][1].display( )
     return scores[0][1]
 
 
rf=getrankfunction(buildhiddenset( ))
final = evolve(2,500,rf,mutationrate=0.2,breedingrate=0.1,pexp=0.7,pnew=0.1)