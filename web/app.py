import os
import sys

import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.models import User, Movie, Channel
from web.provider import UsernameAndPasswordProvider

import config

middleware = [
    Middleware(SessionMiddleware, secret_key=config.conf.web.SECRET_KEY)
]

app = Starlette(middleware=middleware)

logo_url = 'https://cdn2.iconfinder.com/data/icons/business-1334/53/145-512.png'
admin = Admin(
    engine=config.conf.db.db_url,
    title="Aiogram Web Admin",
    base_url='/',
    logo_url=logo_url,
    auth_provider=UsernameAndPasswordProvider()
)

admin.add_view(ModelView(User))
admin.add_view(ModelView(Movie))
admin.add_view(ModelView(Channel))

# Mount admin to your app
admin.mount_to(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
