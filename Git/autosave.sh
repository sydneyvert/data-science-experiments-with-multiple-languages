git add --all
git commit -m "autosave-j"
try
   git push
catch
   git pull --rebase
   git push

