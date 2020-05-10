from behave import *

use_step_matcher("parse")


@when(u'I add playlist')
def step_impl(context):
    """for row in context.table:
        context.browser.visit(context.get_url('spotify:create_playlist'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()"""
    pass


@then('I\'m viewing the details page for playlist by "user"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("There are 1 playlist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

