# Flask Foundation

## Dependencies
- Python 3+
- Flask 1.0+
- all `packages` in `requirements.txt`

## Quick Start

### 复制并修改配置文件
1. `cp .env.example .env`
2. 修改config.py中的数据库账号密码

### Mysql
1. 安装mysql服务端和客户端
2. 打开mysql服务

### 安装依赖
```bash
pip install -U -r requirement.txt
```

### 运行单元测试
```bash
py.test tests 
```
出现如下字样，表明测试通过
```text
==================== 7 passed, 21 warnings in 1.88 seconds ====================
```
### 运行Server
```bash
flask run
```