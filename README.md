# Masonite Dashboard
A Django-like Dashboard For Masonite
## Introduction

Masonite Dashboard is a barebones dashboard designed for third party packages to add links and views to your dashboard. 

These links and views could be: 

* A payment package adding a setup page to ease in the packages configuration 
* A CMS to manage your site's content
* An API dashboard to monitor API requests

This package does not supply these features but it is up to the community to use this package in order to  simply build out functionality on existing dashboards.

## Requirements:

* Masonite 2.0.8+

## Getting Started

### Installation

First you just need to install the package using PIP:

```text
$ pip install masonite-dashboard
```

### Configuration

Just add the provider to the providers list in `config/providers.py`:

```python
from dashboard.providers import DashboardProvider

PROVIDERS = [
    ...
    DashboardProvider,
]
```

Next we will just add the routes to our routes list:

```python
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    ...
    DashboardRoutes(),
    ...
]
```

### Development Only \(optional\)

A likely use case for this dashboard package is that is should only be used by your team in local development environments. In that case you could set a flag in the `routes/web.py` file to only add the routes when `APP_DEBUG` is True:

```python
...
import os
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    ...
]

if os.getenv('APP_DEBUG') == True:
    ROUTES += DashboardRoutes()
```


### Migrations

It is wise to check if the user signing into the dashboard is an admin only. We will set an `is_admin` flag on our users table by creating a new migration:

```text
$ craft migration add_is_admin_to_users --table users
```

And just quickly add a new column:

```python
with self.schema.table('users') as table:
    table.integer('is_admin').nullable()
```

Great! We are all setup, please check the docs for how to [use the dashboard](https://docs.masoniteproject.com/official-packages/masonite-dashboard#using-the-dashboard).
