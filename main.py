"""
    ================
    LOGIN + REGISTRO
    ================
    v.1.0 Login y registro en Flask
    v.0.1 MySQL de los registros de los usuarios
"""
# inicializando librerias
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
# inicializar nuestra clase de conexion para la base de datos
from lib.conexion_Mysql import Base_datos
# instanciar Flask
app = Flask(__name__)
# crear una clave secreta para session
app.secret_key = 'superSecretoooooo'

""" crear rutas """
# ruta / 
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # recuperación de datos de los input
        email = request.form.get('correo')
        password = request.form.get('contrasenya')

        # login
        # primera comprobación, email
        bd = Base_datos('localhost', 'root','root','registro')
        leer_email = bd.query(
            f'SELECT email FROM registrado WHERE email="{email}"'
        )
        # si es verdad ha encontrado el email en la bd
        if leer_email != ():
            # segunda comprobación, email + password
            bd = Base_datos('localhost', 'root','root','registro')
            leer_email_password = bd.query(
            f'SELECT email, password FROM registrado WHERE email="{email}"')

            if leer_email_password[0][0] == email and leer_email_password[0][1] == password:
                # iniciar sesión
                session.clear()
                session['email'] = email
                session['password'] = password

                return redirect(url_for('dentro'))

        return render_template('index.html', usuario_no=True)

    return render_template('index.html')

@app.route('/dentro', methods=['GET','POST'])
def dentro():
    return render_template('dentro.html')



if __name__ == "__main__":
    app.run('127.0.0.1',5500,debug='True')