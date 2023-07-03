## Personal Gift

### Setup
The first thing to do is to clone the repository
#### Download python [click and download](https://www.python.org/)
```sh
git clone https://github.com/KRDevs/personal_gift.git
cd personal_gift
```
Create a virtual environment to install dependencies in and activate it:
```sh
pip install pipenv
pipenv shell
```
Then install the dependencies:
```sh
pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:
```sh
cd project
python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
