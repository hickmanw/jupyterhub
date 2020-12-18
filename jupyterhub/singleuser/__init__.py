"""JupyterHub single-user server entrypoints

Contains default notebook-app subclass and mixins
"""
from .app import main
from .app import SingleUserApp
from .mixins import HubAuthenticatedHandler
from .mixins import make_singleuser_app

# backward-compatibility
JupyterHubLoginHandler = SingleUserApp.login_handler_class
JupyterHubLogoutHandler = SingleUserApp.logout_handler_class
OAuthCallbackHandler = SingleUserApp.oauth_callback_handler_class
