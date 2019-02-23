# Install requirements

All the requirements are in requirements.txt file, you can either use `pip install -r requirements.txt` to get the package installed or do some set up things as follows:
 
## Set up 

If we have Jupyter in your requirements.txt and we activate that environment (Virtualenv), install, and run Jupyter, we'll have all the specific versions we want. So:

     python3 -m venv venv
     source venv/bin/activate #(different command on Windows)
     pip install -r requirements.txt
     jupyter notebook #or jupyter lab

## Something went wrong?

If there are some errors for intalling enchant package in macbook, hope this is helpful. (from [stackoverflow](https://stackoverflow.com/questions/32826466/pyenchant-installation-on-os-x-yosemite))
     
     brew install enchant # install enchant first ; yum install enchant for linux
     pip install pyenchant
     
# Online jupyter version

[Online Notebook](http://ls.xihajun.cn/Project.html) shows our results and don't need to run it for years.
