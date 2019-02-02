# How to use git to upload the code
## From: https://youtu.be/I8gZlctY5no
After installing git, we are able to upload it by terminal command.
### Git clone
Firstly, create a respositories and clone it by using `git clone yourgitaddress` which can be found at the homepage of every respositories
### Coding
After that, you are able to change the local files and enjoy your coding.
### Update the files
In order to update files, we should do as follows:<br>
1. `git add --all`<br>
2. `git commit -m "information"`<br>
(skip: look at your status by using `git status`)<br>
3. `git push` to push the files (need to login in at the first time).<br>
4. if you fail to upload the codes, try to update your version of the code first by using `git pull --rebase`
## Multiuser
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author
    
# Notes
## Permission denied
    sudo chmod 755 'filename'
## Automatically upload every two hours
    crontab -e
    0 0-23/2 * * * bash "/Users/username/Documents/Data Science/data-science-toolbox-kate-syd-jun/Git/autosave.sh"
