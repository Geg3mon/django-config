DJOSER = {
    'USER_CREATE_PASSWORD_RETYPE': True,
    'ACTIVATION_URL': 'auth/users/activation/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFRIMATION_EMAIL':True,
    'LOGIN_FIELD': 'email',
    'USER_ID_FIELD': 'username',
    # 'TOKEN_MODEL': 'rest_framework.authentication.TokenAuthentication',
    'EMAIL':{
        'activation': 'djoser.email.ActivationEmail',

    },
    # 'SERIALIZERS': {
    #     "user_create": "djoser.serializers.UserCreateSerializer",
    #     "user": "djoser.serializers.UserSerializer",
    #     "current_user": "djoser.serializers.UserSerializer",
    #     "user_delete": "djoser.serializers.UserSerializer",
    # }
}
