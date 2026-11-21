from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = int((nota1 + nota2 + nota3) / 3)

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        return render_template('ejercicio1.html', estado=estado, promedio=promedio)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        letras1 = len(nombre1)
        letras2 = len(nombre2)
        letras3 = len(nombre3)

        if letras1 > letras2 and letras1 > letras3:
            mayorNombre = nombre1
            cantidad = letras1
        elif letras2 > letras1 and letras2 > letras3:
            mayorNombre = nombre2
            cantidad = letras2
        elif letras3 > letras1 and letras3 > letras2:
            mayorNombre = nombre3
            cantidad = letras3

        else:
            iguales = 1
            return render_template('ejercicio2.html', iguales=iguales)


        return render_template('ejercicio2.html', mayorNombre=mayorNombre, cantidad=cantidad)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)