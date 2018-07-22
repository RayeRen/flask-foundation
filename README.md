# Flask Foundation
Based on https://github.com/JackStouffer/Flask-Foundation. Compatible with Flask 1.0

## Dependencies
- Python 3+
- Flask 1.0+
- mysql
- all `packages` in `requirements.txt`

## Quick Start Development

### Configure the .env file
1. `cp .env.example .env`
2. Modify `.env`

### Mysql Service
1. Install mysql server and client
2. Enable the mysql service

### Install Dependencies
```bash
pip install -U -r requirement.txt
```

### Run Unittests
```bash
py.test tests 
```
You will see the following summary after all tests finished.
```text
==================== 7 passed, 21 warnings in 1.88 seconds ====================
```
### Create Dev Database
```bash
flask db init
```

### Run Dev Server
```bash
flask run
```

### Migrate Database Schema
```bash
flask db migrate
flask db upgrade
```

## Run Prod Server
1. Switch the config to `Prod` mode in `.env`
2. 
```bash
flask db init
flask run
```

## Deploy with Nginx and Uwsgi

### Intall Nginx and Uwsgi
```bash
apt install nginx
conda install -c conda-forge uwsgi libiconv
```

### Increase Max Listening Connections
```bash
echo net.core.somaxconn= 4000 >  /etc/sysctl.conf && sysctl -p
```

### Configure Nginx
```bash
cp nginx/nginx.conf.example nginx/nginx.conf
vi nginx.conf # modify the config file
ln -s $PWD/nginx/nginx.conf.example /etc/nginx/conf.d/MY_APP.conf
```

### Start UWsgi
```bash
uwsgi --ini uwsgi.ini
```
