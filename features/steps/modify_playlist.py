from behave import *

use_step_matcher("re")


@given('Exists a user "user1" with password "password"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Exists a user "user1" with password "password"')


@step('Exists playlist registered by "user1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Exists playlist registered by "user1"'
                              u' | name |'
                              u'| Gaby\'s playlist|')


@when('I view the details for name "Javi\'s playlist"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I view the details for name "Javi\'s playlist"')


@then("I'm viewing the details from playlist that changes the name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I\'m viewing the details from playlist that changes the name'
                              u'| name |'
                              u'| Javi\'s playlist |')


@step("There are 1 playlist named Javi Playlist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And There are 1 playlist named Javi Playlist')