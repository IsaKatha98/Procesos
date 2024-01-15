from app import *
 #importamos la variable de tipo Flask encargada de levantar el servicio

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6060)