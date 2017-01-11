# Grafista - quick charts

Prototype for a charting tool application, using a set of minimal components. 
Grafista will likely become a [Pillar](https://pillarframework.org) extension 
one day.


## Architecture
Grafista collects, stores and displays *time series*. The series definition is
stored in a database table, as well as series values, which we call *samples*.
The samples of a series are summarized and displayed in a dashboard web view, 
and can be further analyzed in dedicated views.


## Stack
Grafista is a simple `Flask` application, storing its data in a `SQLite`
database, and useing the following libraries:

* `peewee`: ORM
* `pypugjs`: support for jade-based views (instead of HTML)
* `nv3d`: a reusable approach to charts, based on the `d3` library


## Installation

```
mkvirtualenv grafista  # Optional, if you use virtualenvwrapper
pip install -r requirements.txt
python manage.py init_db  # Initialize database
python manage.py runserver  # Run Grafista
```

## Roadmap
In order to further explore the scope of the application, we want to add a some
functionality to Grafista.

* import data (for example using CSV files)
* define and implement *dashboards* and *queries*
* support multiple data collection systems (url query, but also functions)
