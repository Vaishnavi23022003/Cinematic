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
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
