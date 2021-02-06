from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegistrationForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/dashboard')
    return render_template('index.html', title='Sign In', form=form)