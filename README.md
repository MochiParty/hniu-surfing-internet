# hniu-surfing-internet
HNIU 校园网的另一种网上冲浪解决方案, 可适用于任何 Linux 架构的服务器
- 路由器 **OpenWrt** 固件自动重连
- **Termux** 自动重连
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
