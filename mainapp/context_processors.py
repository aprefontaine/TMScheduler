from google.appengine.api import users

"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

def googleUser(request):
    GOOGLE_User = users.get_current_user()
    if not GOOGLE_User:
        GOOGLE_Auth_Url = users.create_login_url('/prefs')     # Path to redirect too after login.
    else:
        GOOGLE_Auth_Url = users.create_logout_url('/')               # Return to home after a logout

    context_extras = {}
    context_extras['GOOGLE_User'] = GOOGLE_User
    context_extras['GOOGLE_Auth_Url'] = GOOGLE_Auth_Url

    return context_extras