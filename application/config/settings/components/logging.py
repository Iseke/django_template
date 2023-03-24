import structlog

_TIME_STAMPER = '%Y-%m-%d %H:%M:%S'

pre_chain = [
    structlog.stdlib.add_log_level,
    structlog.processors.TimeStamper(fmt=_TIME_STAMPER)
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'json_formatter': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.JSONRenderer(),
            'foreign_pre_chain': pre_chain,
        },
        'console_colored': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.dev.ConsoleRenderer(colors=True),
            'foreign_pre_chain': pre_chain,
        },
        'console_plain': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.dev.ConsoleRenderer(colors=False),
            'foreign_pre_chain': pre_chain,
        },
        'key_value': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.KeyValueRenderer(key_order=['timestamp', 'level', 'event', 'logger']),
            'foreign_pre_chain': pre_chain,
        },
    },

    'handlers': {
        'flat_line_file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': PROJECT_ROOT / 'logs' / 'flat_line.log',
            'formatter': 'key_value',
        },
        'json_console': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': PROJECT_ROOT / 'logs' / 'json.log',
            'formatter': 'json_formatter',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_colored',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': environ.get('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'security': {
            'handlers': ['console', 'json_console'],
            'propagate': False,
            'level': 'ERROR',
        },
    },
}

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt=_TIME_STAMPER),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.ExceptionPrettyPrinter(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
