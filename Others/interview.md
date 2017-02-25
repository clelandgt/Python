##软件管理
### Centos7下安装GUI
1. 安装GUI包
     $sudo  yum groupinstall "GNOME Desktop" "Graphical Administration Tools"
2. 更新系统运行的级别
     $sudo ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target
### Centos7下安装pip
启用epel repository
     $yum install epel-release
然后安装pip
     $yum install -y python-pip
###更新下载源
更新cento7s的下载源为阿里云
1. 备份
     $mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
2. 下载源到本地
     **CentOS 5**
     $wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo
     **CentOS 6**
     $wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
     **CentOS7**
     $wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
3. 下载到本地
     $yum makecache


##系统管理
###host
     TODO：


##常用命令
### 感叹号
1. !! 表示上一个命令
2. !str 历史命令中最近一条以str开头的命令
3. 以上两个命令最好不要直接运行，先使用cat !!  或 cat !str。 查看是否是要运行的命令，然后再运行。

### 查看端口
查看端口号
     $ netstat -apn|grep <端口号>
根据找到的进程号以后，查询该进程的详细信息
     $ ps -aux | grep <进程号>

### 实时查看日志
     $ tailf -n 100 file
     $ tail -f logfile

### 设置开机自启
####使用 chkconfig 来配置启动级别
1. 设置mysql开机自启
     $ chkconfig mysql on
2. 取消mysql开机自启
     $ chkconfig mysql off
####使用systemctl 替代chkconfig
systemctl可以完美替代chkconfig和service，常使用的动作有start,stop,restart,status,enable,disable,is-enabled
命令基本操作格式： systemctl   动作   服务名.service
如，设置mysql开机自启
     sudo systemctl start application.service #启动服务
     sudo systemctl stop application.service #停止服务
     sudo systemctl restart application.service #重启服务
     sudo systemctl enable application.service #设置开机自启
     sudo systemctl disable application.service #取消开机自启
     systemctl status application.service #查看服务的状态
     systemctl is-active application.service #查看服务是否有效
     systemctl is-enabled application.service #查看服务是否设置开机自启
     systemctl is-failed application.service #查看服务是否开启失败
     systemctl list-units #列出全部服务
####修改 /etc/rc.d/rc.local
     ...

### 查看目录结构
查看目录结构时，限制目录的显示层数
     $ tree -L 2   

### 查看目录大小
     $ du -sh

### nohup
     $ nohup command > outputfile &

### 改变文件夹的权限包括其子文件夹和文件
     $ chmod -R 777 folder

### 免密登录
     $ ssh-keygen #生成密钥
     $ ssh-copy-id user@host #将公钥推送到服务器

### 查找系统的大文件
     $ find . -type f -size +800M #查找大于800M的文件

### tar的使用
#### 打包
     $ tar xvf FileName.tar #解包
     $ tar cvf FileName.tar DirName #打包

#### 压缩
     $ tar zxvf FileName.tar.gz #解压
     $ tar zcvf FileName.tar.gz DirName #压缩

##常用工具
###vim
查看教程运行： vimtutor


##第三方工具
###iftop网络流量监控
界面上面显示的是类似刻度尺的刻度范围，为显示流量图形的长条作标尺用的.中间的<= =>这两个左右箭头，表示的是流量的方向。
TX：发送流量
RX：接收流量
TOTAL：总流量
Cumm：运行iftop到目前时间的总流量
peak：流量峰值
rates：分别表示过去 2s 10s 40s 的平均流量


###htop
启用epel repository
     $ yum install epel-release
安装htop
     $ yum -y install htop




