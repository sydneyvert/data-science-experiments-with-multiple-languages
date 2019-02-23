# Install requirements

All the requirements are in requirements.txt file, you can either use `pip install -r requirements.txt` to get the package installed or do some set up things as follows:

If there are some errors for intalling enchant package in macbook, hope this is helpful. (from [stackoverflow](https://stackoverflow.com/questions/32826466/pyenchant-installation-on-os-x-yosemite))
     
     brew install enchant # install enchant first ; yum install enchant for linux
     pip install pyenchant
     
## Set up

If you have Jupyter in your requirements.txt and you activate that environment (I recommend Virtualenv), install, and run Jupyter, you'll have all the specific versions you want. So:

     python3 -m venv venv
     source venv/bin/activate #(different command on Windows)
     pip install -r requirements.txt
     jupyter notebook #or jupyter lab

# Online jupyter version

[Online Notebook](http://ls.xihajun.cn/Project.html) shows our results and don't need to run it for years.
