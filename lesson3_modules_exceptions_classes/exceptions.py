try:
    1 / 0
except ZeroDivisionError:
    print('Error div 0')

print('I\'m working')
print('---------------------')

try:
    1 / 0
    '42' + 10
except ZeroDivisionError:
    print('Error div 0')

print('I\'m still working')
print('---------------------')


try:
    1 / 0
    print('Zero')
    '42' + 10
    print('Type')
    [1, 2][2]
    print('Index')
except (ZeroDivisionError, TypeError, IndexError) as e:
    print(type(e), e)
    print('Error div 0 or TypeError or IndexError')

print('I\'m still working')
print('---------------------')

try:
    [1, 2][2]
    print('Index')
except ZeroDivisionError:
    print('Error div 0')
except TypeError:
    print('TypeError')
except IndexError:
    print('IndexError')

print('I\'m still working')
print('---------------------')

try:
    #1 / 0
    #print('Zero')
    #'42' + 10
    #print('Type')
    [1, 2][2]
    print('Index')
except Exception as e:
    print('Got Exception', type(e))

print('I\'m still working')
print('---------------------')

try:
    #1 / 0
    #print('Zero')
    #'42' + 10
    #print('Type')
    exc = Exception('spam', 'eggs')
    print('exc == ', exc)
    raise exc
except Exception as e:
    print('Got Exception', type(e), e.args, type(e.args))

print('I\'m still working')
print('---------------------')

def fails():
    1 / 0

try:
    fails()
except Exception as e:
    print('Got Exception', type(e), e.args, type(e.args))

print('I\'m still working')
print('---------------------')

import logging

logging.basicConfig(level=logging.INFO)
# debug
# info
# warning
# error
# critical

def fails():
    1 / 0

try:
    fails()
except Exception as e:
    print('Got Exception', type(e), e.args, type(e.args))

logging.debug('I\'m still working')
logging.info('I\'m still working')
logging.warning('I\'m still working')
logging.error('I\'m still working')
logging.critical('I\'m still working')
print('---------------------')

logging.basicConfig(
    format='%(filename)s[LINE:%(lineno)d# \
           %(levelname)-8s [%asctime)s] %(message)s',
    level=logging.DEBUG
)

def fails():
    logging.info('Entered fails')
    1 / 0

try:
    fails()
except Exception as e:
    print('Got Exception', type(e), e.args, type(e.args))

print('---------------------')
print('traceback')

def fails():
    1 / 0

try:
    fails()
except Exception as e:
    logging.error('Got Exception', exc_info=e)

print('---------------------')
