# An example app to send SMS via webapp 


## Python/Twilio setup

Make sure the following environment variables are set in `.env` file.

```
TWILIO_AUTH_TOKEN="xxx"
TWILIO_ACCOUNT_SID="xxx"
FROM_PHONE_NUMBER="+10001112222"
TO_PHONE_NUMBER="+10001113333"
```

Ensure that `PYTHON_BIN` variable in `run_script.sh` is set to the correct python binary.
In this case, we set it to `$HOME/opt/miniconda3/envs/py3-env/bin/python` corresponding to
a conda environment we created which has `twilio` python library installed.

Run the script as follows: `./run_script.sh`. This should send SMS to the number specified above.


## Python API server for sending SMS

The code for api server is in `api/backend.py`. It also has a `requirements.txt` file which has
all python dependencies needed by the server. Further all env variables are taken 
from the local`.env` file automatically when we run `vercel dev` locally. 

For preview and production deployments, these environment variables must be set on vercel.com.

