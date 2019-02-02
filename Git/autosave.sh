LOGFILE="/User/xihajun/Documents/Data Science/data-science-toolbox-kate-syd-jun/Git/upload.log"
git add --all
git commit -m "autosave"
{
   git push
   echo "`date +%H:%M:%S : file uploaded" >> $LOGFILE
}||{
   git pull --rebase
   git push
   echo "`date +%H:%M:%S : file reloaded and uploaded" >> $LOGFILE
}
