# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by nasty on Mon Mar 13 08:54:44 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

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
os.chdir(r"F:\Projects\abaqus\huan")

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
#创建查考点
a.ReferencePoint(point=a.instances['Part-1-1'].InterestingPoint(edge=e1[0], 
    rule=MIDDLE))	
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
e21 = a.instances['Part-1-1'].edges
#创建查考点
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
region = a.Set(referencePoints=refPoints1, name='Set-5')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-4', 
    region=region, cf2=-800.0, distributionType=UNIFORM, field='', 
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
    region=region, cf1=-850.0, distributionType=UNIFORM, field='', 
    localCsys=None)
mdb.models['Model-1'].loads['Load-2'].move('Step-4', 'Step-3')
mdb.models['Model-1'].loads['Load-2'].deactivate('Step-4')
session.viewports['Viewport: 1'].view.setValues(nearPlane=433.21, 
    farPlane=617.399, width=334.953, height=151.803, viewOffsetX=-19.7698, 
    viewOffsetY=54.1882)
session.viewports['Viewport: 1'].view.setValues(nearPlane=431.239, 
    farPlane=587.049, width=333.429, height=151.112, cameraPosition=(-22.4555, 
    -123.585, 498.306), cameraUpVector=(0.051699, 0.983596, -0.172819), 
    cameraTarget=(41.3966, -30.0735, -72.1728), viewOffsetX=-19.6799, 
    viewOffsetY=53.9417)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316.071, 
    farPlane=659.761, width=244.383, height=110.756, cameraPosition=(-129.479, 
    -451.673, 147.336), cameraUpVector=(-0.202089, 0.736713, 0.645302), 
    cameraTarget=(79.3006, 50.1252, -59.7317), viewOffsetX=-14.4241, 
    viewOffsetY=39.5359)
session.viewports['Viewport: 1'].view.setValues(nearPlane=337.075, 
    farPlane=638.757, width=179.796, height=81.4848, viewOffsetX=-14.8618, 
    viewOffsetY=30.2976)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=321.371, 
    farPlane=640.065, width=171.419, height=77.6884, cameraPosition=(-359.064, 
    -301.899, 122.829), cameraUpVector=(0.144558, 0.768877, 0.622841), 
    cameraTarget=(105.099, 2.97918, -49.999), viewOffsetX=-14.1694, 
    viewOffsetY=28.8861)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Set(edges=edges1, name='Set-8')
mdb.models['Model-1'].EncastreBC(name='BC-2', createStepName='Step-4', 
    region=region, localCsys=None)
mdb.models['Model-1'].boundaryConditions['BC-2'].move('Step-4', 'Step-3')
mdb.models['Model-1'].boundaryConditions['BC-2'].deactivate('Step-4')
session.viewports['Viewport: 1'].view.setValues(nearPlane=360.559, 
    farPlane=615.229, width=192.322, height=87.1616, cameraPosition=(-61.3719, 
    -439.669, 212.256), cameraUpVector=(0.185657, 0.750958, 0.633714), 
    cameraTarget=(38.6964, 47.7982, -88.7915), viewOffsetX=-15.8972, 
    viewOffsetY=32.4084)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=432.693, 
    farPlane=721.657, width=331.831, height=150.762, cameraPosition=(262.421, 
    297.103, 421.597), cameraUpVector=(-0.61627, 0.602459, -0.507203), 
    cameraTarget=(5.18858, -3.26881, -4.87135), viewOffsetX=9.48041, 
    viewOffsetY=4.36859)
session.viewports['Viewport: 1'].view.setValues(nearPlane=497.021, 
    farPlane=636.44, width=381.164, height=173.176, cameraPosition=(99.142, 
    12.4221, 559.868), cameraUpVector=(-0.200881, 0.923949, -0.325522), 
    cameraTarget=(1.52759, -0.92239, -13.3334), viewOffsetX=10.8898, 
    viewOffsetY=5.01806)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4, 
    numDomains=4, numGPUs=1)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Error in job Job-1: Too many attempts made for this increment
#: Error in job Job-1: THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.
#: Job Job-1: Abaqus/Standard aborted due to errors.
#: Error in job Job-1: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=360.955, 
    farPlane=614.832, width=159.915, height=78.0039, viewOffsetX=-19.2492, 
    viewOffsetY=25.0135)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].loads['Load-1'].setValues(cf2=-800.0, 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
mdb.models['Model-1'].loads['Load-2'].setValues(cf1=-850.0, 
    distributionType=UNIFORM, field='')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
# mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(name='F:/Projects/abaqus/huan/Job-1.odb')
#: Model: F:/Projects/abaqus/huan/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       6
#: Number of Node Sets:          13
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=459.362, 
    farPlane=697.409, width=434.632, height=204.492, cameraPosition=(167.43, 
    153.288, 534.016), cameraUpVector=(-0.321084, 0.807547, -0.494745), 
    cameraTarget=(5.16633, -0.163166, -3.00324))
session.animationController.stop()
session.animationController.decrementFrame()
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=HARMONIC)
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=TIME_HISTORY)
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=HARMONIC)
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
mdb.saveAs(pathName='F:/Projects/abaqus/huan/huan01')
#: The model database has been saved to "F:\Projects\abaqus\huan\huan01.cae".
session.viewports['Viewport: 1'].view.setValues(width=407.721, height=191.831, 
    viewOffsetX=-10.7845, viewOffsetY=-6.02585)

cliCommand("""from odbAccess import *""")
cliCommand("""myodb=openOdb('Job-1.odb')""")
#: Warning: The database has been opened with readOnly flag on. It will remain readOnly.
cliCommand("""mystep=myodb.steps""")
cliCommand("""mystep.keys()""")
#: ['Step-1', 'Step-2', 'Step-3', 'Step-4']
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=6 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=392.62, 
    farPlane=752.155, width=349.194, height=164.294, cameraPosition=(324.95, 
    357.69, 308.849), cameraUpVector=(-0.556092, 0.525738, -0.643709), 
    cameraTarget=(0.425866, -5.71551, -8.7773), viewOffsetX=-9.23638, 
    viewOffsetY=-5.16086)
session.viewports['Viewport: 1'].view.setValues(nearPlane=479.517, 
    farPlane=676.675, width=426.479, height=200.656, cameraPosition=(219.853, 
    46.4991, 534.729), cameraUpVector=(-0.0942054, 0.911997, -0.399233), 
    cameraTarget=(8.07322, 0.916074, -5.02757), viewOffsetX=-11.2806, 
    viewOffsetY=-6.30309)
session.viewports['Viewport: 1'].view.setValues(nearPlane=468.579, 
    farPlane=687.317, width=416.751, height=196.079, cameraPosition=(205.99, 
    71.6873, 537.308), cameraUpVector=(-0.106006, 0.893897, -0.435558), 
    cameraTarget=(8.12589, 0.858643, -5.0001), viewOffsetX=-11.0233, 
    viewOffsetY=-6.15932)
session.viewports['Viewport: 1'].view.setValues(nearPlane=475.085, 
    farPlane=681.381, width=422.537, height=198.802, cameraPosition=(181.433, 
    60.8804, 547.74), cameraUpVector=(-0.0772581, 0.901901, -0.424976), 
    cameraTarget=(8.59274, 0.889017, -4.33959), viewOffsetX=-11.1763, 
    viewOffsetY=-6.24484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=490.048, 
    farPlane=667.64, width=435.846, height=205.063, cameraPosition=(97.7664, 
    57.733, 569.69), cameraUpVector=(-0.0381115, 0.905642, -0.422327), 
    cameraTarget=(9.4674, 1.30323, -2.39688), viewOffsetX=-11.5283, 
    viewOffsetY=-6.44152)
mdb.save()
#: The model database has been saved to "F:\Projects\abaqus\huan\huan01.cae".
