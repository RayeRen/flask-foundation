# Flask Foundation
Based on https://github.com/JackStouffer/Flask-Foundation. Compatible with Flask 1.0

## Dependencies
- Python 3+
- Flask 1.0+
- mysql
- all `packages` in `requirements.txt`

## Quick Start

### 复制并修改配置文件
1. `cp .env.example .env`
2. Modify `config.py`

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
flask createdb
```

### Run Server
```bash
flask run
```

### Run Prod Server
1. Switch the config to `Prod` mode in `.env`
2. Run `flask run`