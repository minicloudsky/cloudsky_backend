#!/usr/bin/env bash


PROJECT_PATH=$(cd "$(dirname "$0")"; cd ../;pwd)
PYTHON_PATH=python3
DESC=cloudsky_backend_django_server
NAME=cloudsky_backend_django_server
PIDFILE=$PROJECT_PATH/cloudsky_backend/cloudsky_backend/uwsgi/uwsgi.pid
STATUS_FILE=$PROJECT_PATH/cloudsky_backend/cloudsky_backend/uwsgi/uwsgi.status
DAEMONIZE_FILE=$PROJECT_PATH/cloudsky_backend/cloudsky_backend/uwsgi/$NAME.log

server_start() {
     $PYTHON_PATH/uwsgi --ini $PROJECT_PATH/cloudsky_backend/cloudsky_backend/uwsgi/cloudsky_backend_uwsgi.ini --stats=$STATUS_FILE --pidfile=$PIDFILE --daemonize=$DAEMONIZE_FILE
}


server_stop() {
    $PYTHON_PATH/uwsgi --stop $PIDFILE
}

server_status() {
#    start-stop-daemon --status --quiet --pidfile $PIDFILE
    $PYTHON_PATH/uwsgi --connect-and-read $STATUS_FILE
    return $?
#    return $?
}


case "$1" in
        start)
            echo -n "Starting $DESC: "
        if [ -e $PIDFILE ]
        then
           echo "Django Server has been started! Please check it!"
        else
            server_start
            sleep 5
                if [ -e $PIDFILE ]
            then
                        echo "Ok"
            else
            echo "Start Failed"
            fi
        fi
                ;;
        stop)
                echo -n "Stopping $DESC: "
        if [ ! -e $PIDFILE ]
                then
                   echo "The Server doesn't start!"
                else
                    server_stop
            sleep 5
            if [ ! -e $PIDFILE ]
            then
                        echo "ok"
            fi
        fi
                ;;
        restart|force-reload)
                echo -n "Restarting $DESC: "
                server_stop
        sleep 5
        if [ -e $PIDFILE ]
        then
            echo "stop failed!"

        else
            echo "stop ok!"
        fi

                server_start
        sleep 5
        if [ -e $PIDFILE ]
                then
                    echo "start ok!"

                else
                    echo "start Failed!"
                fi
                ;;
        status)
                echo -n "Status of $DESC: "
                server_status && echo "running" || echo "stopped"
                ;;
        *)
                N=/etc/init.d/$NAME
                echo "Usage: $N {start|stop|restart|status}" >&2
                exit 1
                ;;
esac

exit 0
