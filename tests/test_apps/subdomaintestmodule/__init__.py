from flask import Blueprint

bp = Blueprint("foo", __name__, subdomain="foo")
