#!/bin/bash 
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECTDIR=$(dirname $DIR)
LOGFILE="${PROJECTDIR}/output.log"
FILENAME=$(basename ${1})
echo "Running script $0 with arguments ${@}" # >> "${LOGFILE}"  2>&1
source $PROJECTDIR/venv/bin/activate
python $PROJECTDIR/photos_utils/image_exists.py --image_name ${FILENAME} # >> "${LOGFILE}"  2>&1
RC=$?
echo "Return code is ${RC}" # >> "${LOGFILE}"  # 2>&1
echo " " #>> "${LOGFILE}"  2>&1
echo " " #>> "${LOGFILE}"  2>&1
deactivate
exit $RC