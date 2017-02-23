import os
from fabric.api import local, task, sudo, run, env, cd
BASE_DIR = os.path.sep.join((os.path.dirname(__file__),''))
VENV_DIR = os.path.join(BASE_DIR,'venmhistory/bin/activate')
env.project_name = 'MedicalHistory'
env.hosts = ['localhost']
env.user = 'vagrant'
env.shell = "/bin/bash"
VENV_COMMAND = 'source '+ VENV_DIR


@task
def start():
    """
         1.Activate virtual env
         2.Run server
         3.Collecstatic
         4. createdb sqlLite
    """
    print("Start Application: ")
    with cd(BASE_DIR):
        local('sudo pip install virtualenv', shell=env.shell)
        local('virtualenv --no-site-packages venmhistory --always-copy', shell=env.shell)
        local(VENV_COMMAND, shell=env.shell)
        local('sudo pip install django', shell=env.shell)
        local('sudo pip install djangorestframework', shell=env.shell)
        local('sudo pip install markdown', shell=env.shell)
        local('sudo pip install django-filter', shell=env.shell)
        local('sudo pip install behave', shell=env.shell)
        local('sudo pip install django-behave', shell=env.shell)
        local('sudo pip install unittest-xml-reporting', shell=env.shell)
        local('sudo pip install requests', shell=env.shell)
        local('python ' + BASE_DIR + 'manage.py collectstatic --noinput', shell=env.shell)
        local('python ' +  BASE_DIR + 'manage.py migrate', shell=env.shell)

@task
def cleanAll():
    """Cleans Python bytecode"""
    local('find . -name \'*.pyc\' -exec rm -rf {} \;', shell=env.shell)
    local('rm -rf ' + BASE_DIR + 'venmhistory' , shell=env.shell)
    local('rm ' + BASE_DIR + 'db.sqlite3' , shell=env.shell)
    local('rm ' + BASE_DIR + '*.html' , shell=env.shell)


@task
def cleanReports():
    local('rm ' + BASE_DIR + '*.html' , shell=env.shell)


@task
def runDjangoServer():
    local(VENV_COMMAND, shell=env.shell)
    local('python '+ BASE_DIR + 'manage.py runserver', shell=env.shell)

@task
def runUnitTest():
    local(VENV_COMMAND, shell=env.shell)
    local('python ' + BASE_DIR + 'manage.py test appmhistory/tests',shell=env.shell)

@task
def runServer():
    local(VENV_COMMAND, shell=env.shell)
    local('nohup python ' + BASE_DIR + 'manage.py runserver &', shell=env.shell)

@task
def runAcceptanceTest(var_deploy_folder):
    var_deploy_folder = os.path.sep.join((os.path.dirname(__file__),var_deploy_folder))
    local('source ' +var_deploy_folder + '/venmhistory/bin/activate', shell=env.shell)
    local('nohup python '+var_deploy_folder+'/manage.py runserver & behave features/register.feature', shell=env.shell)

@task
def packageApplication():
    local('sudo python setup.py sdist')