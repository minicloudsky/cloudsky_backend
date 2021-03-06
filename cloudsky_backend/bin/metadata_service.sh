#!/usr/bin/env bash


PROJECT_PATH=/home/project/cloudsky_backend_project
DESC=service


server_start() {
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_django_uwsgi.sh start
#    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_celery.sh start
#    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_celery_beat.sh start
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_thrift_rpc.sh start
}

server_stop() {
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_django_uwsgi.sh stop
#    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_celery.sh stop
#    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_celery_beat.sh stop
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_thrift_rpc.sh stop
}

server_restart() {
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_django_uwsgi.sh restart
#    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_celery.sh restart
#    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_celery_beat.sh restart
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_thrift_rpc.sh restart
}


case "$1" in
        start)
            echo -n "Starting $DESC: "
            server_start
                ;;
        stop)
            echo -n "Stopping $DESC: "
            server_stop
                ;;
        restart|force-reload)
            echo -n "Restarting $DESC: "
            server_restart
                ;;

esac

exit 0