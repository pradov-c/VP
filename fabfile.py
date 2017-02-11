import os
from fabric.api import local, task, sudo, run, env, cd
from fabric.decorators import runs_once
BASE_DIR = os.path.sep.join((os.path.dirname(__file__),''))
VENV_DIR = os.path.join(BASE_DIR,'venmhistory/bin/activate')
env.password = 'vagrant'
env.hosts = ['localhost']
env.user = 'vagrant'

@task
def start():
    """
         Start app
         Steps:
         1.Activate virtual env
         2.Run server
    """
    print("Start Application: ")
    venv_command = 'source '+ VENV_DIR
    with cd(BASE_DIR):
        print('run virtualenv venmhistory copu')
        run('sudo virtualenv --no-site-packages venmhistory --always-copy')
        run (venv_command)
        run('sudo pip install requests')
        run('sudo pip install django')
        run('sudo pip install djangorestframework')
        run('sudo pip install markdown')
        run('sudo pip install django-filter')
    run('python ' +  BASE_DIR + 'manage.py collectstatic --noinput')
    run('python ' +  BASE_DIR + 'manage.py migrate')


@task
def clean():
    """Cleans Python bytecode"""
    sudo('find . -name \'*.py?\' -exec rm -rf {} \;')