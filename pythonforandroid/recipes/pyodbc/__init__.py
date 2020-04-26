from pythonforandroid.recipe import PythonRecipe


class PyodbcRecipe(PythonRecipe):
    version = '4.0.30'
    url = 'https://github.com/mkleehammer/pyodbc/archive/{version}.tar.gz'
    site_packages_name = 'pyodbc'
    depends = ['setuptools', 'https://github.com/lurcher/unixODBC/archive/2.3.7.tar.gz']
    
    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    install_in_targetpython = False

recipe = PyodbcRecipe()



