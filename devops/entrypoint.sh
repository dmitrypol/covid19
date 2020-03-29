#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

flask sched-start &
rq worker -c rq_config &

# https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php
if [ $APP_ENV = 'dev' ]
then
    #   https://stackoverflow.com/questions/28585033/why-does-a-flask-app-create-two-process
    # exec flask run -h 0.0.0.0 -p 5000 --no-reload
    exec flask run -h 0.0.0.0 -p 5000 --reload
else
    exec gunicorn app:APP -w 1 -t 5 --bind 0.0.0.0:5000 --timeout 300;
fi

fg %1