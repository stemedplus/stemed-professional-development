"""The STEMEd+ disciplines, read from the list shared across STEMEd+ Commons
(stemedplus-theme's stemedplus_disciplines.json, stored here as
stemedplus_disciplines.json; see stemedplus_disciplines.py). Every STEMEd+ board
builds from the same list."""
from . import stemedplus_disciplines as shared

DISCIPLINES = tuple(name for name, _ in shared.rules())
FIELD_DISCIPLINES = shared.field_labels()
