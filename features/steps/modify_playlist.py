from behave import *
from apps.spotify.models import Song, Playlist

use_step_matcher("re")


@step('Exists playlist registered by "user1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    import time
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)
    time.sleep(5)
    context.browser.visit(context.get_url('/accounts/login/?next=/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('user1', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
    time.sleep(5)
    context.browser.visit(context.get_url('/playlist/create/?next=/'))
    context.browser.fill('Gaby playlist', name)
    form.find_by_value('Submit').first.click()
    time.sleep(10)


@when('I view the details for name "Gabys playlist"')
def step_impl(context):
    import time
    context.browser.visit(context.get_url('playlist/?next=/'))
    time.sleep(5)


@step("I edit the current playlist")
def step_impl(context):
    import time
    context.browser.visit(context.get_url('playlist/?next=/'))
    context.browser.find_by_id('--update--').first.click()
    context.browser.fill('Javi playlist',name)
    context.browser.fin_by_value('Submit').first.click()
    time.sleep(5)

@then('Im viewing the details from playlist that changes the name')
def step_impl(context):
    import time

    ()



@step("There are 1 playlist")
def step_impl(context):
    import time
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And There are 1 playlist')
