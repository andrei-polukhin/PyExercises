"""
Let employees apply to leaves: medical, unpaid, paid, etc.
"""

from datetime import datetime

import formencode
from tinyrpc import dispatcher
from formencode import validators

from .pgsql import pgsql


class EmployeeObject:
    """Mock employee object"""

    def __init__(self, not_empty=False) -> None:
        self.not_empty = not_empty


class Schema(formencode.Schema):
    """Schema for the ``apply_to_leave`` API method"""

    employees_id = EmployeeObject(not_empty=True)
    leaves_type = validators.OneOf(['medical', 'paid', 'unpaid'])
    start_date = validators.DateValidator(not_empty=True)
    end_date = validators.DateValidator(not_empty=True)
    notes = validators.String(max=512)

    chained_validators = [
        ('start_date', '<', 'end_date')
    ]


@dispatcher.public(schema=Schema)
def apply_to_leave(
  employees_id: int, leaves_type: str, start_date: datetime, end_date: datetime, notes: str
) -> None:
    """Apply to leaves"""

    data = {
        'employees_id': employees_id,
        'type': leaves_type,
        'start_date': start_date,
        'end_date': end_date,
        'notes': notes,
    }
    return pgsql().query.insert('leaves', data)
