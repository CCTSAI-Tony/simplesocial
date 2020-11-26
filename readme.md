<div align="center">
	<img width="900" src="https://github.com/CCTSAI-Tony/simplesocial/blob/master/logo.png" alt="emaily">
	<br>
</div>

This web app let you create your own social group and post your favorite topics to your friends! [LINK](https://mysocial66.herokuapp.com/).

I'm happy to accept more configurability and features. PR welcome! What you see here is just what I needed for my own apps.

## User Interfaces

#### Main site - login

<img src="https://github.com/CCTSAI-Tony/simplesocial/blob/master/login.png" width="532">

#### Create groups

<img src="https://github.com/CCTSAI-Tony/simplesocial/blob/master/main.png" width="532">

#### Publish Post

<img src="https://github.com/CCTSAI-Tony/simplesocial/blob/master/post.png" width="532">

## To run web server locally, run the following commands.

1. Clone this repo
2. source ../django_env/bin/activate
3. python3 manage.py collectstatic
4. python3 manage.py createsuperuser
5. python3 manage.py runserver 8080
