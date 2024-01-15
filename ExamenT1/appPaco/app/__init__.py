from flask import *
from tienda.tiendaRoutes import tiendasBP
from empleados.empleadosRoutes import empleadosBP
from usuarios.usuarioRoutes import usuariosBP
from flask_jwt_extended import JWTManager

#Creamos una nueva instancia de una aplicación flask que se usará para manejar
#solicitudes web y definir rutas, vistas y comportamientos específicos de la app.
app = Flask(__name__) #__name__ es una variable especial en Python que se refiere al nombre del módulo donde se encuentra el código.
app.config['SECRET_KEY'] = 'clave123'
jwt = JWTManager(app)

app.register_blueprint(tiendasBP, url_prefix='/tiendas')
app.register_blueprint(empleadosBP, url_prefix='/empleados')
app.register_blueprint(usuariosBP, url_prefix='/usuarios')