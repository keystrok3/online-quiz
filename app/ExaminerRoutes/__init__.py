from flask import Blueprint

examiners = Blueprint('examiners', __name__)

from . import views