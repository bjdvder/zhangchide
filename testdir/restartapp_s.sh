#!/bin/bash

PIDFILE="/var/zhangchide/zc.pid"

if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

exec python ./manage.py runfcgi host=127.0.0.1 port=6000 pidfile=$PIDFILE
