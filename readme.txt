# read me txt


# 介绍在abaqus中运行python脚本的方法
	first 启动abaqus/cae的同时运行脚本
		方法：
			在abaqus command 命令窗口中输入
			abaqus cae script =myscript.py 
			abaqus cae startup =myscript.py
			ps:当然在输入命令之前首先要将当前工作目录调整到myscript.py所在的文件夹下
			下列命令可以在在启动abaqus/view的同时并运行脚本：
			abaqus view script =myscript.py
			abaqus view startup =myscript.py
		end
	second 不启动abaqus/cae而直接运行脚本
		方法：
			abaqus cae noGUI =myscript.py
			不启动abaqus/view的同时并运行脚本：
			abaqus view noGUI =myscript.py
			这样做：无法在abaqus/cae中显示分析结果，无法监控分析作业，但是可以提高运行效率，适用于自动实现前后处理的情况
	third 从启动屏幕运行脚本
	fourth 从file菜单运行脚本
	fifth 从命令行运行脚本
		方法：
			execfile('file_name')
			ps: file_name需要给出脚本文件的完整路径，except：文件在工作目录下
#end


# 介绍创建脚本的方法
	1.在宏(macro)管理器中录制宏
	2.借助abaqus.rpy文件
	3.使用PythonReader.exe软件
end


#常用的abaqus内核指令
	1.高亮显示以及取消高亮显示
	2.几何导入
	3.创建集合
	4.单元和节点重新编号
	5.更改草图平面
	6.创建基于单元的面
	7.统计零件或实例的单元和节点数量
	8.sendCommend()指令注意问题
	9.合并节点mergeNodes()
	10.elementFaces与elemFaces的区别
	11.by angle的选取方式
	12.使用findAT()选取对象
	13.有关系统日期和时间的指令
	14. .rpy及.jnl文件的输出格式控制
end


#abaqus GUI应用程序可以实现以下功能
	1.在标准abaqus/cae基础上增加新的功能模块，，对多种工具进行管理。
	2.移除标准abaqus/cae的应用程序模块或者工具条，在创建用户自定义的应用程序的时候，用户可以自定义要加载的标准ababqus/cae的
	  标准模块或者工具条
	3.修改标准abaqus/cae的应用程序模块或者工具条
	4.改变应用程序名称及其版本号
end	


#abaqus插件程序的组成
	一般插件程序由三部分文件组成：
	1.注册文件
	2.图形界面文件
	3.内核执行文件
end


#python命名规则
	1.变量名：首字母一般是字母或者'_',其他位置字符可以是：字母、下划线‘_'、数字组成
	2.模块名：首字符一般是小写字母，*.py文件本身就是一个模块，所以模块名也就是文件名
	3.类名：首字母为大写，其他字母为小写
	4.对象名：使用小写字母
	5.访问类的属性和方法的表示方式为：在对象名后面跟操作符”."，类的私有变量和私有方法则以两个下划线为前缀”__“
	6.函数名：首字母通常为小写，通过下划线或者单词首字母大写的方式增加函数名的可读性
end


#python定义函数的参数时应当注意
	默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
	一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
	二是如何设置默认参数。
	当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
	使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
end


#python模块的使用
	模块：为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
	在Python中，一个.py文件就称之为一个模块（Module）
	好处：
	最大的好处是大大提高了代码的可维护性。
	其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模
	使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突
	包：
	如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
	举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
	现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：
	每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有
	Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany
	安装第三方模块：
	在Python中，安装第三方模块，是通过包管理工具pip完成的
	mac系统和linux系统中一般已经安装了pip，不需要单独安装
	如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。
	在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip	
	注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3
	模块搜索路径：
	当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
	>>> import mymodule
	Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
	mportError: No module named mymodule
	默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
	如果我们要添加自己的搜索目录，有两种方法：
	一是直接修改sys.path，添加要搜索的目录：
	>>> import sys
	>>> sys.path.append('/Users/michael/my_py_scripts')
	这种方法是在运行时修改，运行结束后失效。
	第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
end


#面向对象编程
	面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

	面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

	而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

	在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
	
	所以，面向对象的设计思想是抽象出Class，根据Class创建Instance（实例）
end


#编写脚本访问输出数据库的时候，应当注意：
	1.不能修改或删除输出数据库中的数据，创建新的odb文件时，只允许从odb文件中复制数据，而不会删除数据
	2.对于同一个输出数据库文件，每次只允许一个用户访问，为了防止损坏文件，访问过程中输出数据库文件将自动被锁定
	3.从输出数据库中读取数据向后兼容，即新版本的abaqus可以从读入低版本输出数据库文件
	4.向输出数据库中写入数据不向后兼容，即新版本的abaqus不可以向低版本输出数据库写入数据
	
	如果希望编写脚本来访问和处理输出数据库中的计算结果，这必须包括以下语句：
	
		from odbAccess import*
	
	如果脚本中还会用到abaqus脚本接口中的符号常数，则还应导入模块abaqusConstants，因此，必须包含下列语句：
	
		from abaqusConstants import*
	
	如果希望在其他软件分析结果的基础上，创建abaqus输出数据库，一般需要创建材料对象（）、截面对象（）或梁对象（），因此，应当使用下列语句导入相应模块：
	
		from odbMaterial import*
		from odbSection import*03
		
end


#使用对象模型编写脚本

