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
    print("base dir: "+BASE_DIR)
    venv_command = 'source '+ VENV_DIR
    with cd(BASE_DIR):
        run('virtualenv --no-site-packages venmhistory --always-copy')
        run (venv_command)
        run('pip install django whitenoise')
        run('python manage.py migrate')
        run('python manage.py collectstatic --noinput ')
        run('python manage.py runserver')
 
