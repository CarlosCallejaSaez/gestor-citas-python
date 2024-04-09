from flask import Flask, render_template, request, redirect

app = Flask(__name__)

citas = []

@app.route('/')
def index():
    return render_template('index.html', citas=citas)

@app.route('/agregar_cita', methods=['POST'])
def agregar_cita():
    fecha = request.form['fecha']
    descripcion = request.form['descripcion']
    citas.append({'fecha': fecha, 'descripcion': descripcion})
    return redirect('/')

@app.route('/eliminar_cita/<int:index>', methods=['POST'])
def eliminar_cita(index):
    del citas[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
