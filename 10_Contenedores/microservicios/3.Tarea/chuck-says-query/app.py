import configparser

from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.properties')
mongo_uri = config.get('DatabaseSection', 'mongo.uri')
client = MongoClient(mongo_uri)
db = client.test


@app.route("/")
def index():
    return "<h1>Facts Web Service está Activo!</h1>"


@app.route('/facts', methods=['GET'])
def get_facts():
    facts = list(db.facts.find())
    for fact in facts:
        fact['_id'] = str(fact['_id'])
    print(facts)
    return jsonify(facts)


@app.route('/facts/<id>', methods=['GET'])
def get_fact(id):
    fact = db.facts.find_one({'id': int(id)})
    if fact:
        fact['_id'] = str(fact['_id'])
        print(fact)
        return jsonify(fact)
    else:
        return jsonify({"error": "Fact not found"}), 404


@app.route('/facts/last3days', methods=['GET'])
def get_facts_last_3_days():
    # Calcula la fecha y hora límite (tres días atrás desde ahora)
    three_days_ago = datetime.now() - timedelta(days=3)
    three_days_ago_timestamp = int(three_days_ago.timestamp() * 1000)  # Convertir a milisegundos

    # Filtra los documentos de MongoDB basándote en el timestamp
    facts = list(db.facts.find({"timestamp": {"$gte": three_days_ago_timestamp}}))

    # Convierte el ObjectId en una cadena para JSON
    for fact in facts:
        fact['_id'] = str(fact['_id'])

    # Devuelve los documentos como una respuesta JSON
    return jsonify(facts)


@app.route('/facts/last3days/<int:id>', methods=['GET'])
def get_fact_last_3_days(id):
    # Calcula la fecha y hora límite (tres días atrás desde ahora)
    three_days_ago = datetime.now() - timedelta(days=3)
    three_days_ago_timestamp = int(three_days_ago.timestamp() * 1000)  # Convertir a milisegundos

    # Filtra el documento de MongoDB basándote en el timestamp y el id
    fact = db.facts.find_one({"id": id, "timestamp": {"$gte": three_days_ago_timestamp}})

    if fact:
        # Convierte el ObjectId en una cadena para JSON
        fact['_id'] = str(fact['_id'])
        return jsonify(fact)
    else:
        return jsonify({"error": "Fact not found"}), 404


@app.route('/facts/last3days/<date>', methods=['GET'])
def get_facts_by_date(date):
    try:
        # Convertir la fecha proporcionada a datetime
        input_date = datetime.strptime(date, "%Y-%m-%d")

        # Calcular la fecha límite (tres días atrás desde ahora)
        three_days_ago = datetime.now() - timedelta(days=3)

        # Verificar que la fecha proporcionada no sea anterior a tres días atrás
        if input_date < three_days_ago:
            return jsonify({"Error": "El dato es mas antiguo que los ultimos 3 dias. No hay Facts disponibles"}), 404

        # Convertir la fecha proporcionada a timestamp en milisegundos
        provided_timestamp_start = int(input_date.timestamp() * 1000)
        provided_timestamp_end = provided_timestamp_start + 86400000  # Añadir un día en milisegundos

        # Filtrar los documentos de MongoDB basándote en el timestamp del día completo
        facts = list(db.facts.find({
            "timestamp": {"$gte": provided_timestamp_start, "$lt": provided_timestamp_end}
        }))

        # Verificar si no hay datos para la fecha solicitada
        if not facts:
            return jsonify({"error": f"No hay facts encontrados para el {date}"}), 404

        # Convertir ObjectId a cadena para JSON
        for fact in facts:
            fact['_id'] = str(fact['_id'])

        # Devolver los documentos como una respuesta JSON
        return jsonify(facts)

    except ValueError:
        return jsonify({"error": "Formato invalido. e.g valido: http://localhost:48080/facts/last3days/YYYY-MM-DD"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(config.get('ServerSection', 'server.port')))
