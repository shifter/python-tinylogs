python-tinylogs
===============

A minimalistic class I mostly use in Python scripts to log output in a shell. It is compatible with Python 2.7 and 3.x. It can easily be customized to fit ones needs. 
## Installation
There are multiple ways to use/install this modules:
* Just copy `tinylogs.py` into your project folder.
* Run `python setup.py install` to install `tinylogs` into your global `site-packages` directory.

## Examples
### Basic Usage
```python
from tinylogs import TinyLogs


if __name__ == '__main__':
    # Create a log instance (with debug output)
    log = TinyLogs(debug=True)

    # Log some info
    log.info('Starting code flow')

    # Log some debug information
    log.debug('A fancy debug message')

    if True:
        # Log a warning
        log.warn('Not good, but everything is still OK.')

    if True:
        # Log an error. Error logs and exits.
        log.error('Encountered an error, exiting.')
```
##### Output
![tinylogs output](https://paste.xinu.at/BHk0/)

### Log To File
```python
from tinylogs import TinyLogs


if __name__ == '__main__':
    # Create a log instance that logs into a logfile. multi indicates that
    # logs should be written into a file and additionally printed stdout.
    log = TinyLogs(file='/tmp/logfile', multi=True)

    # Log some info
    log.info('Starting code flow')

    # Log some debug information
    log.debug('A fancy debug message')

    if True:
        # Log a warning
        log.warn('Not good, but everything is still OK.')

    if True:
        # Log an error. Error logs and exits.
        log.error('Encountered an error, exiting.')
```
