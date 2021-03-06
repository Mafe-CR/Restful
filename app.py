#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
ClientesDB = [
 {
 'id':'00055671',
 'nombre':'Juan',
 'apellidos':'Perez Lopez',
 'direccion':'Calle 25 N 45-35',
 'codigopostal':'130001'
 },
]
FacturasDB = [
 {
     'id':'01',
     'total':'24.000',
     'fecha':'16/11/2020',
     'cliente':'Juan',
     'items':'',
 },
]
TrayectoriasDB = [
 {
     'id':'00034',
     'origen':'local',
     'destino':'Africa',
     'costo':'11.350',
 },
]
PaquetesDB = [
 {
    'id' : '001',
    'nombre' : '',
    'precio' : '12.000'
 },
]

@app.route('/clientes' or '/clientes/',methods=['GET'])
def get_all_clientes():
    return jsonify({'clientes': ClientesDB})


@app.route('/clientes/<Id>',methods=['GET'])
def get_clientes(Id):
    clientes = [clientes for clientes in ClientesDB if (clientes['id'] == Id)]
    return jsonify({'est': clientes})

@app.route('/facturas',methods=['GET'])
def get_all_factiras():
    return jsonify({'facturas': FacturasDB})


@app.route('/facturas/<Id>',methods=['GET'])
def get_facturas(Id):
    factura = [factura for factura in FacturasDB if (factura['id'] == Id)]
    return jsonify({'est': factura})

@app.route('/trayectorias',methods=['GET'])
def get_all_trayectorias():
    return jsonify({'trayectorias': TrayectoriasDB})


@app.route('/trayectorias/<Id>',methods=['GET'])
def get_trayectorias(Id):
    trayectoria = [trayectoria for trayectoria in TrayectoriasDB if (trayectoria['id'] == Id)]
    return jsonify({'est': trayectoria})

@app.route('/paquetes',methods=['GET'])
def get_all_paquetes():
    return jsonify({'paquetes': PaquetesDB})

@app.route('/paquetes/<Id>',methods=['GET'])
def get_paquetes(Id):
    paquetes = [paquetes for paquetes in PaquetesDB if (paquetes['id'] == Id)]
    return jsonify({'est': paquetes})


@app.route('/clientes/<Id>',methods=['PUT'])
def update_clientes(Id):
    row = [clientes for clientes in ClientesDB if (clientes['id'] == Id)]
    if 'nombre' in request.json:
        row[0]['name'] = request.json['name']
    if 'apellidos' in request.json:
        row[0]['apellidos'] = request.json['apellidos']
    if 'direccion' in request.json:
        row[0]['direccion'] = request.json['direccion']
    if 'codigopostal' in request.json:
        row[0]['codigopostal'] = request.json['codigopostal']
    return jsonify({'cliente': row[0]})

@app.route('/facturas/<stdId>',methods=['PUT'])
def update_facturas(stdId):
    row = [factura for factura in FacturasDB if (factura['id'] == stdId)]
    if 'total' in request.json:
        row[0]['total'] = request.json['total']
    if 'fecha' in request.json:
        row[0]['fecha'] = request.json['fecha']
    if 'cliente' in request.json:
        row[0]['cliente'] = request.json['cliente']
    return jsonify({'cliente': row[0]})    

@app.route('/paquetes/<Id>',methods=['PUT'])
def update_paquetes(Id):
    row = [paquetes for paquetes in FacturasDB if (paquetes['id'] == Id)]
    if 'nombre' in request.json:
        row[0]['nombre'] = request.json['nombre']
    if 'precio' in request.json:
        row[0]['precio'] = request.json['precio']
    return jsonify({'cliente': row[0]})    


@app.route('/clientes',methods=['POST'])
def create_cliente():
    dat = {
    'id': request.json['id'],
    'nombre': request.json['nombre'],
    'apellido': request.json['apellido'],
    'direccion': request.json['direccion'],
    'codigopostal': request.json['codigopostal']
    }
    ClientesDB.append(dat)
    return jsonify(dat)

@app.route('/facturas',methods=['POST'])
def create_facturas():
    dat = {
    'id': request.json['id'],
    'total': request.json['total'],
    'fecha': request.json['fecha'],
    'cliente': request.json['cliente']
    }
    FacturasDB.append(dat)
    return jsonify(dat)

@app.route('/paquetes',methods=['POST'])
def create_paquetes():
    dat = {
    'id': request.json['id'],
    'nombre': request.json['nombre'],
    'precio': request.json['precio']
    }
    PaquetesDB.append(dat)
    return jsonify(dat)

@app.route('/clientes/<Id>',methods=['DELETE'])
def deleteCliente(Id):
    row = [clientes for clientes in ClientesDB if (clientes['id'] == Id)]
    if len(row) == 0:
       abort(404)
    ClientesDB.remove(row[0])
    return jsonify({'response': 'Success'})

@app.route('/facturas/<Id>',methods=['DELETE'])
def deleteFactura(Id):
    row = [facturas for facturas in FacturasDB if (facturas['id'] == Id)]
    if len(row) == 0:
       abort(404)
    FacturasDB.remove(row[0])
    return jsonify({'response': 'Success'})

@app.route('/paquetes/<Id>',methods=['DELETE'])
def deletePaquete(Id):
    row = [paquetes for paquetes in PaquetesDB if (paquetes['id'] == Id)]
    if len(row) == 0:
       abort(404)
    PaquetesDB.remove(row[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run()


# In[ ]:




