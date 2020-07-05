# Zwerb - Stock Analysis 

Experimentation with python, jupter lab, pandas, numpy, keras, github

## Latest Work Log

* 2020-07-05 Found out my AWS account had running endpoint for the last 67 hours at $0.28/hr

* 2020-07-04 Left off ready to start to scale data and format for input into NN

* 2020-07-04 Left off ready to iterate on processing offline csvs for ML prep

* 2020-07-03 Left off at creating offline CSV-reading functionality


## How to Setup

### get into the main dir 

```
cd ~../stock_analysis
```

### if you're using venv

```
source bin/activate
```

### re-upgrade / install the pip libs

```
./bashsetup.sh
```
### get into the git folder if required

```
cd stock_analysis
```

### start jupyter lab

```
jupyter lab
```

### run the workflow ipynb

## How to setup the environment from scratch

### make the project folder

```
mkdir stock_analysis
```

### get pip (if needed)

```
sudo easy_install pip
sudo pip install --upgrade pip
sudo pip3 install --upgrade pip
```

### get virtualenv (if necessary)

```
pip3 install virtualenv
```

### setup virtualenv (if necessary, in the folder )

```
python3 -m venv /path_to_dir/

cd /path_to_dir/
```

### activate the venv (if you're using virtual environment

```
source bin/activate
```

### install basic support

```
pip install conda

pip install jupyter notebook

pip install jupyterlab
```

### git init

```
git clone https://github.com/zwerb/stock_analysis
```

### get into the git project files

```
cd stock_analysis

mkdir stock_files
mkdir stock_graphs
```

### creating bash file (bashsetup.sh) and chmod 755 bashsetup.sh

```
touch bashsetup.sh
```

## Versioning

We will start using [SemVer](http://semver.org/) for versioning once we break out of 0.0.0.0.0.

## Authors

* **Zwerb** - *Initial work* - [Zwerb](https://www.zwerb.com)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

