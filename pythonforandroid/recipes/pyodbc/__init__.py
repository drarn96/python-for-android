from pythonforandroid.recipe import PythonRecipe


class PyodbcRecipe(PythonRecipe):
    version = '4.0.30'
    url = 'https://github.com/mkleehammer/pyodbc/archive/{version}.tar.gz'
    site_packages_name = 'pyodbc'
    depends = ['setuptools']
    
    call_hostpython_via_targetpython = True
    install_in_hostpython = True
    install_in_targetpython = True
        
    def build_arch(self, arch):
        super().build_arch(arch)
        self.install_python_package(arch)
        self.install_python_package('https://github.com/lurcher/unixODBC/archive/2.3.7.tar.gz')


recipe = PyodbcRecipe()



