# stock_analysis
# the following shows how to set this up on an empty linux / unix system

# get pip

sudo easy_install pip

sudo pip install --upgrade pip

pip install virtualenv

python3 -m venv /path_to_dir/

cd /path_to_dir/

# active the venv

source bin/activate

# install basic support

pip install conda

pip install jupyter notebook

pip install jupyterlab

# git init

git clone https://github.com/zwerb/stock_analysis

# get into the git project files

cd stock_analysis

mkdir stock_files
mkdir stock_graphs

# install the pip libs
# after creating the setup bash and chmod 755 file.sh

./bashsetup.sh

# start jupyter lab

jupyter lab



