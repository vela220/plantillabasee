from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Diccionario para guardar usuarios (en memoria)
usuarios = {}

@app.route('/')
def home():
    if 'username' in session:
        user = usuarios.get(session['username'])
        return f"""
            <h2>Hola, {user['nombre']} {user['apellido']}! Has iniciado sesión.</h2>
            <p>Email: {user['email']}</p>
            <p>Fecha de nacimiento: {user['birthdate']}</p>
            <p>Género: {user['gender']}</p>
            <br>
            <a href='/logout'>Cerrar sesión</a>
        """
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']

        # Buscar usuario por email
        usuario_encontrado = None
        username_encontrado = None
        for username, datos in usuarios.items():
            if datos['email'].lower() == email:
