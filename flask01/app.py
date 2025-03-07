from flask import Flask
app = Flask(__name__)
@app.route('/saludar')
def hola_mundo():
    return 'Hola a todos amigos!!!! :)'

@app.route('/despedir')
def adios_mundo():
    return 'Adios mundo!!!!'

@app.route('/hola')
def hola_html():
    return '<h1 style="color:red;">Hola!!</h1>'

@app.route('/json')
def json():
    return '{"nombre":"John"}'

@app.route('/xml')
def xml():
    return '<nombre>John</nombre>'



if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)

