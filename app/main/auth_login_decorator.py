#-- coding:UTF-8
import jwt
from datetime import datetime
from functools import wraps
from werkzeug.local import LocalProxy
from flask import request, jsonify, _request_ctx_stack, current_app
from datetime import datetime,timedelta
import sys
sys.setdefaultencoding('utf-8')


# LocalProxy的使用说明，很好的一篇文章:https://www.jianshu.com/p/3f38b777a621
current_identity = LocalProxy(lambda: getattr(_request_ctx_stack.top, 'current_identity', None))

def jwt_payload(identity):
    iat = datetime.utcnow()
    exp = iat + timedelta(seconds=3600 * 48)
    return {'exp': exp, 'iat': iat, 'identity': identity }


def jwt_encode(identity):
    # secret = current_app.config['JWT_SECRET_KEY']
    # algorithm = current_app.config['JWT_ALGORITHM']
    # required_claims = current_app.config['JWT_REQUIRED_CLAIMS']

    # JWT_SECRET_KEY = "alita666666"
    # JWT_EXPIRATION_DELTA = timedelta(seconds=3600 * 48)
    # JWT_VERIFY_CLAIMS = ['signature', 'exp', 'iat']
    # JWT_REQUIRED_CLAIMS = ['exp', 'iat']
    # JWT_AUTH_ENDPOINT = 'jwt'
    # JWT_ALGORITHM = 'HS256'
    # JWT_LEEWAY = timedelta(seconds=10)
    # JWT_AUTH_HEADER_PREFIX = 'JWT'
    # JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)


    secret =  "alita666666"
    algorithm ='HS256'
    required_claims = ['exp', 'iat']

    payload = jwt_payload(identity)
    missing_claims = list(set(required_claims) - set(payload.keys()))

    if missing_claims:
        raise RuntimeError('Payload is missing required claims: %s' % ', '.join(missing_claims))

    return jwt.encode(payload, secret, algorithm=algorithm, headers=None)

def jwt_decode(token):
    secret = current_app.config['JWT_SECRET_KEY']
    algorithm = current_app.config['JWT_ALGORITHM']
    leeway = current_app.config['JWT_LEEWAY']

    verify_claims = current_app.config['JWT_VERIFY_CLAIMS']
    required_claims = current_app.config['JWT_REQUIRED_CLAIMS']

    options = {
        'verify_' + claim: True
        for claim in verify_claims
    }
    options.update({
        'require_' + claim: True
        for claim in required_claims
    })

    return jwt.decode(token, secret, options=options, algorithms=[algorithm], leeway=leeway)

def jwt_required(fn):
    @wraps(fn)
    def wapper(*args, **kwargs):
        auth_header_value = request.headers.get('Authorization', None)
        if not auth_header_value:
            return jsonify(code='2100', msg='Authorization缺失')

        parts = auth_header_value.split()
        if len(parts) == 1:
            return jsonify(code='2100', msg='Token缺失') # code 仅作为示例

        elif len(parts) > 2:
            return jsonify(code='2100', msg='Token无效')

        token = parts[1]
        if token is None:
            return jsonify(code='2100', msg='Token异常')

        try:
            payload = jwt_decode(token)
        except jwt.InvalidTokenError as e:
            return jsonify(code='2100', msg=str(e))

        _request_ctx_stack.top.current_identity = payload.get('identity')

        if payload.get('identity') is None:
            return jsonify(code='2100', msg='用户不存在')

        return fn(*args, **kwargs)
    return wapper
