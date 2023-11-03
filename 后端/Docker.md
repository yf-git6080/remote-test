# Docker

## Docker常用命令

~~~shell
# 启动docker服务
systemctl start docker
# 设置 Docker 服务在系统启动时自动启动
systemctl enable docker


~~~



## Docker安装

~~~
# Ubuntu安装

sudo apt update
sudo apt install docker.io
sudo apt install docker-compose

# 启动docker
sudo systemctl start docker

# 自动启动 Docker 服务并在系统启动时启动它
sudo systemctl enable docker

sudo docker --version

sudo docker run hello-world

~~~





> 查看环境

```shell
# 查看系统内核
[root@localhost tyrant]# uname -r
3.10.0-1160.el7.x86_64
```

```shell
# 系统版本
[root@localhost tyrant]# cat /etc/os-release
NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="7"

```

文档：[Install Docker Engine on CentOS | Docker Docs](https://docs.docker.com/engine/install/centos/)

```shell
# 卸载旧版本
yum remove docker \
            docker-client \
            docker-client-latest \
            docker-common \
            docker-latest \
            docker-latest-logrotate \
            docker-logrotate \
            docker-engine


# 2. 安装需要的安装包
yum install -y yum-utils

# 3. 设置镜像仓库
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
    
# 4. 安装最新版本的 Docker Engine 和 containerd
yum install docker-ce docker-ce-cli containerd.io

# 5. 查看docker-ce支持版本
yum list docker-ce --showduplicates|sort -r
# 6. 查看docker-ce-cli版本
yum list docker-ce-cli --showduplicates|sort -r
```

```shell
# 1. 删除任何已存在的Docker安装（如果有的话）：
	sudo yum remove docker docker-client docker-client-latest docker-common docker-latest 	docker-latest-logrotate docker-logrotate docker-engine
# 2. 添加Docker仓库
	sudo vi /etc/yum.repos.d/docker-ce.repo
        # 添加以下信息
        [docker-ce-stable]
        name=Docker CE Stable - $basearch
        baseurl=https://download.docker.com/linux/centos/7/$basearch/stable
        enabled=1
        gpgcheck=1
        gpgkey=https://download.docker.com/linux/centos/gpg
# 3. 安装Docker
	sudo yum install docker-ce docker-ce-cli containerd.io
# 4. 启动Docker：
	sudo systemctl start docker
# 5. 验证 
	docker --version
```

![image-20230902231212795](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230902231212795.png)

```shell
# 6. 下载hello-world
	docker run hello-world
```

![image-20230902231507828](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230902231507828.png)

```shell
# 7. 查看
	docker images
```

![image-20230902231853182](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230902231853182.png)

> 卸载docker： 	yum remove docker-ce docker-ce-cli containerd.io
>
> 删除资源(默认地址)：	 rm -rf /var/lib/docker	
>

### 设置加速

```shell
# 设置加速
# 1. 创建	touch /etc/docker/daemon.json
# 2. 写入腾讯云加速	tee /etc/docker/daemon.json <<EOF
                    {
                      "registry-mirrors": ["https://mirror.ccs.tencentyun.com"]
                    }
                    EOF
      阿里云加速		tee /etc/docker/daemon.json <<-'EOF'
                    {
                      "registry-mirrors": ["https://odmcy51z.mirror.aliyuncs.com"]
                    }
                    EOF
# 3. 重启Docker服务	$ 
    systemctl daemon-reload
    service docker restart
# 4. 检查是否生效
	docker info
```

![image-20230903092051700](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903092051700.png)

### Run原理

run 命令 -->寻找是否存在image

![image-20230903092709874](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903092709874.png)

### 底层原理

Docker 是一个Cilent-Server 结构的系统，Docker的守护进程运行在主机上面。通过socket进行访问。

DockerServer接收到Docker-Client 的指令就会执行这个命令。

![image-20230903092936303](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903092936303.png)

![image-20230903093341490](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903093341490.png)

## Docker常用命令

#### 帮助命令

```shell
docker version	# 显示docker的版本信息
docker info		# 显示docker的系统信息
docker 命令 --help	
```

帮助文档：[Docker run reference | Docker Docs](https://docs.docker.com/engine/reference/run/)

#### 镜像命令

**docker images** 查看所有本地的主机上的镜像

![image-20230903094152548](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903094152548.png) 

```shell
# 解释
REPOSITORY 	镜像的仓库源
TAG			镜像的标签
IMAGE ID 	镜像的ID
CREATE 		镜像的创建时间
SIZE		大小

# 可选项
	-a, -all 	# 列出所有镜像
	-q, -quiet	# 只显示镜像ID

```

**docker search** 搜索镜像

![image-20230903095345738](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903095345738.png)

```shell
# 可选项	通过收藏来过滤 
	--filter 条件
	 docker search mysql --filter STARS=3000
```

**docker pull** 下载镜像

```shell
# 下载镜像 docker pull 镜像名[:tag]
[root@localhost docker]#  docker pull mysql
Using default tag: latest	# 如果不写tag，默认最新
latest: Pulling from library/mysql
b193354265ba: Pull complete 	# 分层下载，docker image的核心，联合文件系统
14a15c0bb358: Pull complete 
02da291ad1e4: Pull complete 
9a89a1d664ee: Pull complete 
a24ae6513051: Pull complete 
b85424247193: Pull complete 
9a240a3b3d51: Pull complete 
8bf57120f71f: Pull complete 
c64090e82a0b: Pull complete 
af7c7515d542: Pull complete 
Digest: sha256:c0455ac041844b5e65cd08571387fa5b50ab2a6179557fd938298cab13acf0dd	# 签名
Status: Downloaded newer image for mysql:latest
docker.io/library/mysql:latest	# 真实地址

# 等价于它
docekr pull docker.io/library/mysql:latest

# 指定版本下载
 [root@localhost docker]#  docker pull mysql:5.7
5.7: Pulling from library/mysql
70e9ff4420fb: Pull complete 
7ca4383b183f: Pull complete 
3e282e7651b1: Pull complete 
1ffa0e0ca707: Pull complete 
6eb790cf6382: Pull complete 
b4b277ff2929: Pull complete 
692fe4469429: Pull complete 
c0d447d97bbd: Pull complete 
99ee594517ba: Pull complete 
a9ae52de4d77: Pull complete 
66cc05a182b5: Pull complete 
Digest: sha256:2c23f254c6b9444ecda9ba36051a9800e8934a2f5828ecc8730531db8142af83
Status: Downloaded newer image for mysql:5.7
docker.io/library/mysql:5.7

```

![image-20230903100855193](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903100855193.png)

**docker rmi** 删除镜像

```shell
docker rmi -f 容器id 		# 删除指定的容器
docker rmi -f 容器id 容器id 容器id 容器id
docker rmi -f $(docker image -aq)	# 删除所有的容器
```

#### 容器命令

**下载一个centos镜像来学习**

```
docker pull centos
```

**新建容器并启动**

```shell
docker run [可选参数] image

# 参数说明
--name "Name" 		容器名字 tomcat01 tomcat02 用来区分容器
-d					后台方式运行
-it					使用交互方式运行，进入容器查看内容
-p					指定容器的端口 -p 8080:8080
		-p	ip:主机端口:容器端口
		-p	主机端口:容器端口（常用）
		-p	容器端口
		容器端口
-p 					随机指定端口


# 测试，启动并进入容器
[root@localhost docker]# docker run -it centos /bin/bash
[root@e0934d4ca01b /]# ls		# 查看容器内的centos，基础版，很多命令不全 
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

```

**列出所有运行的容器**

~~~shell
docker ps 	# 列出正在运行的容器
-a		# 列出当前正在运行的容器 + 历史运行过的容器
-n=5	# 显示最近创建的5个容器
-q 		# 只显示容器的id
~~~

![image-20230903103512942](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903103512942.png)

**退出容器**

~~~shell
exit # 容器停止并退出
Ctrl + P + Q # 容器不停止退出
~~~

**删除容器**

~~~shell
docker rm 容器id				# 删除指定的容器，不能删除正在运行的容器，要删除 rm -f
docker rm -f $(docker ps -aq)	# 删除所有的容器
docker ps -aq|xargs docker rm 	# 删除所有的容器
~~~

**启动和停止容器的操作**

~~~shell
docker start 容器id 	# 启动容器
docker restart	容器id	# 重启容器
docker stop 容器id 		# 停止正在运行的容器
docker kill 容器id 		# 强制停止正在运行的容器
~~~

#### 常用的其它命令

**后台启动容器**

~~~ shell
# docker run -d 容器名			
[root@localhost docker]# docker run -d centos
f69fed854608d6e7edd56a21b5b9b66fc52026922a98c9ffd9ca4b4f21c8ca7c

# 问题，使用docker ps 查看时发现centos已经停止了
# 原因，docker 使用后台启动容器，发现没有前台进程，就自动停止了
# nginx，容器启动后，发现直接没有提供服务，就会立刻停止
~~~

**查看日志**

~~~shell
docker logs -tf 容器id  

# 自己编写一段shell脚本
docker run -d centos /bin/sh -c "while true; do echo tyrant; sleep 1; done"

# 显示日志
-tf				# 显示日志 	
--tail number 	# 要显示的日志条数 
~~~

**查看容器中的进程信息**

~~~shell
# docker top 容器id
[root@localhost docker]# docker top 8d8156e87e33 
UID       PID        PPID       C     STIME      TTY       TIME       CMD
root     105559     105540      0     20:14      pts/0   00:00:00   /bin/bash
~~~

**查看镜像的元数据**

~~~shell
# docker inspect 容器id
~~~

进入当前正在运行的容器

~~~shell
# 容器通常是后台运行的，需要进入容器修改一些配置
# 1. docker exec -it 容器id /bin/bash

# 测试
[root@localhost docker]# docker exec -it 8d8156e87e33 /bin/bash
[root@8d8156e87e33 /]# 

# 2. docker attach 容器id
[root@localhost docker]# docker attach 8d8156e87e33 
正在执行当前的代码...

# docker exec   # 进入容器后开启一个新的终端， 可以在里面进行操作（常用）
# docker attach # 进入容器正在运行的终端
~~~

**从容器内拷贝文件到主机上**

~~~shell
docker cp 容器id:文件 复制到的路径
root@localhost docker]# docker cp 623970e76a88:/home/test.txt ./
                                               Successfully copied 1.54kB to /etc/docker/test.txt
(base) [root@localhost docker]# ls
daemon.json  test.txt
(base) [root@localhost docker]# 

# 这里是手动进行，后面将使用 -v 卷的技术，可以实现自动同步， 将容器的某个目录和主机中的某个目录打通
~~~

#### 练习

> 安装Nginx

~~~shell
# 1. 搜索镜像	docker search nginx
# 2. 拉取镜像	docker pull nginx
# 3. 运行测试	docker images

-d 后台运行
--name 命名
-p	宿主机端口:容器内部端口

# 打开端口
docker run -d --name ngnix01 -p 3344:80 nginx
# 检查是否成功
(base) [root@localhost docker]# curl localhost:3344
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>		# 这里表示成功
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

# 在外网使用ip:3344进行访问

[root@localhost docker]# docker exec -it 46e5f7ab99f5 /bin/bash
root@46e5f7ab99f5:/# where nginx
bash: where: command not found
root@46e5f7ab99f5:/# whereis nginx
nginx: /usr/sbin/nginx /usr/lib/nginx /etc/nginx /usr/share/nginx

# 进入配置文件目录
root@46e5f7ab99f5:/# cd etc/nginx
root@46e5f7ab99f5:/etc/nginx# ls
conf.d  fastcgi_params  mime.types  modules  nginx.conf  scgi_params  uwsgi_params

~~~

![image-20230903132121010](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903132121010.png)

~~~shell

~~~

暴露端口的概念

![image-20230903132643819](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903132643819.png)

>安装tomcat

~~~shell
# 官方使用,下载后就删除
docker run -it --rm tomcat:9.0

# 1. 下载
docker pull tomcat

# 2. 启动
docker run -d -p 3355:8080 --name tomcat01 tomcat

# 外网访问，测试没有问题
~~~

![image-20230903153307117](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903153307117.png)

~~~shell
# 3. 进入容器
docker exec -it tomcat01 /bin/bash

# 发现问题，1.Linux命令少了，2.没有webapps。镜像原因，默认是最小的镜像，把所有的不必要的删除
# 保证最小的可运行环境 

# 修复流程
root@1b44b9d943c4:/usr/local/tomcat# ls
bin  BUILDING.txt  conf  CONTRIBUTING.md  lib  LICENSE  logs  native-jni-lib  NOTICE  README.md  RELEASE-NOTES  RUNNING.txt  temp  webapps  webapps.dist  work
root@1b44b9d943c4:/usr/local/tomcat# cd webapps.dist
root@1b44b9d943c4:/usr/local/tomcat/webapps.dist# ls	
docs  examples  host-manager  manager  ROOT							
root@1b44b9d943c4:/usr/local/tomcat/webapps.dist# cd ..				
root@1b44b9d943c4:/usr/local/tomcat# cp -r webapps.dist/* webapps	# 将其复制到webapps
root@1b44b9d943c4:/usr/local/tomcat# cd webapps	
root@1b44b9d943c4:/usr/local/tomcat/webapps# ls						#复制成功
docs  examples  host-manager  manager  ROOT

# 重新外网访问
~~~

![image-20230903154558439](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903154558439.png)

> 思考问题：我们后面要部署项目，每次进入容器很麻烦！
>
> 解决方案：在容器外面提供一个映射路径，webapps，在外部部署，内部自动同步！
>
> 防止删除docker 容器 跑路

> 部署es + kibana

~~~shell
# es 暴露的端口很多
# es 十分耗内存
# es 的数据一般放到安全目录！挂载
# --net somenetwork ? 网络配置

# 启动 elasticsearch
docker run -d --name elasticsearch  -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.8.0

# 启动了Linux就很卡  docker stats 查看	cpu状态

# 测试一下 es 是否成功	curl localhost:9200
{
  "name" : "ac96bc87f3cf",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "kqdyoyLJREmu34PzXDb2kA",
  "version" : {
    "number" : "7.8.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "757314695644ea9a1dc2fecd26d1a43856725e65",
    "build_date" : "2020-06-14T19:35:50.234439Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
~~~

![image-20230903163219702](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903163219702.png)

~~~shell
# 增加内存限制，修改配置文件 -e 环境配置修改
docker run -d --name elasticsearch02  -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx512m" elasticsearch:7.8.0
~~~

![image-20230903164012562](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903164012562.png)

#### 可视化

portainer(先用这个)

~~~shell
docker run -d -p 8088:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --privileged=true portainer/portainer
~~~

**什么是portainer？**

Docker 图形化界面管理！ 提供一个后台面板

![image-20230903165102106](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903165102106.png)

## Docker镜像理解

### 镜像是什么？

镜像是一种轻量级、可执行的独立软件包，包含打包软件运行环境和基于运行环境开发的软件，即包含了某一个软件的全部。

所有的应用，直接打包成docker镜像，就可以直接跑起来。

如何获得镜像：

- 从远程仓库下载
- 拷贝别人的
- 自己制作DockerFile

### Docker镜像加载原理

> UnionFS(联合文件系统)

![image-20230903170946611](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903170946611.png)

> Docker镜像加载原理

![image-20230903171211013](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903171211013.png)
### 分层原理
![image-20230903172000608](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903172000608.png)

> 容器层是可写的，即是由我们创建的

![image-20230903172245881](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903172245881.png)

> 我们的操作不会影响最初的镜像，如下图，pull过来的为只读，run后的为我们自己的镜像

![image-20230903172440161](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903172440161.png)

### commit 镜像

~~~shell
docker commit 提交容器成为一个新的副本

# 命令和git原理类似
docker commit -m="提交的描述信息" -a="作者" 容器id 目标镜像名:[TAG]
~~~

**实战测试**

~~~shell
# 1. 启动一个默认的tomcat

# 2. 发现这个tomcat没有webapps应用，镜像的原因，官方的镜像默认没有webapps

# 3. 自己拷贝到相应的文件
root@21bd70963221:/usr/local/tomcat# ls
bin  BUILDING.txt  conf  CONTRIBUTING.md  lib  LICENSE  logs  native-jni-lib  NOTICE  README.md  RELEASE-NOTES  RUNNING.txt  temp  webapps  webapps.dist  work
# 拷贝
root@21bd70963221:/usr/local/tomcat# cp -r webapps.dist/* webapps
root@21bd70963221:/usr/local/tomcat# cd webapps
root@21bd70963221:/usr/local/tomcat/webapps# ls
docs  examples  host-manager  manager  ROOT

# 4. 通过commit提交这个镜像，我们以后就使用这个镜像
docker commit -a="tyrant" -m="add webapps" 容器id 名字:[TAG]
~~~

![image-20230903180605132](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230903180605132.png)

> 可以通过提交这个容器来作为快照

## 容器数据卷

### 什么是容器数据卷

**docker** 将应用和环境打包成一个镜像！

数据？如果将数据放在容器中，那么将容器删除相当于删库跑路！

容器之间可以有一个数据共享的技术！Docker产生数据，同步到本地！

这就是卷技术！目录的挂载，将我们容器内的目录，挂载到Linux！

![image-20230904103212099](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904103212099.png)

### 使用数据卷

> 方式一：直接使用命令来挂载  -v

~~~shell
docker run -it -v 主机目录:容器内目录

# 测试 	
[root@localhost tyrant]# docker run -it -v /home/ceshi:/home centos /bin/bash

# 启动后 通过 docker inspect 容器id
~~~

![image-20230904111207979](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904111207979.png)

> 在本地或者容器上修改相应的文件，会自动同步

![image-20230904112240129](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904112240129.png)

### 安装MySQL

官方文档：[mysql - Official Image | Docker Hub](https://hub.docker.com/_/mysql)

~~~shell
# 获取镜像
docker pull mysql:5.7

# 配置密码
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

# 挂载
docker run -d  -p 3310:3306 -v /home/mysql/conf:/home/mysql/conf.d -v /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql01 mysql:5.7

# 数据库里面的数据 cd /home/mysql/data
# 在本地创建也会影响容器，就是一个映射关系
~~~

![image-20230904124807006](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904124807006.png)

删除容器	docker rm -f mysql01   , 本地数据也不会消失

具名和匿名挂载

~~~shell
# 匿名挂载
-v 容器内路径！
docker run -d -P --name nginx01 -v /etc/nginx nginx

# 查看所有的volume的情况
[root@localhost data]# docker volume ls
DRIVER    VOLUME NAME
local     1dedd6eeeff2baca000dda850fb98118e57180bb09ab3082ca67b502bcbc98a3
local     1fe6bf1ff66be85e894bf3918f5db220fc284e05869b6d5948a41e2e612b052b

# 这就是匿名挂载， 我们只写了容器内的路径，没有写容器外的路径

# 具名挂载
docker run -d -P --name nginx02 -v juming-nginx:/etc/nginx nginx

[root@localhost data]# docker volume ls
DRIVER    VOLUME NAME
local     1dedd6eeeff2baca000dda850fb98118e57180bb09ab3082ca67b502bcbc98a3
local     1fe6bf1ff66be85e894bf3918f5db220fc284e05869b6d5948a41e2e612b052b
local     juming-nginx

# 通过 -v 卷名:容器内路径
# 查看一下这个卷
~~~



![image-20230904145948675](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904145948675.png)

所有的docker容器内的卷，没有指定目录的情况下都是在	`/var/lib/docker/volumes/xxx/_data`

![image-20230904151449939](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904151449939.png)

我们通过具名挂载可以方便的找到我们的一个卷，大多数情况下使用`具名挂载`

~~~shell
# 如何确定是具名挂载还是匿名挂载，还是指定路径挂载！
-v 容器内路径		# 匿名挂载
-v 卷名:容器内路径		# 具名挂载
-v /宿主机路径:容器内路径		# 指定路径挂载	
~~~

扩展：

~~~shell
# 通过 -v 容器内路径:ro rw 改变读写权限
ro readonly # 只读
rw	readwrite # 可读可写

docker run -d -P --name nginx -v juming-nginx:/etc/nginx:ro nginx  
docker run -d -P --name nginx -v juming-nginx:/etc/nginx:rw nginx

# ro 说明这个路径只能通过宿主机来操作，容器内部是无法操作！
~~~

### 初始DockerFile commit

DockerFile就是用来构建docker镜像的构建文件！命令脚本！

通过这个脚本可以生成镜像，镜像是一层一层的

~~~shell
# 创建一个dockerfile 文件, 名字随意，最好就是dockerfile 
# 文件中的内容	指令（大写）	参数
FROM centos
VOLUME ["volume01", "volume02"]				
CMD echo "-----end------"
CMD /bin/bash
# 这里的每个命令就是镜像的一层！

# docker build -f dockerfile1 -t tyrant/centos:1.0 .
~~~



![image-20230904160411385](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904160411385.png)

启动自己的镜像：

~~~shell
docker run -it 容器id /bin/bash
~~~



![image-20230904161337636](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904161337636.png)

查看它们的挂载的路径：

![image-20230904161949452](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904161949452.png)

> 这种情况比较常用，我们一般建立属于自己的镜像
>
> 假设构建镜像时没有挂载卷，要手动镜像挂载	-v 卷名：容器内路径！

### 数据卷容器

多个mysql同步数据！

![image-20230904162515435](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904162515435.png)



~~~shell
# 通过 --volumes-from 来进行
docker run -it --name docker02 --volumes-from docker01 tyrant/centos:1.0
~~~



![image-20230904165508517](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904165508517.png)

> 测试：可以删除docker01，docker02还有这个文件
>
> 原因：这个volume01 是在本地有挂载的，删除容器不影响本地
>
> 我的理解：它们之间的数据共享相当于就是将其挂载的内容那些进行了复制，其本质都是本地保存

### 多个mysql实现数据共享

~~~shell
docker run -d  -p 3310:3306 -v /home/mysql/conf.d -v /var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql01 mysql:5.7

docker run -d  -p 3310:3306 -e MYSQL_ROOT_PASSWORD=123456 --name mysql02 mysql:5.7 --volumes-from mysql01 mysql:5.7

# 这个时候，可以实现两个容器数据同步
~~~



结论：

容器之间配置信息的传递，数据卷的生命周期一直持续到没有容器使用为止！

但是一旦持久化本地，这个时候，本地的数据是不会删除的！



## DockerFile

### DockerFile介绍

DockerFile就是用来构建docker镜像的构建文件！命令脚本！

构建步骤：

1. 编写一个dockerfile 文件
2. docker build 构建一个镜像
3. docker run 运行镜像
4. docker push 发布镜像（DockerHub，阿里云镜像仓库！）

官方操作：

![image-20230904172222974](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904172222974.png)



![image-20230904172231265](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904172231265.png)

很多官方镜像都是基础包，很多功能都没有，我们通常搭建自己的镜像！

官方既然可以制作镜像，那我们也可以制作自己的镜像！

### DockerFile构建过程

**基础知识：**

1. 每个保留关键字(指令) 都必须是大写字母！

2. 执行顺序从上到下

3. #表示注释

4. 每一个指令都会创建并提交一个新的镜像层，并提交！

   ![image-20230904175059323](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904175059323.png)

   dockerfile 是面向开发的，我们以后要发布项目，做镜像，就要编写dockerfile文件，这个文件十分简单！

   dockerfile 逐渐成为了企业交付的标准，必须掌握！

   步骤：开发--》部署 --》 运维。。。缺一不可！

   DockerFile：构建文件，定义了一切的步骤，源代码

   DockerImages: 通过DockerFile构建生成的镜像，最终发布和运行的产品！

   Docker容器：容器就是镜像运行起来提供服务器

### DockerFile指令

~~~shell
FROM 			# 基础镜像，一切从这里构建
MAINTAINER		# 镜像是谁写的，姓名 + 邮箱
RUN 			# 镜像构建时需要执行的命令
ADD				# 将本地文件或目录复制到容器中
WORKDIR			# 镜像的工作目录，如/bin/bash
VOLUME			# 挂载的目录
EXPOSE			# 保留的端口配置
CMD				# 指定这个容器启动的时候要运行的命令,只有最后一个会生效，可被替代
ENTRYPOINT		# 指定这个容器启动的时候要运行的命令,可以追加命令
ONBUILD			# 当运行一个被继承的DockerFile，就会运行ONBUILD 的指令。触发指令
COPY			# 类似ADD，将文件拷贝到镜像中
ENV				# 构建的时候设置环境变量
~~~



![image-20230904181902841](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904181902841.png)



### 实战测试

Docker Hub 中的99%镜像都是从这个基础镜像过来的FROM scratch，然后配置需要的软件和配置来进行的构建

![image-20230904172231265](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904172231265.png)

> 创建一个自己的centos

~~~shell
# 1. 编写DockerFile文件
FROM centos:7
MAINTAINER tyant<173001344@qq.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN yum clean all

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "-----end----"
CMD /bin/bash

# 2. 搭建	docker build -f DockerFile文件路径 -t 镜像名:[TAG]
docker build -f mydockerfile-centos -t mycentos:0.1 .

# 3. 测试运行
~~~



![image-20230904190941910](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904190941910.png)

![image-20230904191506367](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904191506367.png)

我们可以列出本地进行的变更历史：

<img src="C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230904192213230.png" alt="image-20230904192213230" style="zoom:67%;" />我们拿到别人的镜像可以研究一下

> CMD 和 ENTRYPOINT 区别

~~~shell
CMD				# 指定这个容器启动的时候要运行的命令,只有最后一个会生效，可被替代
ENTRYPOINT		# 指定这个容器启动的时候要运行的命令,可以追加命令
~~~

测试CMD

~~~shell
# 创建dockerfile
[root@localhost dockerfile]# cat dockerfile-cmd-test 
FROM centos:7
CMD ["ls","-a"]
# 建立
[root@localhost dockerfile]# docker build -f dockerfile-cmd-test -t cmdtest .

# 运行
(base) [root@localhost dockerfile]# docker run cmdtest
.
..
.dockerenv
anaconda-post.log
bin
dev
etc

# 想追加一个命令 -l ls -al

(base) [root@localhost dockerfile]# docker run cmdtest -l
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "-l": executable file not found in $PATH: unknown.

# cmd 的清理下，-l 替换了CMD["ls", "-a"]命令，不是命令所以报错！
~~~

测试ENTRYPOINT

~~~shell
# 创建
(base) [root@localhost dockerfile]# cat dockerfile-cmd-entrypoint 
FROM centos:7
ENTRYPOINT ["ls","-a"]
# 建立
(base) [root@localhost dockerfile]# docker build -f dockerfile-cmd-entrypoint -t entorypoint-test .

# 不同点
[root@localhost dockerfile]# docker run entorypoint-test -l
total 12
drwxr-xr-x.   1 root root     6 Sep  4 11:43 .
drwxr-xr-x.   1 root root     6 Sep  4 11:43 ..
-rwxr-xr-x.   1 root root     0 Sep  4 11:43 .dockerenv
-rw-r--r--.   1 root root 12114 Nov 13  2020 anaconda-post.log
lrwxrwxrwx.   1 root root     7 Nov 13  2020 bin -> usr/bin
drwxr-xr-x.   5 root root   340 Sep  4 11:43 dev


~~~

DockerFile 中很多命令都十分相似，我们需要了解它们的区别，最好对比学习。

### 实战：Tomcat镜像

1. 准备工作：

> 安装tomcat和jdk
>
> wget https://download.oracle.com/java/20/latest/jdk-20_linux-x64_bin.tar.gz
>
> wget --no-check-certificate https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz

![image-20230905090335906](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905090335906.png)

2. 编写DockerFile文件，官方命名` Dockerfile`，bulid 会自动寻找这个文件，就不用 -f 指定！ 

~~~shell
FROM centos:7
MAINTAINER tyrant<173001344@qq.com>

COPY readme.txt /usr/local/readme.txt

ADD jdk-20_linux-x64_bin.tar.gz /usr/local/
ADD apache-tomcat-9.0.80.tar.gz  /usr/local/

RUN yum -y install vim

ENV	MYPATH /usr/local
WORKDIR $MYPATH

ENV JAVA_HOME /usr/local/java
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.80
ENV CATALINA_BASH /usr/local/apache-tomcat-9.0.80
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin

EXPOSE 8080

CMD /usr/local/apache-tomcat-9.0.80/bin/startup.sh && tail -F /usr/local/apache-tomcat-9.0.80/bin/logs/catalina.out
~~~

3. 构建镜像

   ~~~shell
   # docker build -t diytomcat .
   
   # 运行
   docker run -d -p 9090:8080 --name tyranttomcat -v /home/tyrant/build/tomcat/test:/usr/local/apache-tomcat-9.0.80/webapps/test -v /home/tyrant/build/tomcat/tomcatlogs/:/usr/local/apache-tomcat-9.0.80/logs diytomcat
   
   # 我在这里出现了错误，但是我没有办法解决：它告诉我没有startup.sh,还有一个原因在于我没有学过java和tomcat，对它们的环境变量和文件结构并不清楚
   (base) [root@localhost tomcat]# docker run -it -p 9090:8080 --name tyrant -v /home/tyrant/build/tomcat/test:/usr/local/apache-tomcat-9.0.80/webapps/test -v /home/tyrant/build/tomcat/tomcatlogs/:/usr/local/apache-tomcat-9.0.80/logs diytomcat
   /usr/local/apache-tomcat-9.0.80/bin/startup.sh: line 24: uname: command not found
   /usr/local/apache-tomcat-9.0.80/bin/startup.sh: line 41: dirname: command not found
   Cannot find /catalina.sh
   The file is absent or does not have execute permission
   This file is needed to run this program
   
   ~~~

4. 启动镜像
5. 访问测试
6. 发布项目（做了挂载，直接写在本地就行）

~~~shell
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
　　　    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
  
</web-app>
~~~

~~~shell
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
Hello World!<br/>
<%
out.println("你的 IP 地址 " + request.getRemoteAddr());
%>
</body>
</html>

~~~



### 发布自己的镜像

> DockerHub

1. 地址 [Docker Hub Container Image Library | App Containerization](https://hub.docker.com/)

2. 在我们的服务器上提交自己的镜像

~~~shell
 [root@localhost tomcat]# docker login -u tyrantyf
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
~~~

3. 登陆成功后，就可以提交镜像

~~~shell
# push 到自己的镜像服务器上
(base) [root@localhost tomcat]# docker push diytomcat
Using default tag: latest
The push refers to repository [docker.io/library/diytomcat]
5f70bf18a086: Preparing 
8854ea0c4995: Preparing 
99b72c322c4b: Preparing 
8bf2debbd30f: Preparing 
1e48ab17b2ff: Preparing 
174f56854903: Waiting 
denied: requested access to the resource is denied # 拒绝

# 注意：这里有坑，你push的文件必须与你的仓库名一致

# 将本地镜像添加一个标签: docker tag 本地镜像:[tag] 远程仓库名[tag]

# 然后，再重新上传这个镜像: docker push 远程仓库名[tag]
~~~

![image-20230905125943517](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905125943517.png)

> 将镜像传到阿里云、腾讯云上

1. 登录相应的云

2. 找到容器镜像服务
3. 创建命名空间

![image-20230905165117869](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905165117869.png)

4. 创建容器镜像

![image-20230905165131560](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905165131560.png)

5. 浏览云

![image-20230905165235832](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905165235832.png)



### 小结

![](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905165506832.png)



![image-20230905165749719](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905165749719.png)




## Docker 网络

### 理解Docker0

> 清空所有的环境

![image-20230905170318439](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905170318439.png)

三个网络

> 问题：docker 如何处理容器网络访问的？

![image-20230905170539120](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905170539120.png)

~~~shell
# 启动一个tomcat
docker run -d -P --name tomcat01 tomcat

# 查看容器的内部网络地址 ip addr, 发现会得到如下内容 74: veth57282ca@if73
74: veth57282ca@if73: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether 0a:dc:e5:3b:11:a5 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::8dc:e5ff:fe3b:11a5/64 scope link 
       valid_lft forever preferred_lft forever

# 这里不能看到具体的ip地址，原课程是通过 docker exec -it tomcat01 ip addr 查看 如下图
~~~

![image-20230905180440381](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905180440381.png)

~~~shell
# 所以我就通过 docker inspect tomcat01 找到了如下信息
~~~

![image-20230905180544752](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905180544752.png)

~~~shell
# 通过 ping 进行连接，发现没有问题
[root@localhost local]# ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.251 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.055 ms
~~~

> 原理

1. 我们没启动一个docker容器，docker就会给docker容器分配一个ip，我们只要安装了docker，就会有一个网卡docker0桥接模式，使用的技术是evth-pair技术！
2. 再启动一个容器测试，发现又多了一对网卡！

​	![image-20230905181225501](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230905181225501.png)

~~~shell
# 我们发现这个容器带来网卡，都是一对一对的
# evth-pair 就是一对的虚拟设备接口，它们都是成对的出现，一端连着协议，一端彼此相连
# 正因为这个特性，evth-pair 充当一个桥梁，连接各种虚拟设备的
~~~

3. 我们来测试tomcat01和tomcat02是否可以ping通

~~~shell
# 由于和上面的问题相似，我没有办法使用ping，所以我采用了curl来进行访问

# 查看tomcat02的ip，进入tomcat01来curl这个ip的对应端口
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tomcat02
docker exec -it tomcat01 /bin/bash
curl 172.17.0.2:8080
~~~

![image-20230906090724351](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906090724351.png)

![image-20230906091140163](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906091140163.png)

结论：tomcat01和tomcat02 是公用的一个路由器，docker0

所有的容器不指定网络的情况下，都是docker0路由，docker会给我们分配一个默认的ip



> 小结

Docker 使用的是Linux的桥接，宿主机是一个Docker容器的网桥 docker0。

![image-20230906091447865](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906091447865.png)

Docker 中所有的网络接口都是虚拟的。虚拟的转发效率高！（内网传递文件）

只要容器删除，对应网桥就没有了！



### --link

> 思考一个场景，我们编写了一个微服务，database=ip:端口，项目不重启，数据库ip换掉了，我们希望可以处理这个问题，可以通过名字来访问容器？

~~~shell
# 具体如下，因为新的tomcat版本已经不支持ping，所以我没办法测试
~~~



![image-20230906092913823](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906092913823.png)

~~~shell
# 这里将直接查看它们的--link的结果，就不再实操了
# docker run -d -P --name tomcat03 --link tomcat02 tomcat
# 查看 docker exec -it tomcat03 cat /etc/hosts
~~~

![image-20230906094011062](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906094011062.png)

本质探究：--link 就是我们在hosts配置中增加了一个 172.17.0.2      tomcat02 88d0d55f5bfa

现在已经不建议使用--link

自定义网络，不使用docker0！

docker0 不支持容器名连接访问！



### 自定义网络（容器互联）

> 查看所有的docker 网络

![image-20230906094505653](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906094505653.png)

**网络模式**

bridge：桥接模式 docker 大桥（默认），`0.2 ——》 0.1 《——0.3`           0.2和0.3只能通过0.1 访问

none: 不配置网络

host： 和宿主机共享网络

container： 容器内网络连通！（用的少，不仅建议，局限很大）

**测试**

~~~shell
# 我们直接启动的命令， --net bridge， 而这个就是我们的docker0
docker run -d -P --name tomcat01 tomcat
docker run -d -P --name tomcat01 --net bridge tomcat

# docker0 特点: 默认，域名不能访问， --link 可以打通

# 我们自定义网络
# --driver bridge 桥接模式
# --subnet 192.168.0.0/16 	子网地址 可以访问192.168.0.2 ~ 192.168.255.255
# --gateway 192.168.0.1 	网关，路由器的地址
docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet

# 查看我们的网络	docker network inspect mynet
~~~

![image-20230906100432489](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906100432489.png)

~~~shell
# 现在创建两个容器，来测试
docker run -d -P --name tomcat-net-01 --net mynet tomcat
docker run -d -P --name tomcat-net-02 --net mynet tomcat
# 再次查看我们的自定义网络
docker network inspect mynet

# 删除网络
docker network rm 名字
~~~

![image-20230906101211910](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906101211910.png)

![image-20230906100609991](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906100609991.png)

我们自定义的网络docker都已经帮我们维护好了对应的关系，推荐我们平时这样使用网络！



好处：

redis - 不同的集群使用不同的网络，保证集群是安全健康的

mysql -  不同的集群使用不同的网络，保证集群是安全健康的

![image-20230906101529559](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906101529559.png)



### 网络连通

![image-20230906102024175](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906102024175.png)

~~~shell
# 测试打通	tomcat01 -> mynet

# 连通之后就是将 tomcat01 放到了 mynet 网络下	docker network connect 网络 容器	
docker network connect mynet tomcat01

# 一个容器，两个ip地址！	公网ip，私网ip
~~~

![image-20230906102601728](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906102601728.png)

![image-20230906102148115](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906102148115.png)

> 结论：假设要跨网络，就需要使用 docker network connect 来连通！



### 实战：部署Redis集群

![image-20230906102831613](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906102831613.png)

shell脚本！

~~~shell
# 创建网卡
docker network create redis --subnet 172.38.0.0/16

# 通过脚本创建6个redis配置
for port in $(seq 6); \
do \
mkdir -p /mydata/redis/node-${port}/conf
touch /mydata/redis/node-${port}/redis.conf
cat << EOF >/mydata/redis/node-${port}/conf/redis.conf
port 6379
bind 0.0.0.0
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
cluster-announce-ip 172.38.0.1${port}
cluster-announce-port 6379
cluster-announce-bus-port 16379
appendonly yes
EOF
done

# 下面为这6个redis配置
~~~

![image-20230906104006935](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906104006935.png)

~~~shell
# 接下使用模板
docker run -p 637${port}:6379 -p 1637${port};16379 --name redis-${port} \
-v /mydata/redis/node-${port}/data:/data \
-v /mydata/redis/node-${port}/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.1${port} redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf; \

# 可以直接使用循环
for port in $(seq 6); \
do \
docker run -p 637${port}:6379 -p 1637${port}:16379 --name redis-${port} \
-v /mydata/redis/node-${port}/data:/data \
-v /mydata/redis/node-${port}/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.1${port} redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf 
done

# 也通过修改上面的port来启动不同的redis
docker run -p 6371:6379 -p 16372:16379 --name redis-1 \
-v /mydata/redis/node-1/data:/data \
-v /mydata/redis/node-1/conf/redis.conf:/etc/redis/redis.conf \
-d --net redis --ip 172.38.0.11 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf

# 进入某个redis
docker exec -it redis-1 /bin/sh

# 创建集群
redis-cli --cluster create 172.38.0.11:6379 172.38.0.12:6379 172.38.0.13:6379 172.38.0.14:6379 172.38.0.15:6379 172.38.0.16:6379 --cluster-replicas 1

# 下面为创建成功
/data # redis-cli --cluster create 172.38.0.11:6379 172.38.0.12:6379 172.38.0.13:6379 172.38.0.14:6379 172.38.0.15:6379 172.38.0.16:6379 --cluster-replicas 1
>>> Performing hash slots allocation on 6 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
Adding replica 172.38.0.15:6379 to 172.38.0.11:6379
Adding replica 172.38.0.16:6379 to 172.38.0.12:6379
Adding replica 172.38.0.14:6379 to 172.38.0.13:6379
M: 8cee94aa999fc8ce6e947bde63010de85045a2e8 172.38.0.11:6379
   slots:[0-5460] (5461 slots) master
M: 01e683cb5114b8b640bf8ac58b46106bf3093b79 172.38.0.12:6379
   slots:[5461-10922] (5462 slots) master
M: afeee998b890f75838f14d976eafe0aecd5eb959 172.38.0.13:6379
   slots:[10923-16383] (5461 slots) master
S: 9edd27160848b6fa236b2d583abe91b3d492af35 172.38.0.14:6379
   replicates afeee998b890f75838f14d976eafe0aecd5eb959
S: 5b45fb581517b0b0bf042169f0cc22e829cf014c 172.38.0.15:6379
   replicates 8cee94aa999fc8ce6e947bde63010de85045a2e8
S: e67e3870fe2dd06d198072dd9c5841b8804801aa 172.38.0.16:6379
   replicates 01e683cb5114b8b640bf8ac58b46106bf3093b79
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
.....
>>> Performing Cluster Check (using node 172.38.0.11:6379)
M: 8cee94aa999fc8ce6e947bde63010de85045a2e8 172.38.0.11:6379
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
M: 01e683cb5114b8b640bf8ac58b46106bf3093b79 172.38.0.12:6379
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
S: 9edd27160848b6fa236b2d583abe91b3d492af35 172.38.0.14:6379
   slots: (0 slots) slave
   replicates afeee998b890f75838f14d976eafe0aecd5eb959
S: 5b45fb581517b0b0bf042169f0cc22e829cf014c 172.38.0.15:6379
   slots: (0 slots) slave
   replicates 8cee94aa999fc8ce6e947bde63010de85045a2e8
M: afeee998b890f75838f14d976eafe0aecd5eb959 172.38.0.13:6379
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
S: e67e3870fe2dd06d198072dd9c5841b8804801aa 172.38.0.16:6379
   slots: (0 slots) slave
   replicates 01e683cb5114b8b640bf8ac58b46106bf3093b79
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
~~~

> 接下来是简单的redis使用

![image-20230906113135193](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906113135193.png)

> 使用docker后，所有的技术都简单起来了。

![image-20230906113832196](C:\Users\Tyrant\AppData\Roaming\Typora\typora-user-images\image-20230906113832196.png)

## SpringBoot 微服务打包Docker镜像

1. 构架SpringBoot项目
2. 打包应用
3. 编写dockerfile

~~~shell
FROM java:8

COPY *.jar /app.jar

CMD ["--server".port=8080"]

EXPOSE 8080

ENIRYPOINT ["java","-jar","app.jar"]
~~~

4. 构建镜像

5. 运行发布

~~~shell
# 可以使用curl进行检查
curl localhost:端口/路径
~~~





以后我们使用Docker之后，给别人交付的就是一个镜像！

 
