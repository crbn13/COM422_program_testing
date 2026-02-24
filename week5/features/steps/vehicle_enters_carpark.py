from behave import *
from behave.api.pending_step import StepNotImplementedError

@given(u'an empty car park')
def step_impl(context):
    raise StepNotImplementedError(u'Given an empty car park')


@when(u'A car with the registration plate "abc" enters the car park')
def step_impl(context):
    raise StepNotImplementedError(u'When A car with the registration plate "abc" enters the car park')


@then(u'A car with the same reg number should appear in the car parks list of cars')
def step_impl(context):
    raise StepNotImplementedError(u'Then A car with the same reg number should appear in the car parks list of cars')


@given(u'a carpark that holds a car with the reg number "abc"')
def step_impl(context):
    raise StepNotImplementedError(u'Given a carpark that holds a car with the reg number "abc"')


@when(u'a second car with the reg number "abc" tries to enter the carpark')
def step_impl(context):
    raise StepNotImplementedError(u'When a second car with the reg number "abc" tries to enter the carpark')


@then(u'only one car with the reg number "abc" should occupy a space in the car park')
def step_impl(context):
    raise StepNotImplementedError(u'Then only one car with the reg number "abc" should occupy a space in the car park')

@when(u'a {vehicle} tries to enter the car park')
def step_impl(context):
    raise StepNotImplementedError(u'When a {vehicle} tries to enter the car park')

@then(u'the number of spaces occupied should be {number}')
def step_impl(context):
    raise StepNotImplementedError(u'When a {number} tries to enter the car park')