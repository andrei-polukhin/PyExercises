"""
Let employees to apply to leaves: medical, unpaid, paid, etc.
"""
from datetime import datetime

import tinyrpcxt
from formencode import validators

from .pgsql import pgsql


class Schema:
  """Schema for the ``apply_to_leave`` API method"""

  employees_id = validators.Int(not_empty=True)
  leaves_type = validators.OneOf(['medical', 'paid', 'unpaid'])
  start_date = validators.DateValidator(not_empty=True)
  end_date = validators.DateValidator(not_empty=True)
  notes = validators.String()


@tinyrpcxt.public(schema=Schema)
def apply_to_leave(
  employees_id: int, leaves_type: str, start_date: datetime, end_date: datetime, notes: str
) -> None:
  """Apply to leaves"""

  # leaves(employees_id) -> employees(id) FK assumed
  if not pgsql().get.row('employees', [('id', '=', employees_id)]):
    raise Exception('No such an employee!')

  data = {
    'employees_id': employees_id,
    'type': leaves_type,
    'start_date': start_date,
    'end_date': end_date,
    'notes': notes,
  }
  return pgsql().query.insert('leaves', data)
