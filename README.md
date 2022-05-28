# Cinematic
A movie-recommendation website built using python django framework. [Website Link](https://cinematic2022.herokuapp.com)

### Prerequisites
Git
Python (version 3 or above)

### Setup

```sh
$ git clone https://github.com/Vaishnavi23022003/Cinematic.git
$ cd Cinematic
```

Create a virtual environment to install dependencies in:

```sh
$ python -mvenv env
```
if above command does not work due to difference in python versions try:
```sh
$ pip install virtaulenv
$ virtualenv env
```

Activate the virtual environment
```sh
$ env/scripts/activate
```
if above command does not work due to difference in python versions try:
```sh
$ source env/bin/activate
```
if it still doesn't work then find the activate file in env folder and use it's path


Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
if above command does not work due to difference in python versions try:
use `py -m pip install` in place of  `pip install`

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ pip install django
(env)$ django-admin startproject temp
```

A temp folder will be created -> we only need this for django `SECRET_KEY`.<br />
Go to `temp/temp/settings.py` and copy the value of `SECRET_KEY`.<br />
Now got to `../../Cinematic/settings.py` and replace the value of `SECRET_KEY` with the copied one.<br />
Also change `<db_user_name>` with the name of postgresql database and `<db_password>` with password of postgresql database.

Now:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`

### Screenshots of website

![p](https://i.ibb.co/X5cGRC7/p.png)
![p](https://i.ibb.co/Z8cDP0Z/Cinematic-Firefox-Developer-Edition-28-05-2022-20-30-56.png)
![p](https://i.ibb.co/X4xqwQD/Cinematic-Firefox-Developer-Edition-28-05-2022-20-34-19.png)
![p](https://i.ibb.co/YRPPKr4/Cinematic-Firefox-Developer-Edition-28-05-2022-20-34-27.png)
![p](https://i.ibb.co/yFkbDcS/Cinematic-Firefox-Developer-Edition-28-05-2022-20-35-07.png)
![p](https://i.ibb.co/CBy0WLv/Cinematic-Firefox-Developer-Edition-28-05-2022-20-35-17.png)








