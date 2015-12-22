#!/bin/sh

##                                                                           ##
## IT IS A CONFIGURATION FILE FOR THE RAPID DEPLOYMENT OF THE PROJECT IN     ##
## COMBAT CONDITIONS ON THE PRODUCTION SERVER.                               ##
##                                                                           ##

# ** The variables that have the `LOCAL_` prefixed - describe the settings for
#    the computer on which the project will be tested, and variables that have
#    the `SERVER_` prefixed - data for the combat server.

# CONFIGURATIONS
# Determine the root directory of the project.
# *** Root directory - the directory that contains: `src`, `venv`, `world` etc,
#     a 100% `src/manage.py` file exists.
BASE_DIR_FILE_MARKER="src/manage.py"
ABSOLUTE_FILENAME=`readlink -e "$0"`
BASE_DIR=`dirname "$ABSOLUTE_FILENAME"`
while [ true ]
do
    if [ -e $BASE_DIR/$BASE_DIR_FILE_MARKER ]; then
        # Directory exist.
        break
    fi # ...

    BASE_DIR=`dirname "$BASE_DIR"`
    if [ $BASE_DIR = "/" ]; then
        # The directory was not found - use the current directory.
        BASE_DIR=`dirname "$ABSOLUTE_FILENAME"`
    fi # ...
done # end while ().

# Project name.
PROJECT_NAME="dlvpef"

# The path of the project socket.
LOCAL_SOCKET="$BASE_DIR/world/run/$PROJECT_NAME.sock"
SERVER_SOCKET="$BASE_DIR/world/run/$PROJECT_NAME.sock"

# The port on which the project will work.
# *** The port can not be specified as `0000` - to change this value.
LOCAL_PORT="3237"
SERVER_PORT="3237"

# The user under which the project will be launched.
LOCAL_USER="valsorym"
SERVER_USER="valsorym"

# Address where the project will be launched.
LOCAL_HOST="$PROJECT_NAME.local"
SERVER_HOST="dlvpef.org"

# Nginx upstream block name.
# http://nginx.org/ru/docs/http/ngx_http_upstream_module.html#upstream
LOCAL_NGINX_UPSTREAM_NAME="${PROJECT_NAME}_django_project"
SERVER_NGINX_UPSTREAM_NAME="${PROJECT_NAME}_django_project"

# Don't use `exit` command - this file is imported into execution script.

