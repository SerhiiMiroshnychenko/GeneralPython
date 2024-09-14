import logging
from loguru import logger

_logger = logging.getLogger(__name__)


def main():
    logger.debug('DEBUG')
    _logger.debug('DEBUG')
    logger.info('INFO')
    _logger.info('INFO')
    logger.warning('WARNING')
    _logger.warning('WARNING')
    logger.error('ERROR')
    _logger.error('ERROR')
    logger.critical('CRITICAL')
    _logger.critical('CRITICAL')


if __name__ == '__main__':
    main()
