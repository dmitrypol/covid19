# using Redis with Python to analyze COVID19 data

* Redlock for distributed lock management
* Redis as a job queue to scale data processing
* Redis with Python Pandas for Data Science.  Data is stored in Redis Hashes which translate into Panda DataFrames

## Setup dev environment

* Install Docker and Docker Compose https://docs.docker.com/compose/install/
* Clone this repo
* `cp devops/secrets.env.sample devops/secrets.env` and specify values in it
* docker-compose up --build -d
* Run `devops/reimport_data.sh` to import data for all dates
* Run `devops/test.sh` to run all unit tests
* Browse to http://localhost:5000/ to view dashboard
* Browse to http://localhost:5000/rq/ to view jobs running
* Data is sourced from https://github.com/CSSEGISandData/COVID-19, by Johns Hopkins CSSE
