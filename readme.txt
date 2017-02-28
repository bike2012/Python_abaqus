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