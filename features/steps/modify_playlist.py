from behave import *

use_step_matcher("re")


@step('Exists restaurant registered by "user1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Exists restaurant registered by "user1"'
                              u'| name |'
                              u'| Gaby\'s playlist|')


@when('I view the details for name "Javi\'s playlist"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I view the details for name "Javi\'s playlist"')


@step("I edit the current playlist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I edit the current playlist'
                              u'| name |'
                              u'| Javi\'s playlist|')


@then('I\'m viewing the details page for dish at restaurant "The Tavern" by "user2"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for dish at restaurant "The Tavern" by "user2"'
                              u'| name |'
                              u'| Javi\'s playlist |')


@step("There are 1 playlist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And There are 1 playlist')