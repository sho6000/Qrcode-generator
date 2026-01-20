### TASK assigned

Containerize a simple app (Node.js/Python/Java) that connects to a database (MySQL/PostgreSQL/MongoDB).

Run both app and DB in separate containers, using environment variables for configuration.

Use volumes to persist database data.

Ensure the app can read/write to the database locally.

Push the app image to Docker Hub.

Use docker-compose to run both containers together.

### Setup

Created secrets file `user.txt` and `pass.txt` to store credentials

ensure the docker-composee.yml includes the secrets file under secrets

stored the secrets in **.evn** and added to .gitignore

app.py generates qr code based on the link given and stored in mongodb

the data is written and fetch hence showing top 5 entries

setup username and password before running

### Run

```powershell
docker-compose -f qr-compose.yaml up --build -d
```

### App image

app image can be found [here](https://hub.docker.com/r/shoun6000/qr-generator)

