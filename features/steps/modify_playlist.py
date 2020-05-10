from behave import *

use_step_matcher("re")


@given('Exists a user "user1" with password "password"')
def step_impl(context,username,password):
    """
    :type context: behave.runner.Context
    """
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)
    context.browser.visit(context.get_url('/accounts/login/?next=/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
    context.browser.visit(context.get_url('/playlist/create/?next=/'))
    context.browser.fill('name', "Gaby playlist")
    form.find_by_value('Submit').first.click()


@step('Exists playlist registered by "user1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('playlist/?next=/'))

@when('I view the details for name "Javi\'s playlist"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('playlist/?next=/'))
    context.browser.find_by_id('--update--').first.click()
    context.browser.fill('name', "Javi playlist")
    context.browser.fin_by_value('Submit').first.click()


@then("I'm viewing the details from playlist that changes the name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_name("Javi playlist").first.click()


