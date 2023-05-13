"""
Author Sanatjon Burkhanov
github: posesred
routing for the api
"""
from fastapi.routing import APIRoute
from app import app
from app.endpoints.urls import APIPrefix


def use_route_names_as_operation_id(app):
    """
    It takes a FastAPI app and sets the operation_id of
    each route to be the tag, name, and method of the route
    :param app:
    :return:
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            method = list(route.methods)[0].lower()
            route.operation_id = f'{route.tags[0]}{route.name}_{method}'


def add_new_route():
    """
    It imports all the routers from the routes.include list
    and includes them in the app
    :return: The app object is being returned.
    """
    for route in APIPrefix.include:
        exec(f'from app.api.{route}.views import router as {route}')
        exec(f'app.include_router({route})')
    use_route_names_as_operation_id(app)
    return app
