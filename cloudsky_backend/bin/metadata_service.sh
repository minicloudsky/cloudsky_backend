#!/usr/bin/env bash


PROJECT_PATH=/home/tools/opendata_project/metadata_project
DESC=service


server_start() {
    sh $PROJECT_PATH/back_end/back_end/bin/metadata_django_uwsgi.sh start
#    sh $PROJECT_PATH/back_end/back_end/bin/metadata_celery.sh start
#    sh $PROJECT_PATH/back_end/back_end/bin/metadata_celery_beat.sh start
    sh $PROJECT_PATH/back_end/back_end/bin/metadata_thrift_rpc.sh start
}

server_stop() {
    sh $PROJECT_PATH/back_end/back_end/bin/metadata_django_uwsgi.sh stop
#    sh $PROJECT_PATH/back_end/back_end/bin/metadata_celery.sh stop
#    sh $PROJECT_PATH/back_end/back_end/bin/metadata_celery_beat.sh stop
    sh $PROJECT_PATH/back_end/back_end/bin/metadata_thrift_rpc.sh stop
}

server_restart() {
    sh $PROJECT_PATH/back_end/back_end/bin/metadata_django_uwsgi.sh restart
#    sh $PROJECT_PATH/back_end/back_end/bin/metadata_celery.sh restart
#    sh $PROJECT_PATH/back_end/back_end/bin/metadata_celery_beat.sh restart
    sh $PROJECT_PATH/back_end/back_end/bin/metadata_thrift_rpc.sh restart
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