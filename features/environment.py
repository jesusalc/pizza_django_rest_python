"""
This module contains setup and teardown methods for the behave environment.
"""

import os
import django
from behave import use_fixture
from django.test.runner import DiscoverRunner

os.environ["DJANGO_SETTINGS_MODULE"] = "pizza_django.settings"  # replace 'your_project.settings' with your actual settings

def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()

def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()
