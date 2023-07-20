from flask import Flask, jsonify, request,abort #importo l oque necesito
import copa_controller_poo
from copa_db import create_tables
from exchange_rate import get_xr
from copa_db import get_db

app = Flask(__name__)

#comienzo a hacer las rutas que son las que va a usar el usuario para acceder a los datos
@app.route('/api/copadavis/precios', methods=["GET"])
def get_copas():
    copas = copa_controller_poo.get_copas()
    copas_list=[]
    for copa in copas:
        elem = copa.serialize()
        copas_list.append(elem)
    return jsonify(copas_list)

@app.route("/api/copadavis/precios", methods=["POST"])
def insert_copa():
    copa_details = request.get_json()
    id= copa_details["id"]
    estadio = copa_details["estadio"]
    partido =copa_details["partido"]
    precio = copa_details["precio"]
    sector = copa_details["sector"]
    result = copa_controller_poo.insert_copa(id,estadio,partido,precio,sector)
    return jsonify(result)






@app.route("/api/copadavis/comprar/<id>/cantidad/<cantidad>", methods=["GET"])
def get_copa_by_id_psa(id, cantidad):
    try:
        copa = copa_controller_poo.get_by_id(id)

        if copa is None:
            return "El ID es obligatorio.", 404

        xr = get_xr()
        cantidad = int(cantidad)  # Convertir cantidad a un número entero

        price_peso = copa['precio'] * cantidad
        price_dolar = price_peso / xr
        price_descuento = price_peso * 0.85

        response_text = f"Precio en pesos: {price_peso}, Precio en dólares: {price_dolar}, Precio con descuento AAT: {price_descuento}"
        return response_text
    except Exception as e:
        return f"Error: El ID no existe o el parámetro es inválido.", 400

create_tables()

if __name__ == '__main__':
    app.run()
