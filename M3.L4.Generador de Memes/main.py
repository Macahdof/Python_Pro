# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Assignment #3. Receiving the text's positioning
        posicion_superior = request.form.get('textTop_y')
        posicion_inferior = request.form.get('textBottom_y')

        # Asignación #3. Recepción del posicionamiento del texto
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 

                               # Asignación #2. Visualización del texto
                               text_top=text_top,
                               text_bottom=text_bottom,

                               #  Asignación #3. Visualización del color
                               posicion_superior=posicion_superior,
                               posicion_inferior=posicion_inferior,

                               
                               # Asignación #3. Visualización de la posición del texto
                               selected_color = selected_color
                            

                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
