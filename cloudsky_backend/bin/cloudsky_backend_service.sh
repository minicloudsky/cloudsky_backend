#!/usr/bin/env bash


PROJECT_PATH=$(cd "$(dirname "$0")"; cd ../;pwd)
DESC=service


server_start() {
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_django_uwsgi.sh start
}

server_stop() {
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_django_uwsgi.sh stop
}

server_restart() {
    sh $PROJECT_PATH/cloudsky_backend/cloudsky_backend/bin/cloudsky_backend_django_uwsgi.sh restart
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