# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def datumxy(x,y,x2,y2):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
	# import numpy as np
	# from format_fun import format
	# long_a=0.08
	# short_b=0.07
	# nump=pointori
	# jiao=15*np.pi/180*nump
	# xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
	# x=format(np.sqrt(xx),7)
	# y=np.tan(jiao)*x
	
	# jiao2=15*np.pi/180*(nump-1)
	# xx2=1/(1/long_a**2+np.tan(jiao2)**2/short_b**2)
	# x2=format(np.sqrt(xx),7)
	# y2=np.tan(jiao2)*x2
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Part-1-1'].vertices
    e1 = a.instances['Part-1-1'].edges
    a.DatumCsysByThreePoints(origin=(x,-y,0), point2=(x2,-y2,0), name='Datum csys-2', 
        coordSysType=CARTESIAN, 
        point1=(0,0,0))


def datumxy2(x,y,x2,y2):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
	# import numpy as np
	# from format_fun import format
	# long_a=0.08
	# short_b=0.07
	# nump=pointori
	# jiao=15*np.pi/180*nump
	# xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
	# x=format(np.sqrt(xx),7)
	# y=np.tan(jiao)*x
	
	# jiao2=15*np.pi/180*(nump-1)
	# xx2=1/(1/long_a**2+np.tan(jiao2)**2/short_b**2)
	# x2=format(np.sqrt(xx),7)
	# y2=np.tan(jiao2)*x2
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Part-1-1'].vertices
    e1 = a.instances['Part-1-1'].edges
    a.DatumCsysByThreePoints(origin=(-x,-y,0), point2=(-x2,-y2,0), name='Datum csys-3', 
        coordSysType=CARTESIAN, 
        point1=(0,0,0))		
		
def selectdatum():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    datum = mdb.models['Model-1'].rootAssembly.datums[5]
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(localCsys=datum)
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValues(u1=0.013)


def selectdatum2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    datum = mdb.models['Model-1'].rootAssembly.datums[8]
    mdb.models['Model-1'].boundaryConditions['BC-3'].setValues(localCsys=datum)


def XYNode():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    pass


def COORD():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior

    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'LE', 'U', 'CF', 'COORD'))


