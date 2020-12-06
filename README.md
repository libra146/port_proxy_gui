## Windows端口转发命令的GUI版本

### 简介

port_proxy_gui 为 Windows 端口转发的 GUI 版本，为了解决每次需要用到 Windows 端口转发时需要敲很长的命令的问题。

工具界面使用 Python 和 PySide2 编写，跨平台运行，但是由于所使用的端口转发命令仅限于 Windows，所以在其他平台运行没有意义。😂😂

工具所使用到的依赖为：

| 依赖        | 版本号 |
| ----------- | ------ |
| PySide2     | 5.15.2 |
| netifaces   | 0.10.9 |
| pyinstaller | 4.1    |

工具主界面长这样：

![](img/main.png)

### 软件原理

依赖于 Windows 的 IP Helper 服务，在启动时软件会自动检测服务状态， IP Helper 服务状态显示在标题上，如未开启对应服务，请自行开启。

通过 `netsh interface portproxy` 命令设置和删除端口转发规则，`netsh interface portproxy` 命令要求使用管理员权限运行，所以本工具也要使用管理员权限运行。

### 使用教程

#### 添加新的端口转发规则

![](img/add.gif)

### 修改之前的端口转发规则

![](img/edit.gif)

### 删除端口转发规则

![](img/del.gif)