from flask import Blueprint, render_template

site = Blueprint('site',__name__,template_folder='site_templates')

"""
Note that in the below code,
some arguments are specified when creating Blueprint objects.
The first argument, 'site' is the Blueprint's name,
which flask uses for routing.
The second argument, __name__, is the Blueprint's import name, 
which flask uses to locate the Blueprint's resources
""" 
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/search')
def search():
    return render_template('search.html')
