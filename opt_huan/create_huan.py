# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-4 replay file
# Internal Version: 2015_06_12-04.41.13 135079
# Run by DELL on Wed Apr 12 14:23:43 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: 执行 "onCaeGraphicsStartup()", 在目录 site 中 ...
from abaqus import *
from abaqusConstants import *

#参数 单位为m，为浮点型数据
def createhuan(Dxiaya,bound1,bound2):
	session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=296.627624511719, 
		 height=171.077789306641)
	session.viewports['Viewport: 1'].makeCurrent()
	session.viewports['Viewport: 1'].maximize()
	from caeModules import *
	from driverUtils import executeOnCaeStartup
	executeOnCaeStartup()
	session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
		referenceRepresentation=ON)
	Mdb()
	#: 新的模型数据库已创建.
	#: 模型 "Model-1"已创建.
	#：ConstrainedSketch意为草图
	session.viewports['Viewport: 1'].setValues(displayedObject=None)
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.sketchOptions.setValues(decimalPlaces=3)
	s.setPrimaryObject(option=STANDALONE)
	session.viewports['Viewport: 1'].view.setValues(nearPlane=0.155671, 
		farPlane=0.221452, width=0.259235, height=0.157112, cameraPosition=(
		0.0101353, 0.0190899, 0.188562), cameraTarget=(0.0101353, 0.0190899, 0))
	s.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(0.08, 0.0), 
		axisPoint2=(0.0, 0.07))
	session.viewports['Viewport: 1'].view.setValues(width=0.275782, height=0.16714, 
		cameraPosition=(0.00655649, 0.0189371, 0.188562), cameraTarget=(0.00655649, 
		0.0189371, 0))
	s.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(0.07, 0.0), 
		axisPoint2=(0.0, 0.0625))
	p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
		type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Part-1']
	p.BaseShell(sketch=s)
	s.unsetPrimaryObject()
	p = mdb.models['Model-1'].parts['Part-1']
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	del mdb.models['Model-1'].sketches['__profile__']
	p = mdb.models['Model-1'].parts['Part-1']
	f, e, d1 = p.faces, p.edges, p.datums
	t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[0], 
		sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 0.0))
	s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
		sheetSize=0.42, gridSpacing=0.01, transform=t)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.sketchOptions.setValues(decimalPlaces=3)
	s1.setPrimaryObject(option=SUPERIMPOSE)
	p = mdb.models['Model-1'].parts['Part-1']
	p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
	s1.Line(point1=(0.0, 0.0), point2=(0.08, 0.0))
	s1.HorizontalConstraint(entity=g[4], addUndoState=False)
	num_set=24
	s1.radialPattern(geomList=(g[4], ), vertexList=(), number=num_set, totalAngle=360.0, centerPoint=(0.0, 0.0))
	p = mdb.models['Model-1'].parts['Part-1']
	f = p.faces
	pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
	e1, d2 = p.edges, p.datums
	p.PartitionFaceBySketch(sketchUpEdge=e1[0], faces=pickedFaces, sketch=s1)
	s1.unsetPrimaryObject()
	del mdb.models['Model-1'].sketches['__profile__']
	session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
		engineeringFeatures=ON)
	session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
		referenceRepresentation=OFF)
	mdb.models['Model-1'].Material(name='Material-1')
	mdb.models['Model-1'].materials['Material-1'].Elastic(table=((730000000000.0, 
		0.267), ))
	mdb.models['Model-1'].materials['Material-1'].Plastic(table=((510000000.0, 
		0.0), (513520000.0, 0.00783), (554840000.0, 0.00876), (571780000.0, 
		0.0119), (627300000.0, 0.0411), (661880000.0, 0.0666)))
	mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
		preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM, 
		thickness=0.003, thicknessField='', idealization=NO_IDEALIZATION, 
		poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
		useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
	p = mdb.models['Model-1'].parts['Part-1']
	f = p.faces
	faces = f.getSequenceFromMask(mask=('[#ffffff ]', ), )
	region = p.Set(faces=faces, name='Set-1')
	p = mdb.models['Model-1'].parts['Part-1']
	p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
		offsetType=MIDDLE_SURFACE, offsetField='', 
		thicknessAssignment=FROM_SECTION)
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(
		optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
	a = mdb.models['Model-1'].rootAssembly
	a.DatumCsysByDefault(CARTESIAN)
	p = mdb.models['Model-1'].parts['Part-1']
	a.Instance(name='Part-1-1', part=p, dependent=ON)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(
		adaptiveMeshConstraints=ON)
	mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
		maxNumInc=100000000)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
	mdb.models['Model-1'].StaticStep(name='Step-2', previous='Step-1', 
		maxNumInc=100000000)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
	mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
		'S', 'LE', 'U', 'CF','COORD'))
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
		predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
	session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
		engineeringFeatures=OFF)
	session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
		referenceRepresentation=ON)
	p = mdb.models['Model-1'].parts['Part-1']
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	p = mdb.models['Model-1'].parts['Part-1']
	v = p.vertices
	verts = v.getSequenceFromMask(mask=('[#40 ]', ), )
	p.Set(vertices=verts, name='Set-2')
	#: 集 'Set-2' 已创建 (1 顶点).
	p = mdb.models['Model-1'].parts['Part-1']
	v = p.vertices
	verts = v.getSequenceFromMask(mask=('[#1 ]', ), )
	p.Set(vertices=verts, name='Set-3')
	#: 集 'Set-3' 已创建 (1 顶点).
	p = mdb.models['Model-1'].parts['Part-1']
	v = p.vertices
	verts = v.getSequenceFromMask(mask=('[#8 ]', ), )
	p.Set(vertices=verts, name='Set-4')
	#: 集 'Set-4' 已创建 (1 顶点).
	p = mdb.models['Model-1'].parts['Part-1']
	v = p.vertices
	verts = v.getSequenceFromMask(mask=('[#20 ]', ), )
	p.Set(vertices=verts, name='Set-5')
	#: 集 'Set-5' 已创建 (1 顶点).
	# import numpy库以及 保留有效数字的format函数
	import numpy as np
	from format_fun import format
	#定义椭圆长轴长80mm,短轴长70mm

	long_a=0.08
	short_b=0.07
	#定义查找的点的编号	
	nump=bound1-bound2
	jiao=360/num_set*np.pi/180*nump
	xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
	x=format(np.sqrt(xx),7)
	y=np.tan(jiao)*x
	#定义点2
	jiao2=15*np.pi/180*(nump-1)
	xx2=1/(1/long_a**2+np.tan(jiao2)**2/short_b**2)
	x2=format(np.sqrt(xx2),7)
	y2=np.tan(jiao2)*x2
	#使用坐标的方法寻找节点
	a = mdb.models['Model-1'].rootAssembly
	a.regenerate()
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	a = mdb.models['Model-1'].rootAssembly
	v1 = a.instances['Part-1-1'].vertices
	#verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
	#使用坐标的方法寻找节点
	nodePoint=v1.findAt(((x,-y,0),))
	#origionp=v1.findAt(((0,0,0),))
	region = a.Set(vertices=nodePoint, name='Set-1')
	#自定义坐标系
	from abaqusMacros import datumxy
	datumxy(x,y,x2,y2)
	#	
	#创建边界约束条件
	#边界条件BC-1，位移边界条件，创建强制位移，位移大小为
	mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
		region=region, u1=Dxiaya, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, 
		ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
		fieldName='', localCsys=mdb.models['Model-1'].rootAssembly.datums[5])
	#mdb.models['Model-1'].boundaryConditions['BC-1'].move('Step-2', 'Step-1')
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
	
	
	#边界条件BC-2，位移固定约束条件
	#定义椭圆长轴长80mm,短轴长70mm
	long_a=0.08
	short_b=0.07
	#定义查找的点的编号
	nump=bound1
	jiao=360/num_set*np.pi/180*nump
	xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
	x=format(np.sqrt(xx),7)
	y=np.tan(jiao)*x
	#
	a = mdb.models['Model-1'].rootAssembly
	v1 = a.instances['Part-1-1'].vertices
	nodePoint=v1.findAt(((-x,y,0),))
	#verts1 = v1.getSequenceFromMask(mask=('[#0 #4000 ]', ), )
	region = a.Set(vertices=nodePoint, name='Set-2')
	mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
		region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
		amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
		localCsys=None)
	#取消激活
	mdb.models['Model-1'].boundaryConditions['BC-2'].deactivate('Step-2')
	mdb.models['Model-1'].boundaryConditions['BC-1'].deactivate('Step-2')
	
	#边界条件BC-3，位移固定约束条件
	a = mdb.models['Model-1'].rootAssembly
	v1 = a.instances['Part-1-1'].vertices
	#verts1 = v1.getSequenceFromMask(mask=('[#0 #200 ]', ), )
	#计算查找点的坐标
	nump=bound2
	jiao=360/num_set*np.pi/180*nump
	xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
	x=format(np.sqrt(xx),7)
	y=np.tan(jiao)*x
	nodePoint=v1.findAt(((-x,-y,0),))
	region = a.Set(vertices=nodePoint, name='Set-3')
	#定义点2
	jiao2=360/num_set*np.pi/180*(nump-1)
	xx2=1/(1/long_a**2+np.tan(jiao2)**2/short_b**2)
	x2=format(np.sqrt(xx2),7)
	y2=np.tan(jiao2)*x2
	#创建自定义坐标系2
	from abaqusMacros import datumxy2
	datumxy2(x,y,x2,y2)
	mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', 
		region=region, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
		amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
		localCsys=mdb.models['Model-1'].rootAssembly.datums[8])
	mdb.models['Model-1'].boundaryConditions['BC-3'].deactivate('Step-2')
	#
	# from create_Set import createSet
	# createSet(num_set)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
		bcs=OFF, predefinedFields=OFF, connectors=OFF)
	session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
		meshTechnique=ON)
	p = mdb.models['Model-1'].parts['Part-1']
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
	session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
		meshTechnique=ON)
	session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
		referenceRepresentation=OFF)
	p = mdb.models['Model-1'].parts['Part-1']
	#布种，进行网格划分
	#p.seedPart(size=0.0001, deviationFactor=0.1, minSizeFactor=0.1)
	#p = mdb.models['Model-1'].parts['Part-1']
	p.seedPart(size=0.001, deviationFactor=0.1, minSizeFactor=0.1)
	p = mdb.models['Model-1'].parts['Part-1']
	p.generateMesh()
	a1 = mdb.models['Model-1'].rootAssembly
	a1.regenerate()
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
	session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(meshTechnique=OFF)
	a = mdb.models['Model-1'].rootAssembly
	v1 = a.instances['Part-1-1'].vertices
	long_a=0.08
	short_b=0.07
	num=24
	deg=360/num
	x=np.ones(num)
	y=np.ones(num)
	for i in range(0,num):
		if i<=num/4-1:
			jiao=deg*i*np.pi/180
			xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
			x[i]=format(np.sqrt(xx),7)
			y[i]=np.tan(jiao)*x[i]
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a.Set(vertices=nodePoint, name='node-%d'%(i))
		elif i<=num/4:
			jiao=deg*i*np.pi/180
			xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
			x[i]=format(np.sqrt(xx),7)
			y[i]=short_b
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a.Set(vertices=nodePoint, name='node-%d'%(i))
		elif i<=num*3/4-1:
			jiao=deg*i*np.pi/180
			xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
			x[i]=-format(np.sqrt(xx),7)
			y[i]=np.tan(jiao)*x[i]
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a.Set(vertices=nodePoint, name='node-%d'%(i))
		elif i<=num*3/4:
			jiao=deg*i*np.pi/180
			xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
			x[i]=-format(np.sqrt(xx),7)
			y[i]=-short_b
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a.Set(vertices=nodePoint, name='node-%d'%(i))
		else:
			jiao=deg*i*np.pi/180
			xx=1/(1/long_a**2+np.tan(jiao)**2/short_b**2)
			x[i]=format(np.sqrt(xx),7)
			y[i]=np.tan(jiao)*x[i]
			nodePoint=v1.findAt(((-x[i],y[i],0),))
			a.Set(vertices=nodePoint, name='node-%d'%(i))
#: 作业输入文件 "h12.inp" 已提交分析.
#: 作业 h12:  Analysis Input File Processor 成功完成.
#: 作业 h12:  Abaqus/Standard 成功完成.
#: 作业 h12 成功完成. 
#: 模型: D:/SIMULIA/Temp/h12.odb
#: 装配件个数:         1
#: 装配件实例个数:     0
#: 部件实例的个数:     1
#: 网格数:             1
#: 单元集合数:         2
#: 结点集合数:         9
#: 分析步的个数:       2