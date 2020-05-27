# Workshop de Big Data con Apache Spark - Trabajo final por Ezequiel H. Martinez[🇪🇸]

El presente trabajo esta escrito y construido con la intencion de ser los primeros pasos hacia mi trabajo final de especializacion. Nuestra tesis de especializacion trata acerca de la clasificacion de espectrogramas de ondas gravitacionales. Pretendemos trabajar en la preparacion de los datos, el ambiente, y la clasficacion basica del set de entrenamiento a utilizar. Nuestro objetivo principal es entender de que manera podriamos aprovechar las capacidades de Docker, Spark y MLlib para la creacion de la tesis.

## Objetivos

* Preparar el ambiente para el tratamiento de ondas gravitacionales.
* Entrenar al menos un clasificador de ondas gravitacionales con Spark.
* Comprender mejor la estructura de los datos disponibles.

## Tareas realizadas

A continuacion se detallan los pasos que hemos dado para conseguir los objetivos arriba descriptos:

    1. Hemos creado una nueva [imagen Docker](spark/Dockerfile) de spark con todas las librerias necesarias para poder correr los [ejemplos y tutoriales](jupyter/) para entender como trabajar con ondas gravitacionales. 
        > Hemos corrido todos los tutoriales instalados en la carpeta *jupiter*. Los mismos son aquellos notebooks que comienzan con "Tuto x.x". Los mismos funcionan solo bajo el kernel *igwn-py37*.
    2. Hemos downlodeado los [datasets](https://zenodo.org/record/1486046#.XrLYbi-ZMSQ) necesairios y hemos trabajado en la creacion de tres notebooks que realizan:
        * Procesar los datos (3.5Gb) en un formato parquet que sea mas util para su tratamiento en un classificador.
        * Almacenamos los dataframes en formato parquet.
        * Entrenado un clasificador en Spark MLlib e intentado trabajarlo en Pandas (sin exito dado las dimensiones del dataset involucrado).
    Los notebooks cuentan con scripts en Python que realizan el procesamiento *batch* de la informacion. La ejecucion y lectura de los mismos deberia ser en el siguiente ordern:
        1. Abrir el primer notebook [LIGO - Loading of the training dataset](jupyter/notebook/LIGO - Loading of the training dataset.ipynb). El mismo esta escrito en idioma ingles y da una idea de como esta estructurado todo el trabajo. El dataset se limita a solo 569 rows; procesamos todo el dataset en el paso 2.
        2. Ejecutar el script [generate_gw_dataset.py](code/gw/generate_gw_dataset.py); este script generara los archivos parquet con la consolidacion de todos los datos que vamos a necesitar para el trabajo final.
        3. Continuar con el segundo notebook [LIGO - Training classifier to identify Gravitational Waves](jupyter/notebook/LIGO - Training classifier to identify Gravitational Waves.ipynb), donde se intenta preparar el training set y entrenar un modelo de SVC linear. De nuevo, este dataset esta limitado. Procesamos todo el dataset en el paso 4.
        4. Ejecutar el script [training_linearsvc_gw.py](code/gw/training_linearsvc_gw.py). El mismo generara un modelo y lo salvara en disco como parquet.
        5. Ejecutar el script [linear_svc_test.py](code/gw/linearsvc_test.py). El mismo aplicara el modelo entrenado a el set de espectrogramas de test.
        6. Finalmente, en [LIGO - Checking predictions](jupyter/notebook/LIGO - Checking predictions.ipynb) realizamos una tareas "opcional" (pero no menos esencial) de chequeo del modelo. (Establecemos el % de efectividad del modelo mediante la identificacion del area bajo la curva ROC)

    > El trabajo, los comentarios, y practicamente todo el material esta en idioma *ingles*. Se tomo esta decision a sabiendas que el claustro docente maneja el idioma y con la intencion de poder compartir este trabajo de forma internacional con mis contactos en el MIT y CalTech(LIGO).

## Conclusiones

Estos son, solamente, los primeros pasos necesarios como para poder entrenar un modelo capaz de identificar ondas gravitacionales ("Chrips", segun entendemos se los clasifica en el dataset). Un trabajo mas completo deberia intentar optimizar lo mas posible los hiperparametros, manejar adecuadamente la memoria con la que corre Spark y ver si se puede utilizar una libreria como Keras o SVMs no lineales.


