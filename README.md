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
Para la extraccion de datos de Facebook primero debemos definir qué datos necesitamos que en este caso serán de juegos en líea qu en este caso serán de las páginas de FIFA de diferentes países como Ecuador, Argentina, Colombia, México y de la página oficial de EA sports y luego se utilizó un script de extracción de datos para realizarlo.

1. Antes de correr el script en python para extraer los datos se debe correr el elasticsearchcon el siguiente comando en el terminal.


![comandoElastic](https://user-images.githubusercontent.com/85883884/133670480-d80e7742-de10-47db-9f66-80eecc6f7e8a.png)

    1.1 Como Elastcsearch no tiene interfaz gráfica se presentará de la siguiente manera.
    
    
![elasticsininterfaz](https://user-images.githubusercontent.com/85883884/133671352-526be8c5-46e6-47e7-a72f-8b49d3037ef1.png)



2. Para que Elasticsearch tenga una interfaz y podamos ver los datos qeu se almacenen necesitaremos de cerebro que se lo ejecuta de la siguiente manera desde la terminal.

![cerebroterminal](https://user-images.githubusercontent.com/85883884/133671898-0dbd2a19-4b09-4995-8486-536250a6d594.png)

3. Luego de ejecutar cerebro, ingresamos en la interfaz de cerebro con las credenciales para trabajar en la nube y se ve de la siguiente manera.

![elasticinterfaz](https://user-images.githubusercontent.com/85883884/133672326-8d86d24f-736f-43d5-9f31-87c7a94f0a93.png)

4. Una vez estando en la interfaz de Elasticsearch con cerebro, con la utilización de los archivos de configuración corremos Logstash por la terminal para de esta manera pasar los datos que se vayan a gregando a las diferentes bases de datos creadas en CouchDB se almacenen en Elastic.


![correrlogstash](https://user-images.githubusercontent.com/85883884/133673872-34521e3c-b37c-449c-b94b-a500f5718d4b.png)

5. A continuación podremos ver ya los índices creados con los datos en Elasticsearch
![datosenelastic](https://user-images.githubusercontent.com/85883884/133688934-5e548da9-5e0b-4574-b52f-153a8881c894.png)



## Extraccion de datos "Twitter"

1.  Para poder recolectar los datos de Twitter usaremos la herramienta de RapidMiner con la cual podremos minar datos. Primero generamos una conexión con nuestra cuenta de Twitter Developer  desde RapidMiner.

![image](https://user-images.githubusercontent.com/66786471/133686752-96b56245-5ca4-49b3-8611-259b4231ad9a.png)
![image](https://user-images.githubusercontent.com/66786471/133686763-4c1cde45-969d-4023-b204-2148455e9101.png)

2.  Ya una vez generada la conexión seleccionamos los operadores Retrieve y Search Twitter para poder establecer la conexión creada junto con lo que deseamos buscar en twitter que en este caso es el pulso político de 20 ciudades del Ecuador. Para poder cosechar los datos ingresaremos en los campos la palabra a buscar y habilitaremos la geolocalización donde nos pide coordenadas de latitud y longitud aparte de un radio de extensión de la ciudad.

![image](https://user-images.githubusercontent.com/66786471/133686919-aced73da-3e49-4934-87ad-0625f6075327.png)
![image](https://user-images.githubusercontent.com/66786471/133686932-c2519ddc-d240-4835-8156-ac00c0e37a91.png)

3. Para poder cosechar de mejor manera los datos crearemos un proceso con 4 buscadores de Twitter donde cada uno llevara una palabra clave diferente.

![image](https://user-images.githubusercontent.com/66786471/133686969-db8bcb0a-8810-4694-a97e-4bfd0cceaa84.png)

4.  Ya una vez listo, seleccionaremos los atributos que deseamos recolectar gracias a un operador como se muestra en la siguiente imagen. 

![image](https://user-images.githubusercontent.com/66786471/133687070-b16818b1-70d4-421f-ab55-a4b2ec32f727.png)

5.  Junto a estos seleccionadores añadiremos un transformador de DATA a JSON con el fin de que los archivos guardados en MongoDB sean JSON para mayor facilidad.

![image](https://user-images.githubusercontent.com/66786471/133687317-9c72f875-1f78-41af-afe1-9343f01ecbee.png)

6.  Ya una vez transformada la información pasamos a crear otra conexión pero esta vez para MongoDB y de igual manera usar el operador Retrive junto Multiply que nos ayudara a crear copias de objetos de RapidMiner y también un operador de escritura en mongo donde ingresaremos cada unos de los JSON convertidos y estableceremos la conexión con la base de datos. 

![image](https://user-images.githubusercontent.com/66786471/133687352-55624e0e-6b15-49a1-a0db-a54a9ee991fa.png)

7.  Una vez realizado este procedimiento con cada una de las coordenadas respectivas a cada ciudad podemos evidenciar la información recolectada en nuestro MongoDB donde tenemos la base de datos Titter_Mongo y la colección Pulso_Politico20 con 402 documentos registrados.

![image](https://user-images.githubusercontent.com/66786471/133687402-519f87fb-0423-4a20-a79c-b390fd35c327.png)

8.  Para poder conectarnos a elasticsearch se intentó con varios métodos desde códigos, hasta transferir la conexión a CouchDB sin embargo el único camino que dio resultado fue importar los datos de Mongo en un archivo CSV  y posterior a ello subirlos a phpMyAdmin.

![image](https://user-images.githubusercontent.com/66786471/133687441-6ccd5122-5235-4e0f-82e8-b7684e06e67d.png)

10. Una vez ya generado el CSV exitosamente se procede a crear la base de datos Twitter2Mongo.

![image](https://user-images.githubusercontent.com/66786471/133687484-13a94d92-c4f9-417e-81e5-1f04a3522ca6.png)
![image](https://user-images.githubusercontent.com/66786471/133687491-09c71857-4dbf-4cec-bc85-9d7bc250e934.png)

11. Ahora para la conexión respectiva con Elasticsearch nos ayudaremos de la herramienta Logstash que nos permite una conexión con la aplicación de Elastic en la nube. Para ello necesitaremos de un archivo de configuración como el siguiente en la carpeta bin de logstash.

![image](https://user-images.githubusercontent.com/66786471/133687564-dd018db7-7855-4c69-8f22-459d7dd11e4c.png)

12. Corremos el logstash y esperamos hasta que la base de datos sea subida correctamente.

![image](https://user-images.githubusercontent.com/66786471/133687628-8567ec94-770e-4548-b298-d12c3a1ec597.png)

13. Ya con los satos en la nube preocedemos a crear un índice para poder realizar un timetable y manejar la tabla en referencia a esto.

![image](https://user-images.githubusercontent.com/66786471/133688024-89d1d70d-f652-4d98-95c0-340aa5844337.png)

14. por ultimo creamos una pizarra donde podremos tener todos los graficos para su analisis como en la imagen siguiente donde podemos ver a un lado izquierdo las palabras mas usadas en los tweets al igual que los mensajes mas retwiteados.

![image](https://user-images.githubusercontent.com/66786471/133688233-a7aa76bd-fc67-47e9-b8c0-4a971d5dac42.png)



## Extracción de datos "Web scraping"
Para la extraccion de datos con Web scraping tenemos que identificar el tema del cual vamos a extraer la información, en nuestro caso fue el porcentaje de población vacunada en diferentes países de Latinoamérica.
1.  Pagina web de donde se extraerán los datos.

![image](https://user-images.githubusercontent.com/65979995/133649835-32b99e81-de43-4bf7-9ef9-cc805c9f86d2.png)

2.  Se utiliza el siguiente codigo para generar los csv

Web ScrapingArgentina.ipynb

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

jdbc.conf

10. Para poder comenzar la subida, nos dirijimos en nuestro terminal a la carpeta que contenga el ejecutable de logstash y el jdbc.conf (usualmente se ponen en la misma carpeta) y ejecutamos el comando "  logstash -f jdbc.conf  " (sin comillas), y posterior a ellos se verifica en elastic la subida de datos

![image](https://user-images.githubusercontent.com/65979995/133654816-2fc0feca-2e35-440a-b511-f5028c2456db.png)

## Almacenamiento de Datos "Kaggle"
Kaggle es un repositorio de datasets donde se pueden encontrar datos listos para usarse de casi cualquier tema, en este caso se encontró un dataset que muestra el videojuego mas popular por país. Este dataset se puede observar en el siguiente link: https://www.kaggle.com/ezgitural/the-most-popular-video-games-in-the-world

El proceso para poblar ElasticSearch con una fuente de datos estática como Kaggle es el siguiente:
1. Se comienza descargando el archivo y pasándolo a formato CSV, este archivo estaba en formato excel por lo que pasarlo a CSV solo requirió guardarlo. Si se tuvieran archivos en formato JSON, el proceso sería más complicado.
2. Eliminar los encabezados de la tabla ya que estos podrían causar problemas al momento de importar el archivo. Los datos se deberían ver así

![image](https://user-images.githubusercontent.com/66144847/133665096-b4b35fac-2f6f-47c7-b401-f8eaaa331a94.png)

3. Se procede a crear una base de datos en postgreSQL, esto se puede hacer con la línea de comandos o con la interfaz PGAdmin, en este caso se usará esta segunda opción. 

![image](https://user-images.githubusercontent.com/66144847/133678548-f74eb975-dfcb-4784-8f6f-34a317cc027c.png)

4. En la base creada, se crea una tabla que tenga el mismo número de columnas y los mismos tipos de datos que el archivo CSV, si en este paso no se han eliminado los encabezados en el archivo CSV, se poducirá un conflicto con el tipo de datos numeric intentando guardar la palabra del encabezado. También convendrá nombrar las columnas de la tabla como estaban nombradas originalmente en el archivo por motivos de orden.

![image](https://user-images.githubusercontent.com/66144847/133678829-cbc9f3d5-217d-43b1-b187-9d371f562d18.png)

5. Teniendo la tabla creada, se puede importar el archivo CSV con una de las opciones del menu que aparece al hacer click derecho en el nombre de la tabla, para importar se debe especificar la ruta completa del archivo, la codificación y el caracter limitador

![image](https://user-images.githubusercontent.com/66144847/133679045-3669568f-4b1c-4639-aad3-a7ebb8910321.png)

6. Si no hay ningún error, se mostrará un mensaje de éxito y se podrán ver los datos en la tabla

![image](https://user-images.githubusercontent.com/66144847/133679120-6475407c-5638-495b-a11d-2301d290c0f8.png)

7. El siguiente paso es subir esta tabla a la nube de ElasticSearch, para esto se utilizará un archivo de configuración en el cual se utiliza el driver JDBC para conectarse con la base de datos utilizando el plugin respectivo, obtener la información y poblar un índice en la nube con dicha información. El plugin de conexión con la base se deberá descargar y, preferiblemente, ubicar en la carpeta bin de logstash junto con el archivo .conf

![image](https://user-images.githubusercontent.com/66144847/133679547-ab36f2cc-cd22-42dc-b1bd-33ededc42834.png)

8. Luego, asegurándose que ElasticSearch y su cliente Cerebro estén en ejecución, se ejecuta logstash con el archivo de configuración

![image](https://user-images.githubusercontent.com/66144847/133679794-675b006a-72ed-4145-a992-0885c115f43f.png)

9. Si no hay ningún error, se mostrará en la terminal la información extraída y terminará el proceso

![image](https://user-images.githubusercontent.com/66144847/133679873-f14a6108-0783-4942-b60c-0f62c6c84022.png)

10. Ahora, si se ingresa a la nube de ElasticSearch, se podrá ver el índice creado; este tambien se podrá consultar con la función search para verificar que la información está ahí.

![image](https://user-images.githubusercontent.com/66144847/133680149-e2a3e372-946f-4c06-a8d6-0c5616e9a08a.png)

![image](https://user-images.githubusercontent.com/66144847/133680163-d53ab272-6edb-4765-957d-3491133938ea.png)

#
# Recopilacion de datos Tiktok
Tiktok es una plataforma en la que los usuarios pueden subir videos publicos de hasta un minuto, en los videos se puede tener audio agregado, menciones, hashtags y trends. Estas caracteristicas de los videos pueden ser utilizados para su recopilación mediante el uso de tik-tok scraper, pasandolos como parametro definido para obtener la información con lo establecido. Y esto puede ser guardado en un archivo CSV.

1. Para la recopilación se utiliza el comando tiktok-scraper con el parametro de hashtag asignando el de noticias para que recopile información de 20 videos con ese hashtag.
![tiktok-scraper](https://user-images.githubusercontent.com/58042139/133685171-19e9c165-bf6d-47a8-bdc7-fb06597ee515.jpg)

2. Una vez se obtenga la información de los videos recopilada se procede a realizar la limpieza con el operador de ReplaceMissingValues de RapidMiner el cual ayuda a remplazar los datos vacios.
![replace missing values](https://user-images.githubusercontent.com/58042139/133685691-6e11739b-d4f9-495d-a739-3798cf3b6980.jpg)

3. Ya con los datos limpios, se procede a importarlos a una base de datos local en MySQL.
![subidamysql](https://user-images.githubusercontent.com/58042139/133685852-8c465d5a-9710-4e76-9544-7453fdb7d737.jpg)
![noticias](https://user-images.githubusercontent.com/58042139/133685886-ce727941-c153-4bfb-81dd-0311abcd27f0.jpg)

4. Con el archivo de configuración de Logstash se sube la información creando un nodo en la nube de Elastic
![logstash2](https://user-images.githubusercontent.com/58042139/133686472-21bac47f-0843-498c-af40-f801e389d92c.jpg)

![elastic](https://user-images.githubusercontent.com/58042139/133686266-e3c603fa-ac4f-45b2-b98f-40edc65e37eb.jpg)

# Parte 2 Explicacion de caso y graficos.
## Facebbok
Aqí se mostrará el proceso para visualizar los datos obtenidos de la extracción de facebook que en este caso son de videojuegos en línea espec+ificamente de FIFA desde páginas administradas por personas de diferentes paises de latinoamérica.

1. Luego de tener ya los datos almacenados en Elasticsearch procedemos a correr Kibana en la nube para poder utilizar estos datos en las visualizaciones empezando por la creación de los índices.
![creacionindex](https://user-images.githubusercontent.com/85883884/133685550-6e94983b-46b1-49e5-8542-17f3500d8780.png)

2. Una vez tengamos creados los índices procedemos a crear los dashboars para que así se muestren las visualizaciones de los diferentes índices que tenemos.
![creaciondashboards](https://user-images.githubusercontent.com/85883884/133685583-705394d9-4b2b-4d36-b19a-7aa5eac40d59.png)

3. Y al final tendremos las visualizaciones de cada uno de los índices.
![visualizaciones1](https://user-images.githubusercontent.com/85883884/133685637-37588cbd-ae8c-4342-b6ff-de36ef6769f7.png)
![visualizaciones2](https://user-images.githubusercontent.com/85883884/133685646-0a656a9e-d242-4120-b49c-f2368919be04.png)
![visualizaciones3](https://user-images.githubusercontent.com/85883884/133685656-5355be0c-bed8-475f-91e9-ec47d660117a.png)

## Twitter
En la primera imagen podemso encontrar lo que serian los teztos de los tweets y donde podemos encontrar las pabras seleccionadas en la consulta como es "listas", "diputas", entre otros dandonos asi como resultado una cosecha de datos exitosa. 
![image](https://user-images.githubusercontent.com/66786471/133692084-8b20d841-8d2e-4fca-8328-be6f5c44fcb7.png)

En la siguiente tabla encontramos el ocntenido de los tweets mas retweeteados por usuarios y vemos que son referentes a las listas de los candidatos presidenciales.
![image](https://user-images.githubusercontent.com/66786471/133692370-ef28983b-afc7-41a5-83f1-0a5079dff2e6.png)


## Web Scraping
### Caso 1 : Proceso de vacunación y administración en diferentes países latinoamericanos.
Tabla y grafica de pais Argentina: El crecimiento constante del proceso de vacunacion en Argentina, se puede considerar como aceptable, debido a que hay que tener en cuenta al nivel poblacional del mismo.

![image](https://user-images.githubusercontent.com/65979995/133667033-3bead1a0-0985-415e-9d51-2013780d7541.png)

![image](https://user-images.githubusercontent.com/65979995/133667234-76a16dad-25e9-4cdb-8637-7e07aff9c3b8.png)

Tabla y grafica de pais Chile: Chile al tener un nivel poblacional similar al de Ecuador, es el pais que ha logrado tener un mayor pocentaje de su poblacion completamente vacunados, esto indica la buena organizacion del gobierno para estas situaciones.

![image](https://user-images.githubusercontent.com/65979995/133667828-251ead5c-ae95-44da-ba40-0e175d7b39ee.png)

![image](https://user-images.githubusercontent.com/65979995/133667882-85cd0cc9-56bc-4751-8900-12935c541b0f.png)

Tabla y grafica de pais Ecuador: Ecuador no muestra tambien un gran porcentaje de ciudadanos completamente vacunados, esto al tener en cuenta que se viene de un proceso de eleccion, nos indica un compromiso inicial del presidente con el país.

![image](https://user-images.githubusercontent.com/65979995/133668188-f22f70d1-ad56-4840-9af9-c77789952a01.png)

![image](https://user-images.githubusercontent.com/65979995/133668208-05ec0209-7ba3-47e7-9e8a-5c77b416d6ea.png)

Tabla y grafica de pais Paraguay: Posiblemente sea uno de los paises con el peor proceso de vacunacion de latinoamerica, esto se puede deber a una falta de organizacion del gobierno para el conseguir insumos medicos.

![image](https://user-images.githubusercontent.com/65979995/133668430-ad2a50ec-b09c-420d-9247-fdab934bed5d.png)

![image](https://user-images.githubusercontent.com/65979995/133668503-54be3baf-1158-4742-8cb2-c7e031c8dc14.png)

Tabla y grafica de pais Perú: Comparado a Argentina, Perú tiene un proceso de vacunacion lento y deficiente, que no permitira que tengan un proceso de vacunacion de forma correcta y les tome mas tiempo inmunisarce.

![image](https://user-images.githubusercontent.com/65979995/133668804-14a112af-a922-4017-b80a-8d5fc8b25caf.png)

![image](https://user-images.githubusercontent.com/65979995/133668837-fc688475-b752-4c4b-9f7b-3223fce46a7e.png)

# INEC

En este caso, de acuerdo a nuestro diseño de arquitectura se utilizará directamente elasticsearch como concentrador de los datos de los archivos csv de INEC.Gracias a que INEC da la posibilidad de bajar archivos csv directamente de su sitio web. 


![imagen](https://user-images.githubusercontent.com/58041267/133682139-5cb091e4-19f4-4ab2-9c67-45fbfde68605.png)


El archivo csv obtenido tiene por nombre, egresos hospitalarios del año 2020 y es justamente con este archivo el que guardaremos como evento en el contenedor elasticsearch en la nube.


![imagen](https://user-images.githubusercontent.com/58041267/133682194-e30f3bee-132a-479b-8789-bead6af6aad8.png)


Como sabemos Logstash es parte del preprocesameinto antes de guardar la información en Elasticsearch, por lo tanto, el proceso básicamente consistió en:

1. Se procede a poner en marcha cerebro con el fin de poder conectarnos con elastic cloud, el cual hemos creado para uso del equipo del proyecto.


![imagen](https://user-images.githubusercontent.com/58041267/133683051-c2013c0e-a6a3-4996-b329-2f1c8e0cf9e5.png)



2. Poner en marcha logstash.


![imagen](https://user-images.githubusercontent.com/58041267/133683102-ebe09887-c5bd-4af8-b095-9ec7fbf0018e.png)

3. Usando Kibana, importar el archivo csv mediante File Data Visualizer que se encuentra en la sección Machine Learning > Visualización de datos


![imagen](https://user-images.githubusercontent.com/58041267/133683186-88bba947-481d-40f2-9e33-0c24134c82e7.png)
![imagen](https://user-images.githubusercontent.com/58041267/133683343-1e252b8b-2a7f-4de1-8054-4849431f49fe.png)
![imagen](https://user-images.githubusercontent.com/58041267/133683379-ee940b84-f52c-4750-a905-c6a90ad199a6.png)

4. Utilizando Discover y Visualizer, realizar la visualización de datos del archivo mediante gráficas.


![imagen](https://user-images.githubusercontent.com/58041267/133683498-96f711e4-6c3b-4514-904a-97d0d7612426.png)
![imagen](https://user-images.githubusercontent.com/58041267/133683548-6071f3ca-457b-41e3-93da-84d4e4acab6a.png)



## Tiktok Scraper
Para realizar las visualizaciones se utiliza Kibana dentro de logstash lo cual permite mediante los datos crear visualizaciones, para ello se puede usar el nodo existente en elastic o cargar manualmente la data.
Una vez se tenga la data se pueden observar los campos que tiene.
![limpieza4](https://user-images.githubusercontent.com/58042139/133687534-ed48b734-0846-49a7-9413-e7a1b25bb978.jpg)

Ya con el archivo cargado con sus campos correspondientes se procede a realizar las visualizaciones.
###
### Caso 1: en este caso se pueden observar el numero de seguidores que tiene cada usuario que subio un video que contenga el hashtag de noticias. Como se puede observar que un usuario sobresale sobre el resto.

![image](https://user-images.githubusercontent.com/58042139/133688467-c6a8ae0b-b180-4f51-b886-132f6eb4370e.png)

### Caso 2: en este caso se utilizo una nube de palabras para visualizar el nombre de usuarios o nicknames de las personas que subieron videos con el hashtag "noticias". En algunos casos se puede observar un identificador unico de usuario para los que no tienen Nickname.

![image](https://user-images.githubusercontent.com/58042139/133688976-81caa0e8-0ca9-4d0d-a620-077444bb86a9.png)

### Caso 3: En este caso se utilizo un diagrama de pastel para ver los porcentajes de los registros de los sonidos utilizados comunmente en los videos. Se puede observar que la mayoria usa audios en comun, mientras que un 25% utiliza sus propios audios en los videos y no añaden contenido musical en común.

![image](https://user-images.githubusercontent.com/58042139/133689427-587d2ec6-de7f-4b9b-87aa-4ae92bbcf5a8.png)

### Caso 4: En este caso se utilizo un diagrama de barras horizontales para analizar el número de comentarios que reciben los titulos de los videos.

![image](https://user-images.githubusercontent.com/58042139/133689724-4f79d45f-83e2-4f31-834a-db36bcdc0b70.png)


## Videojuegos más populares según países (Kaggle)
Basándose en la información obtenida en el dataset sacado de Kaggle, se puede deducir a simple vista cual es el juego más popular en cada país (la tabla literalmente lo dice), pero, al realizar visualizaciones se pueden comparar los campos dados para obtener otros resultados interesantes.
Para realizar visualizaciones se utiliza Kibana, una herramienta que se conecta directamente a ElasticSearch y permite construir todo tipo de gráficos con los índices que están almacenados. Pero antes de que los datos puedan representarse gráficamente, se debe crear un patrón de índice, para esto se despliega el menu en la página principal de Kibana y se selecciona Stack managemente

![image](https://user-images.githubusercontent.com/66144847/133682728-73f7c223-c06b-4d31-ad70-533e78ae46c4.png)

Luego se debe crear un patrón de índice seleccionando el índice de la lista (la misma lista que está en ElasticSearch)

![image](https://user-images.githubusercontent.com/66144847/133682961-601a03f4-4887-4ac9-aff5-d933fbfc9f1f.png)

Se añade el campo timestamp y el índice quedará guardado. Timestamp no es de utilidad en este caso pués los datos son estáticos, pero se lo agrega de todas formas para crear el índice.

![image](https://user-images.githubusercontent.com/66144847/133683136-4d73d2fc-d743-46f8-a7f3-ae30ee9308ec.png)

Hecho esto, se puede volver a la página de inicio y seleccionar dashboard. Se puede crear un dashboard para observar toda las visualizaciones de un índice, si no se ha creado uno, se lo puede hacer con el botón create dashboard. Dentro del dashboard habrá un botón para crear visualizaciones, al seleccionarlo, se abrirá un editor donde se deberá seleccionar el tipo de gráfico, el patrón de índice a utilizar y las columnas del índice para construir el gráfico.

![image](https://user-images.githubusercontent.com/66144847/133683486-9c12bc9d-7948-4ea4-8b3e-5c887887c037.png)

Dependerá de los datos el tipo de gráfico que se pueda hacer, se deberán conocer las columnas y experimentar para averiguar que tipo de gráfico permite visualizar mejor la información.
Para este caso se construyeron dos gráficos:

Este gráfico muestra el juego más popular a nivel mundial, para hallar esto, se agregaron las apariciones de un juego como más popular en varios países y se creó un total que permite concluir que el juego más popular del mundo se ganó ese título ya que una mayoría de países lo consideraron como el más popular dentro de sus países. Por otro lado, el juego menos popular solo fue seleccionado en un solo país.

![image](https://user-images.githubusercontent.com/66144847/133684024-a697e031-ab5d-48f6-bb77-0c77530a4a61.png)

El segundo gráfico permite ver en que coordenadas un juego es popular, el dataset especificaba las coordenadas de los países que eligieron al juego más popular, por ende, si se saca el promedio de todas las coordenadas que eligieron un mismo juego se puede observar el promedio de las coordenadas donde cada juego es jugado, esto se ilustó con un gráfico de barras apiladas

![image](https://user-images.githubusercontent.com/66144847/133684469-bf0cbf2b-31da-458d-b142-c4abf5759ae5.png)

Una vez creados y guardados estos gráficos, se podrá observar como el dashboard los muestra

![image](https://user-images.githubusercontent.com/66144847/133684534-5c8dd0db-5b9f-4ed8-9ab5-fb251c0738eb.png)


