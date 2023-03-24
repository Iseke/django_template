# SECURITY WARNING: keep the secret key used in production secret!

SECRET_FILE = PROJECT_ROOT / 'run' / 'SECRET.key'

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

if SECRET_KEY is None:
    logger.debug('Could not find key in the environment!')

    logger.debug('Trying to read SECRET_KEY from SECRET_FILE...')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
        logger.info('Read SECRET_KEY from SECRET_FILE.')
    except IOError:
        logger.debug('Could not open SECRET_FILE ({})!'.format(SECRET_FILE))

        try:
            from django.utils.crypto import get_random_string
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
            SECRET_KEY = get_random_string(50, chars)
            with open(SECRET_FILE, 'w') as f:
                f.write(SECRET_KEY)

            logger.info('Generated a new SECRET_KEY and stored it in SECRET_FILE ({})!'.format(SECRET_FILE))
        except IOError:
            logger.exception('Could not open SECRET_FILE ({}) for writing!'.format(SECRET_FILE))
            raise Exception('Could not open {} for writing!'.format(SECRET_FILE))
else:
    logger.info('Fetched SECRET_KEY from environment.')
