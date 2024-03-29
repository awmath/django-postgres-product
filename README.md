[![GitHub version](https://badge.fury.io/gh/awmath%2Fdjango-postgres-product.svg)](https://badge.fury.io/gh/awmath%2Fdjango-postgres-product)
[![PyPI version](https://badge.fury.io/py/django-postgres-product.svg)](https://badge.fury.io/py/django-postgres-product)

![CI/CD Workflow](https://github.com/awmath/django-postgres-product/workflows/test%20and%20packaging/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/awmath/django-postgres-product/badge)](https://www.codefactor.io/repository/github/awmath/django-postgres-product)
[![codecov](https://codecov.io/gh/awmath/django-postgres-product/branch/master/graph/badge.svg)](https://codecov.io/gh/awmath/django-postgres-product)

# django-postgres-product

Adds a product aggregation function to a postgres database and makes it available with django

## Usage

Add the app to your list of installed apps

```
INSTALLED_APPS = [
    ...,
    'postgres_product',
    ...
]
```

Import the product aggregation function

```
from postgres_product import Product
```

Use the aggregation as described in the [Django Documentation](https://github.com/awmath/django-postgres-product/workflows/Python%20package/badge.svg)

## Roadmap

- create python packaging
