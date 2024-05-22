from pyramid.view import view_config
from pyramid.request import Request
from pyramid.response import Response
import pyramid.httpexceptions as x
from list_activity_tracker.services.user_query_service import create_user , get_user_by_username

@view_config(route_name='home', renderer='list_activity_tracker:templates/home/home.pt')
def my_view(request):
    return {'project': 'list_activity_tracker'}


#################### Register ##############
@view_config(route_name='register', renderer='list_activity_tracker:templates/account/register.pt',
             request_method='GET')
def register_get(request: Request):
    return {}


@view_config(route_name='register', renderer='list_activity_tracker:templates/account/register.pt',
             request_method='POST')
def register_post(request: Request):

    if 'submit' in request.params:
        username = request.params['username']
        password = request.params['password']
        create_user(username,password)
        return x.HTTPFound("/login")

################ LOGIN ######################

@view_config(route_name='login', renderer='list_activity_tracker:templates/account/login.pt',request_method='GET')
def login_get(request: Request):
    return {}

@view_config(route_name='login', renderer='list_activity_tracker:templates/account/login.pt', request_method='POST')
def login_post(request: Request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    request.session['username'] = username
    request.session['password'] = password
    user = get_user_by_username(username)
    if not user:
        return {}
    return x.HTTPFound('/account')





##### Account Index ##########
@view_config(route_name='account', renderer='list_activity_tracker:templates/account/account.pt', request_method='GET')
def account_get(request: Request):
    username = request.session.get('username')
    print(username)
    return {"username": username, "password": request.session.get('password')}