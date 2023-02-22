
## CRM Django With React.js 
Sistema de información para la gestión, atención y servicio al cliente; para el seguimiento y entrega de medicamentos según ordenes médicas.



## Page demo

## Getting started
Proyecto Users
Este proyecto consiste en una API creada con Django y Django Rest framework que permite realizar un login de usuarios y obtener una lista de usuarios registrados en una base de datos SQLite. También cuenta con un frontend creado con React y Mui-Material que consume la API para mostrar la lista de usuarios y realizar el login.

Configuracion del BackEnd en Django y el FrontEnd en React.Js
-[Clonar el repositorio BackEnd: git clone](https://github.com/CalicheDev/Proyectos_Django.git).
-[Clonar el repositorio FrontEnd: git clone](https://github.com/CalicheDev/Proyectos_Django_React.git).
-Crear un entorno virtual e instalar las dependencias de Django: pip install -r requirements.txt.
-Configurar la base de datos SQLite en el archivo settings.py de Django.
-Migrar las tablas a la base de datos: python manage.py migrate.
-Crear un superusuario de Django: python manage.py createsuperuser.
-Correr el servidor de Django: python manage.py runserver.
-En otra terminal, moverse a la carpeta frontend y ejecutar npm install para instalar las dependencias de React.
-Ejecutar npm start para iniciar el servidor de desarrollo de React.
-Instalar la libreria axios para poder conectarse a la base de datos y al backend Dejango
-Instalar la libreria la biblioteca js-cookie para almacenar y recuperar un valor en una cookie en este caso el inicio de sesion
-Instalar la libreria la libreria 'jsonwebtoken' npm install jsonwebtoken. Se puede importar de dos formas: import jwt from 'jsonwebtoken'; o const jwt = require('jsonwebtoken')
-Instalar la libreria la libreria 'buffer' npm install buffer. Buffer es una API que viene incluida en Node.js para utilizarla en una aplicación de React en el navegador



## Biblioteca js-cookie
1. Instala la biblioteca js-cookie utilizando npm o yarn:
npm install js-cookie
yarn add js-cookie

2. En el componente donde quieras utilizar cookies, importa la biblioteca:
import Cookies from 'js-cookie';

3. Para establecer una cookie, puedes utilizar el siguiente código:
Cookies.set('cookie_name', 'cookie_value');

4. Para recuperar el valor de una cookie, puedes utilizar el siguiente código:
const cookieValue = Cookies.get('cookie_name');

5. Para eliminar una cookie, puedes utilizar el siguiente código:
Cookies.remove('cookie_name');


API
La API cuenta con dos endpoints:

/api/user_api/
Este endpoint devuelve una lista de usuarios registrados en la base de datos en formato JSON. Solo es posible acceder a este endpoint si se ha iniciado sesión en la API.

GET
Devuelve una lista de usuarios en formato JSON.

'api_generate_token/'
Este endpoint permite realizar el login de usuarios.

POST
Realiza el login de un usuario y devuelve un token de autenticación en formato JSON.

Parámetros
|Nombre	    |Tipo	    |Descripción                                        |
|-----------|-----------|---------------------------------------------------|
|username	|string	    |Obligatorio. El nombre de usuario del usuario.     |
|password	|string	    |Obligatorio. La contraseña del usuario.            |


Frontend
El frontend se ha creado con React y Material-UI. Cuenta con dos componentes principales:

UserCard.js
Este componente muestra un card con la información de un usuario.

PacientesList.js
Este componente muestra una lista de pacientes en un Grid con varias columnas.

LoginForm.js
Este componente permite realizar el login de un usuario utilizando la API de Django.

## License

## Contact us

Email Us: cabejarano21@gmail.com