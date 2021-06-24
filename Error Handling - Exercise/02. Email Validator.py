class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


emails = input()

while emails != 'End':
    if '@' not in emails:
        raise MustContainAtSymbolError('Email must contain @')
    else:
        first_email_part, second_email_part = emails.split('@')
        if len(first_email_part) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')
        data, domain = second_email_part.split('.')
        if domain not in ('com, bg, org, net'):
            raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
        else:
            print('Email is valid')
    emails = input()