from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log_page():
    tiempo = datetime.now().time()
    temperatura = request.args.get('t')
    humedad = request.args.get('h')

    file = open(str(datetime.now().date()) + ".csv","a+")
    file_input = "Tiempo,Temperatura,Humedad\n"+str(tiempo)+","+str(temperatura)+","+str(humedad)+"\n"
    file.write(file_input)
    file.close
    return render_template('log.html', t = datetime.now().date())

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)