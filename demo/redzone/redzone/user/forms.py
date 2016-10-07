# -*- coding: utf-8 -*-


"""User forms."""


from flask_wtf import Form
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

from redzone.user.models import User


class RegisterForm(Form):
    """Register form."""

    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=3, max=25)],
                           _name='username')
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, max=40)],
                              _name='password')
    password_confirm = PasswordField('Verify password',
                            [DataRequired(),
                             EqualTo('password',
                                     message='Passwords must match')],
                            _name='password_confirm')

    def __init__(self, *args, **kwargs):
        """Create instance."""

        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""

        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('Username already registered')
            return False

        return True


class AddMessageForm(Form):
    """Add Message form."""

    title = StringField('Title',
                        validators=[DataRequired(),
                                    Length(min=1)],
                         _name='title')
    message = TextAreaField('Message', _name='message')

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(AddMessageForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(AddMessageForm, self).validate()
        if not initial_validation:
            return False
        return True
