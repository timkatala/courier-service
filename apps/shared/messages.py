# Django
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ngettext_lazy

DATE_TIME_FORMAT = 'YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]'
DATE_FORMAT = 'YYYY[-MM[-DD]]'
INVALID_REQUIRED = _('This field is required.')
INVALID_PASSWORD_ENTIRELY_NUMERIC = _('This password is too common.')
INVALID_BLANK = _('This field may not be blank.')
INVALID_STRING = _('Not a valid string.')
INVALID_NUMBER = _('A valid number is required.')
INVALID_BOOLEAN = _('"{input}" is not a valid boolean.')
INVALID_NULL = _('This field may not be null.')
INVALID_CHOICE = _('"{input}" is not a valid choice.')
INCORRECT_TYPE_PK = _(
    'Incorrect type. Expected pk value, received {data_type}.')

INVALID_DICT = _("Invalid data. Expected a dictionary, but got {datatype}.")
INCORRECT_DATE_FORMAT = _('Date has wrong format. '
                          'Use one of these formats instead: {format}.')
INCORRECT_DATETIME_FORMAT = _(
    'Datetime has wrong format. '
    'Use one of these formats instead: {format}.'
)

INCORRECT_PK_TYPE = _('Incorrect type. '
                      'Expected pk value, received {data_type}.')
INVALID_OBJECT404 = _('Invalid pk "{pk_value}" - object does not exist.')
CREATED = _('Created')
UPDATED = _('Updated')
NOT_OWNER_PERMISSION = _('You not owner of this company')
INVALID_UNIQUE = _('%(model_name)s with this %(field_label)s already exists.')
NO_FILE_WAS_SUBMITTED = _('No file was submitted.')


def invalid_unique(model_name, field_label):
    return INVALID_UNIQUE % dict(
        model_name=model_name,
        field_label=field_label)


def invalid_boolean(value):
    return INVALID_BOOLEAN.format(input=value)


def invalid_choice(value):
    return INVALID_CHOICE.format(input=value)


def invalid_object404(pk):
    return INVALID_OBJECT404.format(pk_value=pk)


def incorrect_pk_type(value):
    return INCORRECT_PK_TYPE.format(data_type=type(value).__name__)


def incorrect_datetime_format(value=DATE_TIME_FORMAT):
    return INCORRECT_DATETIME_FORMAT.format(format=value)


def incorrect_date_format(value):
    return INCORRECT_DATE_FORMAT.format(format=value)


def invalid_password_min_length(min_length):
    return ngettext_lazy(
        'This password is too short. '
        'It must contain at least %(min_length)d character.',
        'This password is too short. '
        'It must contain at least %(min_length)d characters.',
        min_length
    ) % dict(min_length=min_length)
