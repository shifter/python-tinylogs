python-tinylogs
===============

A minimalistic class I mostly use in Python scripts to log output in a shell. It is compatible with Python 2.7 and 3.x. It can easily be customized to fit ones needs. 
### Installation
Either put the class file in the directory of your script, in the python site-packages directory or just include the class itself in your script.

### Usage
```python
from tinylogs import TinyLogs
DEBUG = True

if __name__ == '__main__':
    # Create a global log instance (with debug output)
    global log
    log = TinyLogs(debug=DEBUG)

    # Log some info
    log.info('Starting code flow')

    # Log some debug information
    log.debug('A fancy debug message')

    if True:
        # Log a warning
        log.warning('Not good, but everything is still OK.')

    if True:
        # Log an error. Error logs and exits.
        log.error('Encountered an error, exiting.')
```
### Output
![tinylogs output](https://paste.xinu.at/MGnTo/)
