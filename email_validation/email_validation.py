import re
import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(':')


class Email:
    def __init__(self, address: str):
        if self.validate(address):
            self.address = address
            _logger.info(f'\t<{address}> is a valid email address.')
        else:
            self.address = None
            _logger.warning(f'\t<{address}> is NOT a valid email.')

    @classmethod
    def validate(cls, address: str) -> bool:
        if not isinstance(address, str) or not address:
            return False
        email_validate_pattern = re.compile(
            r'^(?![.-])'  # Local part should not start with a dot or hyphen
            r'^(?!.*\.\.)'  # Prevent consecutive dots in any part
            r'[a-zA-Z0-9._%+-]+'  # Local part can include alphanumeric characters and special characters . _ % + -
            r'(?<![._%+-])'  # Local part should not end with characters [._%+-]
            r'@[a-zA-Z0-9-]+'  # Domain part have to start with @ and can include alphanumeric characters and hyphens
            r'(?:\.[a-zA-Z0-9-]+)*'  # Allow subdomains with the same rules as the domain part
            r'\.[a-zA-Z]{2,}$'  # Top-level domain (e.g., .com, .org) - should start with a dot followed by at least
            # two alphabetic characters
        )
        is_valid = email_validate_pattern.match(address)
        return bool(is_valid)


if __name__ == '__main__':
    emails = ('abc-d@mail.com', 'abc.def@mail.com', 'abc.def@mail.com',
              'abc_def@mail.com', 'abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com',
              'abc#def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com',
              'abc.def@mail.org', 'abc.def@mail.com', 'abc.def@mail.c',
              'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com',
              'abc-d@mail.com.', 'abc-d@mail.com ', 'adbyers@aah-n3.co.uk')

    for email in emails:
        email_address = Email(email)
