# instgram clawler

```sh
$ cat /etc/system-release
Amazon Linux release 2 (Karoo)

$ uname -r
4.14.77-81.59.amzn2.x86_64

$ sudo yum install git gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel -y
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ source ~/.bash_profile

$ pyenv -v
pyenv 1.2.8-5-gec9fb549

$ pyenv install 3.6.2
Downloading Python-3.6.2.tar.xz...
-> https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
Installing Python-3.6.2...
Installed Python-3.6.2 to /home/ec2-user/.pyenv/versions/3.6.2

$ pyenv global 3.6.2
$ pyenv rehash

$ python --version
Python 3.6.2

$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/c2/d7/90f34cb0d83a6c5631cf71dfe64cc1054598c843a92b400e55675cc2ac37/pip-18.1-py2.py3-none-any.whl (1.3MB)
  
$ pip --version
pip 18.1 from /home/ec2-user/.pyenv/versions/3.6.2/lib/python3.6/site-packages/pip (python 3.6) 

$ pip install selenium
Collecting selenium
  Using cached https://files.pythonhosted.org/packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl

$ pip freeze
selenium==3.141.0
urllib3==1.24.1

$ git clone https://github.com/watanabeJunna/crwler.git

$ cd clawler

$ python clawler.py
usage:   python crawler.py [username] [password] [keyword]
example: python crawler.py user c8can1!!0_ python3

```

