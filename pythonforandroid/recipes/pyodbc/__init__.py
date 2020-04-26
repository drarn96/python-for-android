from pythonforandroid.recipe import Recipe


class PyodbcRecipe(Recipe):
    version = '4.0.30'
    url = 'https://github.com/mkleehammer/pyodbc/archive/{version}.tar.gz'
    site_packages_name = 'pyodbc'


recipe = PyodbcRecipe()

