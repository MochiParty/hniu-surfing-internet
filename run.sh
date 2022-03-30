BASE_PATH=$(cd `dirname $0`;pwd)

setting(){
read -p "请选择运营商 
0. 校园网 1. 移动 2. 电信 3. 联通 
" isp

case $isp in
	1 ) isp="@cmcc";;
	2 ) isp="@telecom";;
	3 ) isp="@union";;
	*) isp="";;
esac

read -p "请输入账号: " user
read -p "请输入密码: " password

# 覆盖原账号 密码
sed -i "4c user=\"$user$isp\"" "$BASE_PATH/login.sh"
sed -i "5c pwd=\"$password\"" "$BASE_PATH/login.sh"
echo "修改用户成功
账号: $user$isp
密码: $password"
}

addCrontab(){
crontab="/etc/crontabs/root"
echo "*/5 * * * * cd $BASE_PATH && ./login.sh" >> $crontab
echo "添加定时任务成功,重启定时任务"
/etc/init.d/cron restart
crontab -l
}

downloadScript(){
curl -LJO "https://cdn.jsdelivr.net/gh/Ayouuuu/hniu-surfing-internet@main/login.sh"
curl -LJO "https://cdn.jsdelivr.net/gh/Ayouuuu/hniu-surfing-internet@main/logout.sh"
}

update(){
echo "正在更新软件..."
opkg update
echo "更新软件成功！正在安装相关依赖"
opkg install curl cronie
echo "依赖安装成功,下载主程序中"
downloadScript
echo "主程序下载成功!"
echo "alias hniu='bash "$BASE_PATH/run.sh"'" >> ~/.bashrc
source ~/.bashrc
echo "添加环境变量成功! 输入 hniu 可快捷打开菜单"
}

login(){
bash "$BASE_PATH/login.sh"
}

logout(){
bash "$BASE_PATH/logout.sh"
}

run(){
read -p "请选择安装模式
0) 默认: 初始化
1) 设置账户信息
2）登陆
3) 登出
4) 更新脚本
" mode
case $mode in
	4 )
		downloadScript;;
	3 )
		logout;;
	2 )
		login;;
	1 )
		setting;;
	0 )
		update
		addCrontab;;
	*)
		exit 0;;
esac
}

run
