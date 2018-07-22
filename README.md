# Flask Foundation
Based on https://github.com/JackStouffer/Flask-Foundation. Compatible with Flask 1.0

## Dependencies
- Python 3+
- Flask 1.0+
- mysql
- all `packages` in `requirements.txt`

## Quick Start

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
1. Run `flask db migrate`
2. Run `flask db upgrade`

### Run Prod Server
1. Switch the config to `Prod` mode in `.env`
2. Run `flask db init`
3. Run `flask run`

### Deploy with Nginx and Uwsgi

1. `apt install nginx uwsgi`
2. `echo net.core.somaxconn= 4000 >  /etc/sysctl.conf && sysctl -p`
3. `uwsgi --ini uwsgi.ini`

