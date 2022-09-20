# hniu-surfing-internet
HNIU 校园网的另一种网上冲浪解决方案, 可适用于任何 Linux 架构的服务器
- 路由器 **OpenWrt** 固件自动重连
- **Termux** 自动重连
- 支持 Python 登陆
## 如何使用
```shell
curl -LJO https://cdn.jsdelivr.net/gh/Ayouuuu/hniu-surfing-internet@main/run.sh
bash run.sh
# 输入 0 默认安装
请选择安装模式
0) 默认: 初始化
1) 设置账户信息
2）登陆
3) 登出
4) 更新脚本
```
安装完成之后输入 `hniu` 可快捷进入管理,快捷管理无法使用，可以输入 `base run.sh` 进行管理

## 使用技巧
Linux 可以采用 Crontab 设置定时任务进行自动重连  
Windows 系统可以使用自带的创建任务进行联网检查,只需要写一个 .bat 脚本使用 vbs 后台运行即可,运行路径要填绝对路径  
login.bat 文件
```bash
E:
py E:\login-hniu-net.py
```
login.vbs 文件
```text
Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c login.bat",0
```


### 进阶
```shell
git clone https://github.com/MochiParty/hniu-surfing-internet.git
```
然后根据自己的实际情况去选择相应的脚本,支持多账户的脚本需要配置 `accounts.txt` 帐号和密码
|脚本名|介绍|多账户|
|:---|:---|:---:|
|hniu-wifi-login|只会对名称为 HNIU 的 Wifi 进行登陆验证|✔
|openwrt-autologin|适用于 OpenWrt 固件的脚本(并不|✔
|login.sh|普普通通的登陆脚本(鶸爆了|✖
|login-hniu-net.py|Python 语言的登陆脚本,自带网络情况检测|✔

## 注意事项
账户由 **用户名**+**运行商** 组成
```text
校园网: 直接就是用户名,不需要后缀
电信: 123456@cmcc
联通: 123456@unicom
电信: 123456@telecom
```


## 交流群
QQ群: HNIUer | 707175908 [[link](https://jq.qq.com/?_wv=1027&k=qeqLaXhG)]
