

from behave import *

use_step_matcher("parse")


@when(u'I add playlist')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('spotify:create_playlist'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for playlist by "{user}"')
def step_impl(context, user):
    """q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from apps.spotify.models import Playlist
    restaurant = Playlist.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(restaurant)"""
    pass
