# POSTGRES
BBDD="bbdd_usuarios"
TABLA="usuarios"
HOST="postgres"
USUARIO="airflow"
CONTRASENA="airflow"
PUERTO=5432
JDBC_URL=f"jdbc:postgresql://{HOST}:{PUERTO}/{BBDD}"
PROPIEDADES={"user":USUARIO, "password":CONTRASENA, "driver":"org.postgresql.Driver"}

# KAFKA
HOST_KAFKA="kafka"
PUERTO_KAFKA="19092"
SERVIDOR_KAFKA=f"{HOST_KAFKA}:{PUERTO_KAFKA}"
TOPIC="usuarios"