# Mask-RCNN-Instance-Segmentation
An implementation of Instance Segmentation using Keras, Tensorflow and data from Berkeley Deep Drive.

# Datasets

La carpeta contiene:

●	Ejemplo de dataset creado con VIA 
●	Ejemplo de dataset creado con BDD
●	Script para crear datasets a partir de BDD

________________________________________
Hacer dataset con VIA:

1.	Seleccionar Load images y seleccionar las imágenes a etiquetar
2.	Utilizar la Region shape del tipo polygon y delimitar los objetos de interes de la imagen
3.	 En la seccion Region data de la imagen, llamar a la primera columna 
"name" y comenzar a asignar las categorias a los objetos de interés. Repetir por cada imagen del set de datos.  
![](https://i.imgur.com/cTlFY97.png)

4.	Una vez terminado, ir a Annotation -> Save as JSON y descargar las anotaciones. Guardar el archivo via_region_data.json en la misma carpeta que las imagenes correspondientes.

*Es posible también editar un archivo via_region_data.json ya existente, para añadir/quitar/editar imagenes u etiquetas, seleccionando Annotation -> Import entre el paso 1 y 2 y subiendo el .json a editar.

 
________________________________________
Hacer dataset con BDD+Script:

1.	Descargar de la página de BDD (requiere hacer una cuenta) los archivos de Images y Labels  
![](https://i.imgur.com/K35eI0p.png)


2.	Crear una carpeta donde se extraen las imágenes de Images y su archivo de etiquetas correspondiente. (Utilizar las etiquetas de train/valid con las imagenes en la carpeta 100k de train/valid del archivo comprimido) 
3.	Descargar y colocar el archivo dataset_creator.py en la carpeta madre de la que contiene las imagenes + etiquetas. Abrir el archivo .py y editar los parámetros necesarios al inicio del archivo. La seccion a editar es la siguiente: 
	![](https://i.imgur.com/7Mrd0Rb.png)

5.	Correr el archivo. Se habrá creado en la carpeta que contiene el script otra con el set de datos con el formato adecuado bajo el nombre "train" o "valid".
 
 
Formato del archivo .zip

 El jupyter notebook que se corre en colaboratory inicialmente descomprime un archivo con el set de datos. Este archivo tiene extensión .zip y contiene el siguiente formato:
 
images.zip
"images" directory
****|- "train" directory
******|- jpg image files of training data
******|- "via_region_data.json" annotations file of training data
****|- "val" directory
******|- jpg image files of validation data
******|- "via_region_data.json" annotations file of validation data

Donde `train` y `val` directory son carpetas creadas con cualquiera de los dos métodos anteriores. Esta carpeta se crea localmente y luego se sube a Drive, donde se debe permitir compartir via link. El resto del trabajo se hace desde el jupyter notebook en model.

# Model

La carpeta contiene:

●	Ejemplo de entrenamiento con dataset VIA 
●	Ejemplo de entrenamiento con dataset BDD

Ambos notebooks funcionan igual, pero se agregan para poder ver como varían las partes que debe editar el usuario para entrenar su propio modelo. Cada celda viene con su propia explicación. 

Es clave correr los notebooks con GPU, desde la opción Runtime -> Change Runtime Type -> GPU en Hardware accelerator.

Ocasionalmente aparecerá en colaboratory un mensaje de advertencia acerca de la memoria disponible. Se selecciona Ignorar y se sigue con la ejecución de celdas de manera normal.
![](https://i.imgur.com/WO0VOTN.png)