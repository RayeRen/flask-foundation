from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_caching import Cache
from app.models import User

# Setup flask cache
cache = Cache()

debug_toolbar = DebugToolbarExtension()

login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
