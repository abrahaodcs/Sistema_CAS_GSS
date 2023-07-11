from flask import Blueprint, render_template, redirect, url_for, request, session

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    session.pop('cpf', None)
    session.pop('nivel_acesso', None)
    session.pop('nivel_organizacional', None)
    return redirect(url_for('index.index'))
