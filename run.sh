#!/bin/sh
export DEBUG="TRUE"
cd /web/projects/tjdests2018/tjdests/
/web/projects/tjdests2018/tjdests/env/bin/gunicorn tjdests.wsgi -b 127.0.0.1:$PORT -w=15

