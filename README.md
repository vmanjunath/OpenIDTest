# OpenIDTest
A simple django app where you can log in and log out using openid

Setting up
------------------
1. Clone this repository
2. Create a virtual env (I usually do this outside of the repository folder):
`virtualenv openidenv`
3. Activate the virtual env:
`source openidenv/bin/activate`
4. Install the required modules from requirements.txt:
`pip install requirements.txt`
5. Set up the django database by running:
`python manage.py makemigrations`
and then 
`python manage.py migrate`

6. Run the django server:
`python manage.py runserver`
7. You can kill the server with Ctrl-C.


Now you can point your browser at http://localhost:8000 to see the simple log in and log out functionality that uses openid. 
To test it out, just enter an openid URI. You can go to [Yahoo](http://openid.yahoo.com/) to get one. The one provided by my locally running crowdid server is http://localhost:8095/openidserver/users/vikram while the one from the coop’s dev server would be https://login-dev.psfc.coop/openidserver/users/vikram, however this one doesn’t work.
