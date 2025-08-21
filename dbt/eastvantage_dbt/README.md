# create a python virtual environment
python3 -m venv dbt-env 

# activate python virtual environment (linux/MacOS)
source dbt-env/bin/activate 

# installing required packages
pip install -r requirements.txt


### Generate Docs
```
dbt docs generate
dbt docs serve
```
then access http://localhost:8080 on web browser.