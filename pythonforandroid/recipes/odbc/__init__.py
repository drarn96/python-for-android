from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class OdbcRecipe(CompiledComponentsPythonRecipe):
    
    pre_build_ext = False
    
    version = '2.3.7'
    url = 'https://github.com/lurcher/unixODBC/archive/{version}.tar.gz'
    site_packages_name = 'odbc'
    depends = ['setuptools']
    
    call_hostpython_via_targetpython = True
    install_in_hostpython = False
    install_in_targetpython = False

recipe = OdbcRecipe()
