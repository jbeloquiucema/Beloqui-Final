from flask import Flask, jsonify, request
import dieta_controller_poo
from db_dietas import create_tables
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/api/dreamfly/dietas', methods=["GET"])
def get_dietas():
    dietas = dieta_controller_poo.get_dietas()
    dietas_list=[]
    for dieta in dietas:
        elem = dieta.serialize()
        dietas_list.append(elem)
    return jsonify(dietas_list)

@app.route("/api/dreamfly/dietas", methods=["POST"])
def insert_dieta():
    dieta_details = request.get_json()
    id = dieta_details["id"]
    Restriction = dieta_details["Restriction"]
    Restriccion = dieta_details["Restriccion"]
    USD = dieta_details["USD"]
    result = dieta_controller_poo.insert_dieta(id, Restriction, Restriction, USD)
    return jsonify(result)



@app.route("/dieta/<id>/pais/ARG", methods=["GET"])
def get_dieta_by_id(id):
    dieta = dieta_controller_poo.get_by_id(id)
    if id == None:
        return jsonify({"error": "el parametro es obligatorio"})
    else:
        xr = get_xr()
        price_usd = dieta['price']*xr
        dieta['USD'] = round(price_usd,2)
        return jsonify(dieta)

create_tables()

app.run()

if __name__ == '__main__':
    app.run()
