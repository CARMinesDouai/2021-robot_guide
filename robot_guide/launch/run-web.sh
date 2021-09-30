#!/bin/sh
# launch web servers
cd `dirname $0`/../web-admin && node app.js&
cd `dirname $0`/../web-user && node app.js&
