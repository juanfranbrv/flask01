from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    texto1 = ""
    texto2 = ""

    if request.method == 'POST':
        texto1 = request.form.get('texto1', '')
        texto2 = request.form.get('texto2', '')

        if 'borrar' in request.form:
            texto1 = ""
            texto2 = ""
        elif 'swap' in request.form:
            texto1, texto2 = texto2, texto1

    return render_template('index.html', texto1=texto1, texto2=texto2)

if __name__ == '__main__':
    app.run(debug=True)