from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key ="Luciano Usnayo"

@app.route('/')
def encuesta():
    return render_template('encuesta.html')

@app.route("/formulario", methods=['POST'])
def formulario():
    
    session['usuario'] = request.form['usuario']
    session['ubicación'] = request.form['ubicación']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['comentario']
    
    return redirect('/dojo')

@app.route("/dojo")
def procesado():
    return render_template('dojo.html')





if __name__ == "__main__":
    app.run(debug=True)