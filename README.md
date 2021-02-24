```sh
python3 -m venv venv
source venv/bin/activate

pip install flask
pip install gunicorn
pip freeze > requirements.txt

chmod +x boot.sh
```

```sh
export FLASK_CONFIG=development
export FLASK_APP=main.py
export FLASK_DEBUG=1
export SPECIALMESSAGE="This is a special message from the ship"

flask run
```

```sh
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 874957933250.dkr.ecr.ap-southeast-1.amazonaws.com

docker build -t flask-helloworld .

docker tag flask-helloworld:latest 874957933250.dkr.ecr.ap-southeast-1.amazonaws.com/flask-helloworld:v0.0.2

docker push 874957933250.dkr.ecr.ap-southeast-1.amazonaws.com/flask-helloworld:v0.0.2
```

# Paths

- `GET /` - homepage
- `POST /loyalty_card` - create a loyalty card