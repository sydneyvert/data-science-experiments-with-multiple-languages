LOGFILE=./upload.log
git add --all
git commit -m "autosave"
{
   git push
   echo "$(date) : file uploaded" >> $LOGFILE
}||{
   git pull --rebase
   git push
   echo "`date +%H:%M:%S` : file reloaded and uploaded" >> $LOGFILE
}
