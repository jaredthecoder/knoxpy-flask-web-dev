# -*- coding: utf-8 -*-


"""Public section, including homepage and signup."""


from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from redzone.extensions import login_manager
from redzone.public.forms import LoginForm
from redzone.user.forms import RegisterForm
from redzone.user.models import User
from redzone.utils import flash_errors


blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""

    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET'])
def home():
    """Home page."""

    return render_template('public/home.html')


@blueprint.route('/user/login', methods=['GET', 'POST'])
def login():
    """Login the user."""

    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)

    return render_template('public/login.html', form=form)


@blueprint.route('/user/logout')
@login_required
def logout():
    """Logout the user."""

    logout_user()
    flash('You are logged out.', 'info')

    return redirect(url_for('public.home'))


@blueprint.route('/user/register', methods=['GET', 'POST'])
def register():
    """Register new user."""

    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        User.create(username=form.username.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)

    return render_template('public/register.html', form=form)


@blueprint.route('/about')
def about():
    """About page."""

    return render_template('public/about.html')
