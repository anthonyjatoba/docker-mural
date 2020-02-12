# docker-mural

## Run locally

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r requirements`

`python banco.py`

`python app.py`

## Run on docker

`docker build -t mural:latest .`

`docker run -p 5000:5000 mural:latest`

Go to: [localhost:5000](localhost:5000)

## Push to heroku

`cd docker-mural`

`heroku container:login`

`heroku create seumural`

`heroku container:push web --app seumural`

`heroku container:release web --app seumural`
