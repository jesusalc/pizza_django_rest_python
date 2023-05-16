"""
This module contains setup and teardown methods for the behave environment.
"""

import os
import django
from behave import use_fixture
from django.test.runner import DiscoverRunner

# Behave doesn't automatically integrate with Django's environment 
# like Django's built-in testing tools do
# This should set up Django's environment correctly before your tests run, 
# preventing the AppRegistryNotReady error.
os.environ["DJANGO_SETTINGS_MODULE"] = "pizza_django.settings"  
django.setup()

# This is a fixture to ensure Django is set up for the tests
def django_test_runner(context):
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()

def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()

def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()
