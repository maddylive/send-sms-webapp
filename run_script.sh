PYTHON_BIN=$HOME/opt/miniconda3/envs/py3-env/bin/python

set -a
source .env
set +a

$PYTHON_BIN scripts/send_sms.py
