BASE_PATH=$(cd `dirname $0`;pwd)
datetime=$(date +[%Y-%m-%d_%H:%M:%S])
code=`curl -i -m 10 -o /dev/null -s -w %{http_code}  http://10.253.0.1/F.html`;
echo "successfully logout! $code"
echo "$datetime logout" >> "$BASE_PATH/log.log"