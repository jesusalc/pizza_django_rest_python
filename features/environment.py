"""
This module contains setup and teardown methods for the behave environment.
"""

import os
from behave import use_fixture
from django.test.runner import DiscoverRunner
from django.conf import settings

# This is a fixture to ensure Django is set up for the tests
def django_test_runner(context):
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()

def before_all(context):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza_django.settings'
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()

def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()