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

archivoclubs = open("data/datos_clubs.txt", "r")
registros = archivoclubs.readlines();
        
for r in registros:
         nombre = r.split(";")[0]
         deporte = r.split(";")[1]
         fundacion = r.split(";")[2].replace("\n","")
         club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
         session.add(club)


# se confirma las transacciones
session.commit()





