"""
    Python utiliza Flask para gestionar las sesiones, y no utiliza espacio en memoria como otros lenguajes. Sino que crea un cookie para el contenido de la sesión.
"""

# crear una cookie, nos obliga a cifrar el contenido de la cookie para emplearla como sesión:
app.secret_key = 'mi_super_clave_secreta'

# Añadir contenido a una sesión:
# session['nombre_variable'] = 'valor'
nombre = request.form['nombre']
apellido = request.form['apellido']

session['nombre'] = nombre
session['apellido'] = apellido


# Mostrar contenido de la varible en session:
session['nombre']
session['apellido']

# validar si existe una variable dentro de una sesión:
if 'nombre' in session:
    nombre_nuevo = session['nombre']


""" Cerrar Sesión """
# Elimando variables de la sesión
# borrar variable de la sesión. Pero esta opción la utilizariamos en casa de tener pocas variables o querer eliminar alguna varible, sin cerrar la sesión al completo.
session.pop('nombre', None)
session.pop('apellidos', None)

# Elimar toda la sesión:
# Aquí estoy eliminando todas las variables de sesión, y la cookie.
session.clear()