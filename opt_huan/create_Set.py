from abaqus import *
from abaqusConstants import *


def createSet():
	import numpy as np
	from format_fun import format
	a12 = mdb.models['Model-1'].rootAssembly
	v1 = a12.instances['Part-1-1'].vertices
	a=0.08
	b=0.07
	num=24
	x=np.ones(num)
	y=np.ones(num)
	for i in range(0,num):
		if i<=num/4-1:
			jiao=15*i*np.pi/180
			xx=1/(1/a**2+np.tan(jiao)**2/b**2)
			x[i]=format(np.sqrt(xx),7)
			y[i]=np.tan(jiao)*x[i]
			nodePoint=v1.findAt(((-x[i],y[i],0),))
		    a12.Set(vertices=nodePoint, name='node-%d'%(i))
		elif i<=num/4:
			jiao=15*i*np.pi/180
			xx=1/(1/a**2+np.tan(jiao)**2/b**2)
			x[i]=format(np.sqrt(xx),7)
			y[i]=b
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a12.Set(vertices=nodePoint, name='node-%d'%(i))
		elif i<=num*3/4-1:
			jiao=15*i*np.pi/180
			xx=1/(1/a**2+np.tan(jiao)**2/b**2)
			x[i]=-format(np.sqrt(xx),7)
			y[i]=np.tan(jiao)*x[i]
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a12.Set(vertices=nodePoint, name='node-%d'%(i))
		elif i<=num*3/4:
			jiao=15*i*np.pi/180
			xx=1/(1/a**2+np.tan(jiao)**2/b**2)
			x[i]=-format(np.sqrt(xx),7)
			y[i]=-b
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a12.Set(vertices=nodePoint, name='node-%d'%(i))
		else:
			jiao=15*i*np.pi/180
			xx=1/(1/a**2+np.tan(jiao)**2/b**2)
			x[i]=format(np.sqrt(xx),7)
			y[i]=np.tan(jiao)*x[i]
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a12.Set(vertices=nodePoint, name='node-%d'%(i))