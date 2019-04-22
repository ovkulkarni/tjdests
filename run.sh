#!/bin/sh
export PRODUCTION=TRUE
cd /web/projects/tjhsst2019/tjdests/
/web/projects/tjhsst2019/tjdests/env/bin/gunicorn tjdests.wsgi -b 127.0.0.1:$PORT -w=7
