# Google Drive Uploader Rei Chikita en Render.com

Antes de comenzar:
Ya el repo tiene el archivo docker, dummy server y el start.sh nuevos creados por Carlos(sin usar el wget)
Bajas este repo y lo subes a GH hazlo privado primero q nada....

Pasos para comenzar xd

1- Vas a tg y creas un canal publico

2- Vas a botfather y creas un bot y copias el token y lo guardas

3- Agrega el bot como admin al canal del primer paso

---------------------
Ahora vamos al repo a editar unas cuantas cosas para q funcione todo ok (hay muchos pasos ya q el creador hizo un enrredo con muchas cosas xd)

1- vas al archivo creds.py 
lo abres y donde dice TG_TOKEN = "" (pones el token del bot ahi entre comillas) y guardas

2- abres client_secrets.json
aca lo q hay q hacer es ir a console.cloud.google.com(usar wireguard o un vpn) para conseguir el client secret con nuestro client_id y client_secret

Antes de continuar, si ya tienes esos datos evita el tutorial y lo q tienes q hacer es ir a:

-https://console.cloud.google.com/apis/credentials y descargas tus credenciales en un json en el boton de descargas con una flechita pa abajo dentro de un circulito xd

- Al descargarse, lo abres y copias su contenido y lo pegas en el archivo client_secrets.json en Github y guardas

- Luego vas a https://console.cloud.google.com/apis/api/drive.googleapis.com/ y habilitas la api de google drive

Listo.....
	
Tutorial por si no tienes nada de eso
https://www.youtube.com/watch?v=sTQkY0UE20c

Desde el minuto minuto 2:39 al 4:40 no sigas de ahi y das en OK y descargas tus credenciales en un json en el boton de descargas con una flechita pa abajo dentro de un circulito xd

- Al descargarse, lo abres y copias su contenido y lo pegas en el archivo client_secrets.json en Github y guardas

- Luego vas a https://console.cloud.google.com/apis/api/drive.googleapis.com/ y habilitas la api de google drive

Listo.....


3- Ahora vamos a app.json 
en repository y website ,pones el link de tu repo dentro de las comillas y guardas

4- Ahora vamos a config.py y haces lo q dicen las notas dentro de las comillas y las notas con #, Ejemplo: 

"aca va tu token con las comillas"

"aca va tu id con las comillas" 

"aca va tu hash con las comillas"

#aca no pongas nada

#aca va el id de tg del administrador del bot y el canal

5- Ahora vas a la carpeta bot/util/
-abres check_channel.py y donde dice "aca pon el nombre de usuario del canal sin @" has eso xd y das guardar #Recuerda siempre pones todo entre comillas

-abres send_join.py y donde dice "link de tu canal con t.me/canalmio" pones el link del canal ahi con t.me y das guardar #Recuerda siempre pones todo entre comillas

Listo

5.1- Ahora para poner tu index link (opcional), vas a la carpeta bot/uploadHandler y abres upload.py 

- vas a la linea 22 "Index link", url= requote_uri(f"https://acapontulinkxd.workers.dev/0:/carpetadearchivos/{_uploadedFile['title']}"))], esa.

- en el link https://acapontulinkxd.workers.dev/0:/carpetadearchivos/ ahi cambialo por el tuyo y la carpeta donde se suben los archvios con un / al final, listo.

6-Ahora vas para la carpeta bot y abres __ init __.py y haces lo siguiente:

-Donde dice en las lineas 35 y 40 Post_url = "aca pones la db de elephantsql" ahi pones la db #la misma

LISTO

7- Ahora ya vamos a editar cosas bobas

-Vamos a la carpeta plugins en el repo y abrimos help.py y donde dice: msg += "Report  @nombredeusuario\n\n" pones tu nombre de usuario(el admin)

-Ahora abres start.py y donde dice:

    url="https://t.me/canal")], Ahi pones el link del canal
    
    url="https://t.me/usuario")] Ahi Pones tu usuario con t.me

LISTO ya ahora vamos a render

creamos el web service, ponemos el name y en Health Check Path pones un / y ya mas nada, empieza a montar el bot(esperas a q finalice y deje abrir la pagina del bot)

luego de creado vas al bot en tg y das /start y escribes /login te dira q entres al link, entras pones tus datos, etc luego te dira q la pagina no es segura, tu marcas el boton de continuar abajo a la izquierda, luego das en continuar, luego te mandara a una pagina vacia copias la url en el navegador sera parecida a esta http://localhost/?code=4/0ARtbsJp6VLAj0HU7Wpegja0w__y8frUuMzZt6LmhGSqo0ARL-KDSvCk02Aiu7BanC4HNYw&scope=https://www.googleapis.com/auth/drive, de aca copias 4/0ARtbsJp6VLAj0HU7Wpegja0w__y8frUuMzZt6LmhGSqo0ARL-KDSvCk02Aiu7BanC4HNYw sin el &scope, y lo pegas en el bot, listo ya estas logeado...

Los comandos son

/start

/help

/login

/logout

..........cualquier duda con Markhz en el rei chikita

Nota: este tutorial lo hice segun lo q fui haciendo y funciono al 100%... si hay otras vias, editen el tutorial si quieren....
