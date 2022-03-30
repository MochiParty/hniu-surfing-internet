BASE_PATH=$(cd `dirname $0`;pwd)
datetime=$(date +[%Y-%m-%d_%H:%M:%S])
# 账号 密码
user=""
pwd=""

checkCode=`curl -o /dev/null -s -w %{http_code} baidu.com`;

if [[ "$checkCode" != "200" ]]; then
    content=`curl -m 10 -s -w "Code: %{http_code}\n" -d "DDDDD=$user&upass=$pwd&0MKKey=123456" http://10.253.0.1/a70.html`;
	title=`echo "$content" | grep '<title>(.*)</title>' -E`
	if [[ ${#title} == 22 ]]; then
		msg="$datetime Successfully login,code: $code title: $title"
		echo $msg
		echo $msg >> "$BASE_PATH/log.log"
	else 
		msg="$datetime can't login plz check your user and pwd,title: $title"
		echo $msg
		echo $msg >> "$BASE_PATH/log.log"
	fi
else echo 'already login...'
fi