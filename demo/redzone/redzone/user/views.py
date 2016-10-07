# -*- coding: utf-8 -*-


"""User views."""


from flask import Blueprint, render_template, request, redirect
from flask import url_for, flash, current_app
from flask_login import login_required, current_user

from redzone.user.forms import AddMessageForm
from redzone.user.models import User, Message
from redzone.utils import flash_errors


blueprint = Blueprint('user', __name__, static_folder='../static')


@blueprint.route('/users')
@login_required
def members():
    """List members."""

    return render_template('users/members.html')


@blueprint.route('/message/add', methods=['GET', 'POST'])
@login_required
def add_message():
    """Add message."""

    user = User.query.filter_by(
        username=current_user.username).first()
    form = AddMessageForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        Message.create(title=form.title.data,
                       message=form.message.data)
        flash('Your message was added!', 'success')
        return redirect(url_for('user.add_message'))
    else:
        flash_errors(form)
    return render_template('users/addMessage.html', form=form)


@blueprint.route('/message/list')
@login_required
def list_messages():
    """List messages."""

    user = User.query.filter_by(
        username=current_user.username).first()
    messages = Message.query.all()
    return render_template('users/listMessages.html', messages=messages)
