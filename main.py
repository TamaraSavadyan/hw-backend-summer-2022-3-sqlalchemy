import os
# smth random

from app.web.app import setup_app
from aiohttp.web import run_app

if __name__ == "__main__":
    run_app(
        setup_app(
            config_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "config.yml"
            )
        )
    )

# aiohttp==3.8.1
# aiohttp-apispec==2.2.3
# aiohttp-session==2.11.0
# aioresponses==0.7.3
# aiosignal==1.2.0
# alembic==1.8.1
# apispec==3.3.2
# async-timeout==4.0.2
# asyncpg==0.26.0
# attrs==22.1.0
# cffi==1.15.1
# charset-normalizer==2.1.0
# coverage==6.4.4
# cryptography==37.0.4
# freezegun==1.2.2
# frozenlist==1.3.1
# greenlet==1.1.2
# idna==3.3
# iniconfig==1.1.1
# Jinja2==3.1.2
# Mako==1.2.1
# MarkupSafe==2.0.1
# marshmallow==3.17.0
# multidict==6.0.2
# packaging==21.3
# pluggy==1.0.0
# py==1.11.0
# pycparser==2.21
# pyparsing==3.0.9
# pytest==7.1.2
# pytest-aiohttp==1.0.4
# pytest-asyncio==0.19.0
# pytest-cov==3.0.0
# pytest-mock==3.8.2
# python-dateutil==2.8.2
# PyYAML==6.0
# six==1.16.0
# SQLAlchemy==1.4.40
# tomli==2.0.1
# webargs==5.5.3
# yarl==1.8.1
