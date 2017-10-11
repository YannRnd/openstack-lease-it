"""
This module manage configuration file.
* /etc/openstack-lease-it/config.ini
* $HOME/.lease-it.ini
"""
import ConfigParser
import os

# List possible configuration file, last item has highest priority
CONFIG_FILES = (
    '/etc/openstack-lease-it/config.ini',
    os.path.expanduser('~') + '/.lease-it.ini',
)


OPTIONS = {
    # [django] section
    'SECRET_KEY': {
        'section': 'django',
        'option': 'secret_key'
    },
    'DEBUG': {
        'section': 'django',
        'option': 'debug'
    },
    'LOGDIR': {
        'section': 'django',
        'option': 'log_dir'
    },
    'LOGLEVEL': {
        'section': 'django',
        'option': 'log_level'
    },

    # [openstack] section
    'OS_USERNAME': {
        'section': 'openstack',
        'option': 'OS_USERNAME'
    },
    'OS_PASSWORD': {
        'section': 'openstack',
        'option': 'OS_PASSWORD'
    },
    'OS_TENANT_NAME': {
        'section': 'openstack',
        'option': 'OS_TENANT_NAME'
    },
    'OS_PROJECT_NAME': {
        'section': 'openstack',
        'option': 'OS_PROJECT_NAME'
    },
    'OS_AUTH_URL': {
        'section': 'openstack',
        'option': 'OS_AUTH_URL'
    },
    'OS_CACERT': {
        'section': 'openstack',
        'option': 'OS_CACERT'
    },
    'OS_IDENTITY_API_VERSION': {
        'section': 'openstack',
        'option': 'OS_IDENTITY_API_VERSION'
    },
    'OS_PROJECT_DOMAIN_NAME': {
        'section': 'openstack',
        'option': 'OS_PROJECT_DOMAIN_NAME'
    },
    'OS_USER_DOMAIN_NAME': {
        'section': 'openstack',
        'option': 'OS_USER_DOMAIN_NAME'
    },

    # [memcached] section
    'MEMCACHED_HOST': {
        'section': 'memcached',
        'option': 'host'
    },
    'MEMCACHED_PORT': {
        'section': 'memcached',
        'option': 'port'
    },

    # [plugins] section
    'BACKEND_PLUGIN': {
        'section': 'plugins',
        'option': 'backend'
    },

    # [notification] section
    'NOTIFICATION_SSL': {
        'section': 'notification',
        'option': 'ssl'
    },
    'NOTIFICATION_SMTP': {
        'section': 'notification',
        'option': 'smtp'
    },
    'NOTIFICATION_USERNAME': {
        'section': 'notification',
        'option': 'username'
    },
    'NOTIFICATION_PASSWORD': {
        'section': 'notification',
        'option': 'password'
    },
    'NOTIFICATION_EMAIL_HEADER': {
        'section': 'notification',
        'option': 'email_header'
    },
    'NOTIFICATION_SUBJECT': {
        'section': 'notification',
        'option': 'subject'
    },
    'NOTIFICATION_LINK': {
        'section': 'notification',
        'option': 'link'
    },
    'NOTIFICATION_DEBUG': {
        'section': 'notification',
        'option': 'debug'
    },
    'NOTIFICATION_DOMAIN': {
        'section': 'notification',
        'option': 'default_domain'
    }
}


def load_config_option(global_config, config, name, option):
    """
    This function overwrite the current global_config[name] value
    with option
    :param global_config: The actual configuration
    :param config: The new configuration
    :param name: Name of value we will overwrite
    :param option: Option section and value on config
    :return: void
    """
    try:
        global_config[name] = config.get(option['section'],
                                         option['option'])
    except ConfigParser.NoSectionError:
        pass
    except ConfigParser.NoOptionError:
        pass


def load_config():
    """
    Define default configuration, *NOT* all value have a default
    :return: dict of configuration
    """
    global_configuration = {
        # Django parameters
        'DEBUG': 'False',
        'LOGDIR': '/var/log/openstack-lease-it/',
        'LOGLEVEL': 'INFO',

        # OpenStack parameters
        'OS_USERNAME': 'admin',
        'OS_TENANT_NAME': 'admin',
        'OS_PROJECT_NAME': 'admin',
        'OS_IDENTITY_API_VERSION': '3',
        'OS_USER_DOMAIN_NAME': 'default',
        'OS_PROJECT_DOMAIN_NAME': 'default',

        # memcached parameter
        'MEMCACHED_HOST': '127.0.0.1',
        'MEMCACHED_PORT': '11211',

        # plugins parameter
        'BACKEND_PLUGIN': 'Openstack',

        # notification parameter
        'NOTIFICATION_DEBUG': 'False',
        'NOTIFICATION_DOMAIN': ''

    }
    config = ConfigParser.RawConfigParser()

    for config_file in CONFIG_FILES:
        config.read(config_file)
        for option in OPTIONS:
            load_config_option(global_configuration,
                               config,
                               option,
                               OPTIONS[option])

    return global_configuration
