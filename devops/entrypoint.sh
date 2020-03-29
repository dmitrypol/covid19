#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

flask run -h 0.0.0.0 -p 5000 --reload &
flask sched-start &
rq worker -c rq_config &

# https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php
# if [ $CONTAINER_TYPE = 'web' ]
# then
# elif [ $CONTAINER_TYPE = 'worker' ]
# then
# fi

fg %1