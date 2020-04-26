from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class PyodbcRecipe(CompiledComponentsPythonRecipe):
    version = '4.0.30'
    url = 'https://github.com/mkleehammer/pyodbc/archive/{version}.tar.gz'
    site_packages_name = 'pyodbc'
    depends = ['python3']
    conflicts = []


recipe = PyodbcRecipe()

