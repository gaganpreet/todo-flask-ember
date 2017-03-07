## Todo

A todo app built using Flask and Ember.js

The project is divided in two Flask modules:

* The backend API written in Python using Flask-Restful (/api directory)
* The frontend written in Javascript using Ember.js (/todo directory)

## Setup

Install the dependencices using pip:

    pip install -r requirements.txt

## Run

Run init\_db.py to initialize the database tables. There are two helper scripts run\_{dev,prod}.py to start the server.

## Known bugs

* Toggling a todo twice quickly causes the event to trigger and toggle itself infinitely.
