# 说明文档
```angular2html
然后进入你的.py所处的文件夹，打开命令控制台，按自己的打包方式输入以下代码即可：

Pyinstaller -F main.py //打包exe
Pyinstaller -F main.pyw //打包exe 或重命名

Pyinstaller -F -w main.py //不带控制台的打包

Pyinstaller -F -i xx.ico main.py //打包指定exe图标打包

Pyinstaller -F -w -i xx.ico main.py //打包不带控制台的带图标的exe
```
