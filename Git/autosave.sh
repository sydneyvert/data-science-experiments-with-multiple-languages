LOGFILE=./upload.log
git checkout master
git add .
git commit -m "autosave"
#try catch function 
#write in this way {code1&&}||{code2}
read -p "请选择相应的发行版本系统（输入数字序号）：" number
if [ "$number" == "" ]; then
  echo "未选择任何发行版本，脚本退出"
  exit 1
{
   git push&&
   echo "$(date) : file uploaded" >> $LOGFILE
}||{
   git pull --rebase
   git push
   echo "$(date) : file reloaded and uploaded" >> $LOGFILE
}
