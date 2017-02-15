import os
from fabric.api import local, task, sudo, run, env, cd
from fabric.decorators import runs_once
BASE_DIR = os.path.sep.join((os.path.dirname(__file__),''))
VENV_DIR = os.path.join(BASE_DIR,'venmhistory/bin/activate')
env.password = 'vagrant'
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
    venv_command = 'source '+ VENV_DIR
    with cd(BASE_DIR):
        local('virtualenv --no-site-packages venmhistory --always-copy', shell=env.shell)
        local(VENV_COMMAND, shell=env.shell)
    local('python ' + BASE_DIR + 'manage.py collectstatic --noinput', shell=env.shell)
    local('python ' +  BASE_DIR + 'manage.py syncdb --noinput', shell=env.shell)


@task
def clean():
    """Cleans Python bytecode"""
    sudo('find . -name \'*.py?\' -exec rm -rf {} \;')

@task
def runDjangoServer():
    local(VENV_COMMAND, shell=env.shell)
    local('python '+ BASE_DIR + 'manage.py runserver', shell=env.shell)

@task
def runUnitTest():
    local('python ' + BASE_DIR + 'appmhistory/tests/test_unitTest.py',shell=env.shell)

