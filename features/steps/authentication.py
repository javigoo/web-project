from behave import *

use_step_matcher("parse")


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/social/login/spotify/'))
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    context.browser.find_by_id('login-button').first.click()
