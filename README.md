# UCM Course Stats

This is project is for UC Merced's CSE-111 Final Project. Our goal was to create a class 
scheduler that would make it easy for student's to digest all relevant course data and choose
the courses best for them. To do this, we used [Postgres](https://www.postgresql.org/) and [Budibase](https://budibase.com/),
both hosted on Docker.

## Installation

We used this [guide](https://www.dbvis.com/thetable/how-to-set-up-postgres-using-docker/) to set up Postgres in Docker
and this [guide](https://docs.budibase.com/docs/docker-compose) to set up Budibase in Docker. 

### Postgres Installation

First open up a terminal.
Then pull the latest Postgres Docker image from the Docker Hub Repository with the following command
```bash
docker pull postgres
```

Then create a Docker volume with the following. The name `postgres_data` can be changed.
```bash
docker volume create postgres_data
```

Finally, run a Postgres Docker container using the following.
```bash
docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres
```
- `postgres_container` can be changed to another name
- `POSTGRES_PASSWORD` should be set to preferred password
- If the docker volume name has changed, fix the mapping at `postgres_data`
  - The value after `postgres_data` is the container directory, that should not need to be changed

### Budibase Installation

The official Budibase installation guide contains essential files needed to set up the Docker container.
Please follow the steps there: https://docs.budibase.com/docs/docker-compose

### Set Up

Once you have both Postgres and Budibase containers running. Click the following link to open Budibase:
http://localhost:10000/

You will have to create an account and sign in.

Download `Course Scheduler.tar.gz`

Once signed in, click import app.

![](README%20Screenshots/import.png)

From there, use the file `Course Scheduler.tar.gz` to get your own instance of the 
Course Scheduler web app. 

Once created you might need to hook up Postgres with Budibase if it isn't hooked up already.
Click Postgres as the datasource
![](README%20Screenshots/select-postgres.png)

Connect to your Postgres container according to how you set it up when running the Docker container.

![](README%20Screenshots/postgres-setup.png)

Then setup the database relationships. Double sided arrow is many to many and single side arrow is one to many.
In the single sided arrow, many is the side the arrow points to

![](README%20Screenshots/relationships.png)

Click publish in the top right corner and the app should then run!