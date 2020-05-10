from behave import *

use_step_matcher("re")


@given('Exists a user "user1" with password "password"')
def step_impl(context,username,password):
    """
    :type context: behave.runner.Context
    """
    import time
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)
    time.sleep(5)
    context.browser.visit(context.get_url('/accounts/login/?next=/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
    time.sleep(5)
    context.browser.visit(context.get_url('/playlist/create/?next=/'))
    context.browser.fill('name', "Gaby playlist")
    form.find_by_value('Submit').first.click()
    time.sleep(10)


@step('Exists playlist registered by "user1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    import time
    context.browser.visit(context.get_url('playlist/?next=/'))
    time.sleep(5)


@when('I view the details for name "Javi\'s playlist"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    import time
    context.browser.visit(context.get_url('playlist/?next=/'))
    context.browser.find_by_id('--update--').first.click()
    context.browser.fill('Javi playlist', name)
    context.browser.fin_by_value('Submit').first.click()
    time.sleep(5)


@then("I'm viewing the details from playlist that changes the name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    import time
    context.browser.find_by_name("Javi playlist").first.click()
    time.sleep(10)


