#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

# https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php
if [ $CONTAINER_TYPE = 'web' ]
then
    if [ $APP_ENV = 'dev' ]
    then
        #   https://stackoverflow.com/questions/28585033/why-does-a-flask-app-create-two-process
        exec flask run -h 0.0.0.0 -p 5000 --reload
    else
        exec gunicorn app:APP -w 1 -t 5 --bind 0.0.0.0:5000 --timeout 300;
    fi
elif [ $CONTAINER_TYPE = 'worker' ]
then
    exec rq worker -c rq_config &
elif [ $CONTAINER_TYPE = 'scheduler' ]
then
    exec flask sched-start &
else
    echo unknow $CONTAINER_TYPE 
fi

fg %1