# Website

[![CI](https://github.com/tjh90/website/actions/workflows/ci.yml/badge.svg)](https://github.com/tjh90/website/actions/workflows/ci.yml)

Simple website

## Extracting the SSL certificates

To extract the SSL certificate and key, use the following commands:

```
openssl pkcs12 -in ./certs/index.p12 -nokeys -out ./certs/index.crt
openssl pkcs12 -in ./certs/index.p12 -nocerts -out ./certs/index.key
```

You will be prompted for the store password.

## Running a development instance

Once checked out, development should be done in a python virtual environment. To set up the virtual environment and start a development instance, run:

```
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
python ./wsgi.py
```

in the `index` directory.

# Running a production instance

To build the docker images, run:

```
docker-compose build
```

To deploy, run:

```
docker-compose up -d
```
