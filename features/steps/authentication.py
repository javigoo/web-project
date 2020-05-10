from behave import *

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    pass
    #from django.contrib.auth.models import User
    #User.objects.create_user(username=username, email='user@example.com', password=password)

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    import time     # Just for debug
    context.browser.visit(context.get_url('/social/login/spotify/'))
    context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    time.sleep(1)
    context.browser.find_by_id('login-button').first.click()
    time.sleep(5)
