# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by nasty on Mon Mar 13 08:54:44 2017

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
force_1=3000
force_2=3000

Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints

# 草绘圆环
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(51.25, 31.25))
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(43.75, 20.0))
s.RadialDimension(curve=g[2], textPoint=(-27.8459815979004, -22.1807708740234), 
    radius=100.0)
s.RadialDimension(curve=g[3], textPoint=(-20.812671661377, -29.010425567627), 
    radius=80.0)
	
# 建立模型1的部件1	
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=4.0)

s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']

# session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

p = mdb.models['Model-1'].parts['Part-1']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[2], sketchUpEdge=e[2], 
    sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 4.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=565.2, gridSpacing=14.13, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)

s1.ConstructionLine(point1=(0.0, 0.0), point2=(-42.39, 0.0))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.CoincidentConstraint(entity1=v[0], entity2=g[4], addUndoState=False)
s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.0, 21.1950000000326))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.CoincidentConstraint(entity1=v[0], entity2=g[5], addUndoState=False)
s1.FixedConstraint(entity=g[4])
s1.FixedConstraint(entity=g[5])
s1.Line(point1=(0.0, 100.0), point2=(0.0, 80.0))
s1.VerticalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[6], addUndoState=False)
s1.CoincidentConstraint(entity1=v[3], entity2=g[2], addUndoState=False)
s1.CoincidentConstraint(entity1=v[4], entity2=g[3], addUndoState=False)
s1.Line(point1=(80.0, 0.0), point2=(100.0, 0.0))
s1.HorizontalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[7], addUndoState=False)
s1.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
s1.Line(point1=(0.0, -80.0), point2=(0.0, -100.0))
s1.VerticalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[8], addUndoState=False)
s1.CoincidentConstraint(entity1=v[7], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[8], entity2=g[2], addUndoState=False)
s1.Line(point1=(-80.0, 0.0), point2=(-100.0, 0.0))
s1.HorizontalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[9], addUndoState=False)
s1.CoincidentConstraint(entity1=v[9], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[10], entity2=g[2], addUndoState=False)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
f1, e1, d2 = p.faces, p.edges, p.datums
p.PartitionFaceBySketchThruAll(sketchPlane=f1[2], sketchUpEdge=e1[2], 
    faces=pickedFaces, sketchPlaneSide=SIDE1, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']


import os
#os.chdir(r"F:\Projects\abaqus\huan")

# 创建材料
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((210000000000.0, 
    0.27), ))
mdb.models['Model-1'].materials['Material-1'].Plastic(table=((218.11, 0.0), (
    218.113, 0.002), (226.903, 0.004), (232.208, 0.006), (236.047, 0.008), (
    239.069, 0.01), (241.566, 0.012), (243.698, 0.014), (245.56, 0.016), (
    247.214, 0.018), (248.703, 0.02), (258.726, 0.04), (264.775, 0.06), (
    269.153, 0.08), (272.598, 0.1), (275.446, 0.12), (277.877, 0.14), (278.972, 
    0.15), (283.584, 0.2), (290.214, 0.3), (295.012, 0.4), (298.789, 0.5), (
    301.91, 0.6), (304.574, 0.7), (306.902, 0.8), (308.969, 0.9), (310.83, 
    1.0), (312.523, 1.1), (314.07, 1.2), (315.513, 1.3), (316.849, 1.4), (
    318.097, 1.5), (319.27, 1.6), (320.375, 1.7), (321.42, 1.8), (322.413, 
    1.9), (323.357, 2.0), (324.257, 2.1), (325.118, 2.2)))
#创建实体截面
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)

p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )

#为部件分配截面属性
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

#创建部件实例	
#a = mdb.models['Model-1'].rootAssembly
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)


#创建分析步step-1、step-2、step-3、step-4，静力分析步的时间为1.0，初始增量为1
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=10000, initialInc=1, maxInc=1, nlgeom=ON)
mdb.models['Model-1'].StaticStep(name='Step-2', previous='Step-1', 
    maxNumInc=10000, initialInc=1, maxInc=1)
mdb.models['Model-1'].StaticStep(name='Step-3', previous='Step-2', 
    maxNumInc=10000, initialInc=1, maxInc=1)
mdb.models['Model-1'].StaticStep(name='Step-4', previous='Step-3', 
    maxNumInc=10000, initialInc=1, maxInc=1)

#创建场输出，'S', 'PE', 'PEMAG', 'LE', 'U', 'UT', 'UR'
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'PE', 'PEMAG', 'LE', 'U', 'UT', 'UR'))

a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
#创建查考点，添加耦合约束
a.ReferencePoint(point=a.instances['Part-1-1'].InterestingPoint(edge=e1[0], 
    rule=MIDDLE))	
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['Part-1-1'].edges
#创建查考点，添加耦合约束
a.ReferencePoint(point=a.instances['Part-1-1'].InterestingPoint(edge=e21[6], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[4], )

region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-1')
mdb.models['Model-1'].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-3')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#40 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-3')
mdb.models['Model-1'].Coupling(name='Constraint-2', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
	
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[4], )

#在圆环表面施加线载荷
region = a.Set(referencePoints=refPoints1, name='Set-5')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-4', 
    region=region, cf2=-force_1, distributionType=UNIFORM, field='', 
    localCsys=None)
mdb.models['Model-1'].loads['Load-1'].move('Step-4', 'Step-3')
mdb.models['Model-1'].loads['Load-1'].move('Step-3', 'Step-2')
mdb.models['Model-1'].loads['Load-1'].move('Step-2', 'Step-1')
mdb.models['Model-1'].loads['Load-1'].deactivate('Step-2')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
region = a.Set(referencePoints=refPoints1, name='Set-6')
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-4', 
    region=region, cf1=-force_2, distributionType=UNIFORM, field='', 
    localCsys=None)
mdb.models['Model-1'].loads['Load-2'].move('Step-4', 'Step-3')
mdb.models['Model-1'].loads['Load-2'].deactivate('Step-4')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#200 ]', ), )
region = a.Set(edges=edges1, name='Set-7')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-4', 
    region=region, localCsys=None)
mdb.models['Model-1'].boundaryConditions['BC-1'].move('Step-4', 'Step-3')
mdb.models['Model-1'].boundaryConditions['BC-1'].move('Step-3', 'Step-2')
mdb.models['Model-1'].boundaryConditions['BC-1'].move('Step-2', 'Step-1')
mdb.models['Model-1'].boundaryConditions['BC-1'].deactivate('Step-2')
a = mdb.models['Model-1'].rootAssembly
#添加边界条件
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Set(edges=edges1, name='Set-8')
mdb.models['Model-1'].EncastreBC(name='BC-2', createStepName='Step-4', 
    region=region, localCsys=None)
mdb.models['Model-1'].boundaryConditions['BC-2'].move('Step-4', 'Step-3')
mdb.models['Model-1'].boundaryConditions['BC-2'].deactivate('Step-4')
p = mdb.models['Model-1'].parts['Part-1']
#为部件实例撒种子
p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
#划分网格
p.generateMesh()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly

# 为模型创建分析作业
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4, 
    numDomains=4, numGPUs=1)
#等待分析作业完成	
mdb.jobs['Job-1'].submit()
mdb.jobs['Job-1'].waitForCompletion()
#print'分析已经顺利完成，进行下一步处理'
#后处理部分
from odbAccess import *
myodb=openOdb('Job-1.odb')
mystep=myodb.steps
step4=mystep['Step-4'].frames
len1=len(step4)
u1=step4[len1-1].fieldOutputs['U'].values
len2=len(u1)
add_u1=0
for ui in range(len2):
 u1x=u1[ui].data
 add_u1x=0
 for i in range(3):
  u1y= u1x[i] 
  add_u1x=add_u1x+abs(u1y)
 add_u1=add_u1+add_u1x
print(add_u1)