try:
    from .dev import *
except IOError:
    from .production import *