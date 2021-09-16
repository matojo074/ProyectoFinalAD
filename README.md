# Proyecto Final Analisis de Datos

Integrantes:
- Mateo Borja
- Stiven López 
- Diana Almeida
- Christian Soledispa
- Mateo Cevallos
- Josué Singaña

# Parte 1: Extracción y Almacenamiento de Datos

## Extracción de datos "Facebook"


## Extraccion de datos "Twitter"


## Extracción de datos "Web scraping"
Para la extraccion de datos con Web scraping tenemos que identificar el tema del cual vamos a extraer la información, en nuestro caso fue el porcentaje de población vacunada en diferentes países de Latinoamérica.
1.  Pagina web de donde se extraerán los datos.

![image](https://user-images.githubusercontent.com/65979995/133649835-32b99e81-de43-4bf7-9ef9-cc805c9f86d2.png)

2.  Se utiliza el siguiente codigo para generar los csv

https://github.com/matojo074/ProyectoFinalAD/blob/a2c7e7fdcd6f88c369a76186978de1ebe18a818d/Web%20Scraping/Web%20Scraping%20Argentina.ipynb

3.  Creamos la bse de datos en sql para la subida de datos

![image](https://user-images.githubusercontent.com/65979995/133650733-0117ca87-8e7f-4dc0-b932-58066c13c709.png)

4.  Acedemos a la configuracion de subida de archivo

![image](https://user-images.githubusercontent.com/65979995/133651033-1af3406b-7368-45f1-8979-9f53a1375bea.png)

5. Importamos los CSV y damos next hasta que se suban

![image](https://user-images.githubusercontent.com/65979995/133651171-41c5a56a-3fa6-4085-8253-d39e8b4849bb.png)

Nota: en caso que se vea necesario, sql nos permite cambiar las variables.

![image](https://user-images.githubusercontent.com/65979995/133651338-b3eddc62-de13-437c-ae83-f8dd641a6733.png)

6.  Para evitar errores, se transferiran los datos de SQL Server a MySQL, para ello se utilizo MySQL Workbench que facilita la tranferencia sin errores y datos limpios sin afectacion, primero entramos MySQL y vamos a database.

![image](https://user-images.githubusercontent.com/65979995/133652770-f4987c70-204f-47f4-b39d-2170a6899089.png)

7. Damos clic en ODBC administrator, una vez dentro creamos el odcb para la coneccion con SQL server, los campos que vienen por defecto se los deja y se da next

![image](https://user-images.githubusercontent.com/65979995/133652945-9a6fa400-2e65-46f9-8723-967256893d3b.png)

![image](https://user-images.githubusercontent.com/65979995/133653024-28125aee-2c3a-4c87-a0eb-3764b1ebd7b0.png)

![image](https://user-images.githubusercontent.com/65979995/133653076-e5d55dd6-0ab2-4462-8ac2-a09ca8d1cea9.png)

8. Nos dirijimos a start migration, en esta seccion solo es de configurar las secciones que se presentan a continuacion.

![image](https://user-images.githubusercontent.com/65979995/133653824-e4e94c1e-79af-4bd1-b462-0953cf8c9edc.png)

![image](https://user-images.githubusercontent.com/65979995/133653873-12b6e2dc-ee2f-4ca7-81e5-c04cdb1323da.png)

![image](https://user-images.githubusercontent.com/65979995/133654125-dd9e1573-edcf-4081-a851-dcc9bcaac97f.png)

Nota: para mejorar la configuracion y como opcional, es la seccion que se presenta se puede cambiar las variables de cada dato de la tabla.

![image](https://user-images.githubusercontent.com/65979995/133654225-dfc9db03-3515-4ed5-8455-fb469559b715.png)

9. Se procede a subir al logstash, para este paso se creo un jdbc del cual se fue modificando en cada subida de datos, para poder subir los datos de todas las tablas.

https://github.com/matojo074/ProyectoFinalAD/blob/4356db33aeb1dbdf3c4e95940dcf015c067abb5d/Web%20Scraping/jdbc.conf

10. Para poder comenzar la subida, nos dirijimos en nuestro terminal a la carpeta que contenga el ejecutable de logstash y el jdbc.conf (usualmente se ponen en la misma carpeta) y ejecutamos el comando "  logstash -f jdbc.conf  " (sin comillas), y posterior a ellos se verifica en elastic la subida de datos

![image](https://user-images.githubusercontent.com/65979995/133654816-2fc0feca-2e35-440a-b511-f5028c2456db.png)

## Almacenamiento de Datos "Kaggle"
Kaggle es un repositorio de datasets donde se pueden encontrar datos listos para usarse de casi cualquier tema, en este caso se encontró un dataset que muestra el videojuego mas popular por país. Este dataset se puede observar en el siguiente link: https://www.kaggle.com/ezgitural/the-most-popular-video-games-in-the-world

El proceso para poblar ElasticSearch con una fuente de datos estática como Kaggle es el siguiente:
1. Se comienza descargando el archivo y pasándolo a formato CSV, este archivo estaba en formato excel por lo que pasarlo a CSV solo requirió guardarlo. Si se tuvieran archivos en formato JSON, el proceso sería más complicado.
2. Eliminar los encabezados de la tabla ya que estos podrían causar problemas al momento de importar el archivo. Los datos se deberían ver así

![image](https://user-images.githubusercontent.com/66144847/133665096-b4b35fac-2f6f-47c7-b401-f8eaaa331a94.png)



# Parte 2 Explicacion de caso y graficos.



# INEC 
En este caso, de acuerdo a nuestro diseño de arquitectura se utilizará directamente elasticsearch como concentrador de los datos de los archivos csv de INEC.Gracias a que INEC da la posibilidad de bajar archivos csv directamente de su sitio web.
![imagen](https://user-images.githubusercontent.com/58041267/133668850-73540f3b-97da-42d4-971d-c6da920c46e7.png)


El archivo csv obtenido tiene por nombre, egresos hospitalarios del año 2020  y es justamente con este archivo el que guardaremos como evento en el contenedor elasticsearch en la nube.
![imagen](https://user-images.githubusercontent.com/58041267/133667563-b579e19d-bcac-417a-8eee-9cb08bd9341e.png)


Como sabemos Logstash es parte del preprocesameinto antes de guardar la información en Elasticsearch, por lo tanto, el proceso básicamente consistió en: 
1. Se procede a poner en marcha cerebro con el fin de poder conectarnos con elastic cloud, el cual hemos creado para uso del equipo del proyecto. 
2. Poner en marcha logstash.
3. Usando Kibana, importar el archivo csv mediante File Data Visualizer que se encuentra en la sección Machine Learning > Visualización de datos.
4. Utilizando Discover y Visualizer, realizar la visualización de datos del archivo mediante gráficas.
