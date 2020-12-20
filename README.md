```sh
python3 -m venv venv
source venv/bin/activate

pip install flask
pip freeze > requirements.txt
```

```sh
export FLASK_CONFIG=development
export FLASK_APP=main.py
export FLASK_DEBUG=1
export SPECIALMESSAGE="This is a special message from the ship"

flask run
```