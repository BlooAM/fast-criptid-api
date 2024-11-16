from datetime import datetime, timedelta
import os
from jose import jwt
from model.user import User

if os.getenv('CRYPTID_UNIT_TEST'):
    from fake import user as data
else:
    from data import user as data

