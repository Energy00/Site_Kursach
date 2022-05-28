from roof_user.forms import *


def get_context(request):
    context = {
        'reg_form': UserRegForm,
        'phone_form': PhoneNumberForm,
        'log_form': UserAuthForm
    }
    return context
