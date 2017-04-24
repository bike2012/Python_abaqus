#-*-coding:utf-8-*-
from abaqus import *
from abaqusConstants import *
from create_huan import createhuan
import odbAccess
import visualization 
import numpy as np
xiaya=0.011
B1=1
B2=1
print '下压量为：%02d%02s'%(xiaya*1000,'mm')
print '边界约束B1,B2位置:%s%d,%d%s'%('节点',B1,B2,'处')
createhuan(xiaya,B1,B2)
jobName = "HUAN%02d%01d%01d" %(xiaya*1000,B1,B2)
#print jobName
#创建job
mdb.Job(name=jobName, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
#运行job
mdb.jobs[jobName].submit(consistencyChecking=OFF)
mdb.jobs[jobName].waitForCompletion()

#打开数据库
from odbAccess import *
odb=openOdb(path='%s.odb'%(jobName))

coord=odb.steps['Step-1'].frames[0].fieldOutputs['COORD']
u=odb.steps['Step-2'].frames[1].fieldOutputs['U']
assembly=odb.rootAssembly
num=24
x=np.ones(num+1)
y=np.ones(num+1)
for i in range(0,num):
	nodeName='NODE-%d'%(i)
	nodeset=assembly.nodeSets[nodeName]
	coxy=coord.getSubset(region=nodeset)
	uxy=u.getSubset(region=nodeset)
	x[i]=coxy.values[0].data[0]+uxy.values[0].data[0]
	y[i]=coxy.values[0].data[1]+uxy.values[0].data[1]
	print '%f,%f'%(x[i],y[i])
x[num]=x[0]
y[num]=y[0]
#使用参数插值获取xy点
from scipy import interpolate
f,t=interpolate.splprep([x,y],s=0)
xi,yi=interpolate.splev(np.linspace(t[0],t[-1],900),f)
#计算校正后零件的圆度
x0=np.sum(x)/len(x)
y0=np.sum(y)/len(y)
x1=x-x0
y1=y-y0
maxlong=np.max(x1*x1+y1*y1)
#计算多边形的面积，使用多边形的面积代替变形后工件的面积
import getarea as gae
points=gae.Point(xi,yi)
area=gae.GetAreaOfPolyGon(points)
#圆度
cir=area/(maxlong*np.pi)
print area
print cir
odb.close()