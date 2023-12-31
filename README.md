<!-- [![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) -->

<img src="./demo/screenshot01.PNG" width=900>
<img src="./demo/screenshot02.PNG" width=900>
<img src="./demo/screenshot03.PNG" width=900>

## About Lorrie Park

A web platform for modern and used car listings.
Users can :

- Create an account
- Login , Once Authenticated .
- Create and Modify your Profile
- Post your own car listing
- Find, Like and Save Other people's post you find interesting
- Get reviews on posts in real time via Email
- User posts can get liked by other users on the platform

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html
