import os  
from contextlib import contextmanager  
from fabric.api import cd, env, prefix, run, sudo, task
 
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file)))
VENV_DIR = os.path.join(PROJECT_ROOT, 'venmhistory')  

@contextmanager
def source_virtualenv():  
	with prefix('source ' + os.path.join(VENV_DIR, 'bin/activate')):
	yield


@task
def deploy():     
with cd(PROJECT_ROOT):
        run('git pull origin master')
        with source_virtualenv():            
            run('source venmhistory/bin/activate')
            run('./manage.py migrate')
            run('./manage.py collectstatic --noinput')