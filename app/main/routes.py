from . import bp
from flask import redirect, request, url_for, flash, current_app, render_template, abort

@bp.get('/home/')
@bp.get('/')
def home(): 

    return render_template("home.html",
                    title="GETLINKED"
    )