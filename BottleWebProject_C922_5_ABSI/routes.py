"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        year=datetime.now().year
    )

@route('/mcm_system_reliability_3_2')
@view('mcm_system_reliability_3_2')
def contact():
    """Renders the contact page."""
    return dict(
        title='System reliability 3 and 2 thread',
        year=datetime.now().year
    )

@route('/mcm_estimating_failure_probilities_4')
@view('mcm_estimating_failure_probilities_4')
def about():
    """Renders the about page."""
    return dict(
        title='Estimating failure probilities 4 tread',
        year=datetime.now().year
    )

@route('/mcm_system_reliability_2_3')
@view('mcm_system_reliability_2_3')
def about():
    """Renders the about page."""
    return dict(
        title='System reliability 2 and 3 thread',
        year=datetime.now().year
    )

@route('/mcm_estimating_failure_probilities_3')
@view('mcm_estimating_failure_probilities_3')
def about():
    """Renders the about page."""
    return dict(
        title='Estimating failure probilities 3 tread',
        year=datetime.now().year
    )

@route('/program_mcm_2_3_K')
@view('program_mcm_2_3_K')
def about():
    """Renders the about page."""
    return dict(
        title='System reliability 2 and 3 thread',
        year=datetime.now().year
    )

@route('/program_mcm_3_2_A')
@view('program_mcm_3_2_A')
def about():
    """Renders the about page."""
    return dict(
        title='System reliability 3 and 2 thread',
        year=datetime.now().year
    )

@route('/program_mcm_3_V')
@view('program_mcm_3_V')
def about():
    """Renders the about page."""
    return dict(
        title='Estimating failure probilities 3 tread',
        year=datetime.now().year
    )

@route('/program_mcm_4_S')
@view('program_mcm_4_S')
def about():
    """Renders the about page."""
    return dict(
        title='Estimating failure probilities 4 tread',
        year=datetime.now().year
    )
@route('/template_sv')
@view('template_sv')
def about():
    """Renders the about page."""
    return dict(
        year=datetime.now().year
    )
@route('/template_ak')
@view('template_ak')
def about():
    """Renders the about page."""
    return dict(
        year=datetime.now().year
    )