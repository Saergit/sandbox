# Petteri Heinonen 2019
# How to test the program

Make sure you have Python 3.7 installed.

Once installed, open up your terminal or cmd to install flask.
> pip install Flask
// or
> py -m pip install Flask

Once flask is installed, navigate to the sandbox/ folder, set needed environment variables and run flask.
> set FLASK_ENV=development
> set FLASK_APP=app.py
> flask run

Now go to the internet browser and start using the API by localhost.
E.g. 
http://127.0.0.1:5000/median_pickup_time/?location_id=12&start_time=2019-01-09T11:00:00&end_time=2019-01-14T12:00:00
