SANIC_JWT_ACCESS_TOKEN_NAME = 'access_token'
SANIC_JWT_ALGORITHM = 'HS256'
SANIC_JWT_AUTHORIZATION_HEADER = 'authorization'
SANIC_JWT_AUTHORIZATION_HEADER_PREFIX = 'Bearer'
SANIC_JWT_AUTHORIZATION_HEADER_REFRESH_PREFIX = 'Refresh'
SANIC_JWT_CLAIM_AUD = None  # String
SANIC_JWT_CLAIM_IAT = None  # Boolean
SANIC_JWT_CLAIM_ISS = None  # String
SANIC_JWT_CLAIM_NBF = None  # Boolean
SANIC_JWT_CLAIM_NBF_DELTA = 0
SANIC_JWT_COOKIE_DOMAIN = ''
SANIC_JWT_COOKIE_HTTPONLY = True
SANIC_JWT_COOKIE_SET = False
SANIC_JWT_COOKIE_TOKEN_NAME = SANIC_JWT_ACCESS_TOKEN_NAME
SANIC_JWT_EXPIRATION_DELTA = 60 * 5 * 6
SANIC_JWT_HANDLER_PAYLOAD = 'sanic_jwt.handlers.build_payload'
SANIC_JWT_HANDLER_PAYLOAD_EXTEND = 'sanic_jwt.handlers.extend_payload'
SANIC_JWT_HANDLER_PAYLOAD_SCOPES = None
SANIC_JWT_LEEWAY = 60 * 3
SANIC_JWT_REFRESH_TOKEN_ENABLED = False
SANIC_JWT_REFRESH_TOKEN_NAME = 'refresh_token'
SANIC_JWT_SCOPES_NAME = 'scopes'
SANIC_JWT_SECRET = 'This is a big secret. Shhhhh'
SANIC_JWT_URL_PREFIX = '/auth'
SANIC_JWT_USER_ID = 'user_id'

SANIC_JWT_COOKIE_REFRESH_TOKEN_NAME = SANIC_JWT_REFRESH_TOKEN_NAME
