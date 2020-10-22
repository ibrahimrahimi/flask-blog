# flask-blog

Flask Blog is a simple web application build upon flask framework. You can use it to post your blogs easily with creating 
accounts in this website.

## Installation

In order to install this application after you cloned the source code from GitHub you need to install the requirements of 
the project provided in ```requirements.txt``` file by using following command.

```bash
pip3 install -r requirements.txt
```

## Usage 'Linux'

In this application we directly used some of the configuration from **OS** environment in config file. So you need to provide 
some values in ```.bashrc``` file of your **Ubuntu** to make them available for config.py file of the project. You need to add 
bellow keys and related values in ```.bashrc``` file:

```
SQLALCHEMY_DATABASE_URI=your database URLI
SECRET_KEY=your secret key
EMAIL_USER=your email to be used as the sender email
EMAIL_PASSWORD=password of the email
```
After installing the requirements you should navigate to the project dirctory using terminal and then run following commands to 
run the application:

```python
export FLASK_APP=run.py

flask run
```
## Usage 'Windows'

In this application we directly used some of the configuration from **OS** environment in ```config.py``` file of the project. 
So you need to provide those values in **environment variables** section of your **Windows** to make them available for config.py 
file of the project. You need to add bellow keys and related values in **environment variables** section:

```
SQLALCHEMY_DATABASE_URI=your database URLI
SECRET_KEY=your secret key
EMAIL_USER=your email to be used as the sender email
EMAIL_PASSWORD=password of the email
```

After installing the requirements you should navigate to the project dirctory in a terminal and then run following commands to 
run the application:

```python
export FLASK_APP=run.py

flask run
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.Please make 
sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
