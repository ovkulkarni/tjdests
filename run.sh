#!/bin/sh
cd /web/activities/tjdests2018/tjdests/
/web/activities/tjdests2018/tjdests/env/bin/gunicorn tjdests.wsgi -b 127.0.0.1:$PORT -w=15

