from behave import *

use_step_matcher("re")


@when("I add playlist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I add playlist '
                              u'| name    | '
                              u'| Temazos | ')


@then('I\'m viewing the details page for playlist by "user"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for playlist by "user"'
                              u'| name |'
                              u'| Temazos | ')


@step("There are 1 playlist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And There are 1 playlist')
