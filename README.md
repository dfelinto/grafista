# Grafista - quick charts

Prototype for a charting tool application, using a set of minimal components. 
Grafista may become a [Pillar](https://pillarframework.org) extension 
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
cd grafista
python manage.py db_init  # Initialize database
python manage.py runserver  # Run Grafista
```

## Configuration
In order to get Grafista up and running, create a file called `config_local.py`
and override the desired config values available in `config.py`. In particular,
add some `DATA_SOURCES`.

```
DATA_SOURCES = [
    {'url': 'https://www.example.com/stats.json',
     'series': [
         {'name': 'total_sold',
          'description': 'Subscriptions',
          'sample_unit': 'People'}
     ]},
]

```

## Roadmap
In order to further explore the scope of the application, we want to add a some
functionality to Grafista.

* define and implement *queries*
* support multiple data collection systems (url query, but also functions)


## Known issues
Because the `name` attribute of a Series record has to be unique, we have to be
sure that even in different data sources, records don't have conflicting names.

This could be solved by introducing a `source` attribute in the Series model,
and then enforcing name uniqueness for records featuring the same `source`.
