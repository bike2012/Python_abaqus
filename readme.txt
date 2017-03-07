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
	