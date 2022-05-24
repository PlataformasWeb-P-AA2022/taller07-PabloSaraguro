from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


archivojug = open("data/datos_jugadores.txt", "r")
registros = archivojug.readlines();

for r in registros:
    nombre = r.split(";")[3]
    dorsal = r.split(";")[2]
    posicion = r.split(";")[1]
    club = session.query(Club).filter_by(nombre= r.split(";")[0]).one()
    
    jugador = Jugador(nombre=nombre,dorsal=dorsal, posicion=posicion, club=club   )
    session.add(jugador)

# se confirma las transacciones
session.commit()





