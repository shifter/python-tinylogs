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