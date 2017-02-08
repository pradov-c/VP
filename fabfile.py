import os
from fabric.api import local, task, sudo, run, env, cd
from fabric.decorators import runs_once
BASE_DIR = os.path.sep.join((os.path.dirname(__file__),''))
VENV_DIR = os.path.join(BASE_DIR,'venmhistory/bin/activate')
env.password = 'vagrant'
env.hosts = ['localhost']
env.user = 'vagrant'

@task
def deploy():
 """
 Deploy the app to the remote host.
 Steps:
   1.Change to de app's directory
   2.Activate virtual env
   Run south migration
 """
 print("Begining Deploy: ")
 print("base dir: "+BASE_DIR) 
 venv_command = 'source '+ VENV_DIR
 with cd(BASE_DIR):
  run('virtualenv venmhistory')    
  run (venv_command)
  run('pip install django whitenoise')
  run('python manage.py migrate')
  run('python manage.py collectstatic --noinput ')
  run('python manage.py runserver')
 
