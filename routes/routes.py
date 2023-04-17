from controllers.controller import *
from controllers.error import *



routes={
    # rutas = '':'','':as_view(),
    'api_rut':'/api','api_cont':apiController.as_view('api'),
    'reg_rut':'/register','reg_cont':registerController.as_view('register'),
    # pagina de error 404 
    'notFound_route': 404, 'not_found_cont':notFoundController.as_view('error')
}