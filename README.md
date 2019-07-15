# PyPosSQLCollector
Web based app that sends your weight and weight average from a database of other users to your email address

The app uses python to trigger the script and heroku to deploy the web in the server. Frontend has been done using html and css files. Backend is based on the python script as well as the database created using postgreSQL thanks to SQLAlchemy.

The repository includes: templates folder (html files), static folder (css file), python script as well as send_email function, heroku necessary files such as requirements.txt, Procfile, runtime.txt. It is also included .gitignore file to avoid unnecesary data in the heroku server.

I have added some notes to deploy the app on a heroku server (through the CLI), although you can still use the app in the local host if you prefer it.

Note 1: you will need to create an app and db using your CLI and typing heroku commands:
C:\...> heroku create nameoftheapp
C:\...> heroku addon:create heroku_postgresql: hobby-dev --app nameoftheapp

Note 2: you will need to find the URI of your database:
C:\...>heroku config --app nameoftheapp

Note 3: follow the set up commands:
C:\...>git init
C:\...>git add.
C:\...>git commit -m "first commit"
C:\...>heroku git:remote --app nameoftheapp
C:\...>git push heroku master
C:\...>heroku open

Note 4: Set up the db on heroku:
C:\...>heroku run python
C:\...>from script import db
C:\...>db.create_all()
