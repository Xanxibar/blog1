try:
    from .dev import *
except ImportError:
    from .production import *


SECRET_KEY = 'na!1i(grfayqf3sth=*h%yj2+z!q**t6@lfp_u365m!_%f=5ut'