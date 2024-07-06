
[![Licencia](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)

# Usuarios Streaming

Este proyecto trata de obtener datos de usuarios en streaming para despues procesarlos y almacenarlos en una base de datos. 

## Tabla de Contenidos
- [Funcionalidades Principales](#funcionalidades-principales)
- [Diagrama del proyecto](#diagrama-del-proyecto)
- [Instrucciones de Uso](#instrucciones-de-uso)
  - [Prerequisitos](#prerequisitos)
  - [Instalación](#instalación)
  - [Tests](#tests)
- [Tecnologías Utilizadas](#tecnologias-utilizadas)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Funcionalidades Principales

- **Generacion de usuarios:** Permite generar usuarios en streaming de manera constante mediante Kafka. 

- **Procesamiento y almacenamiento de datos:** Permite procesar los datos de los usuarios en real time con Spark y almacenarlos para conservar su informacion en Postgres.

## Diagrama del proyecto

![Diagrama](./diagrama/diagrama.png)

## Instrucciones de Uso

### Prerequisitos

Antes de comenzar, asegúrate de tener instalado Docker en tu máquina. Puedes descargarlo [aquí](https://www.docker.com/get-started).

### Instalación

Para ejecutar la aplicación con Docker:

1. Clona este repositorio con el siguiente comando:

    ```bash
    git clone https://github.com/nachodorado98/Usuarios-Kafka-Spark.git
    ```

2. Navega al directorio del proyecto.

3. Ejecuta el siguiente comando para construir y levantar los contenedores:

    ```bash
    docker-compose up -d
    ```

4. **DAG STREAM DATA**
Inicia el DAG Equipos en la interfaz de Apache Airflow para generar los usuarios en streaming con Kafka: `http://localhost:8080`.

Este DAG genera durante un minuto los usuarios simulando un sistema de registro de usuraios. Esta planificado para ejecutarse de manera diaria pero se puede modificar e incluso ejeuctar de manera manual.

5. Dentro del contenedor del servicio `spark-master`, cambia al directorio del script para ejecutar la aplicacion de Spark:

    ```bash
    cd /opt/spark/nacho/scripts
    ```

6. Ejecuta el siguiente comando para ejecutar la aplicacion en streaming de Spark:

    ```bash
    spark-submit --packages "org.postgresql:postgresql:42.2.23,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0" ./spark_script.py
    ```

### Tests

Para ejecutar los tests de la generacion de usuarios con Kafka:

1. Asegúrate de que los contenedores estén en funcionamiento. Si aún no has iniciado los contenedores, utiliza el siguiente comando:

    ```bash
    docker-compose up -d
    ```

2. Dentro del contenedor del servicio `scheduler`, cambia al directorio de los tests:

    ```bash
    cd dags/python/tests
    ```

3. Ejecuta el siguiente comando para ejecutar los tests utilizando pytest:

    ```bash
    pytest
    ```

Este comando ejecutará todas las pruebas en el directorio `tests` y mostrará los resultados en la consola.

## Tecnologías Utilizadas

- [![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
- [![airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](https://airflow.apache.org/)
- [![spark](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)](https://spark.apache.org/)
- [![kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
- [![postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
- [![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


## Licencia

Este proyecto está bajo la licencia MIT. Para mas informacion ver `LICENSE.txt`.
## 🔗 Contacto
[![portfolio](https://img.shields.io/badge/proyecto-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/nachodorado98/Usuarios-Kafka-Spark.git)

[![email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:natxo98@gmail.com)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nacho-dorado-ruiz-339209237/)
