from flask import Blueprint, render_template

error = Blueprint('error', __name__)

@error.app_errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404

@error.app_errorhandler(403)
def access_forbidden(error):
    return render_template('error/403.html'), 403

@error.app_errorhandler(500)
def error_500(error):
    return render_template('error/500.html'), 500