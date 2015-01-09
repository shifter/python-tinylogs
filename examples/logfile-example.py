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