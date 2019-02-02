git add --all
git commit -m "autosave-j"
{
   git push
}||{
   git pull --rebase
   git push
}
