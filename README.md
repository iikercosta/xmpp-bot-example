# xmpp-bot-example

Ejemplo de un bot XMPP que devuelve datos del Covid-19 referidos a Euskadi.

El evento que activa la comunicación de los datos es un mensaje de otro cliente XMPP
que contenga la palabra "datos".

## Setup

Instalar librería slixmpp (soporte de XMPP en python)

`pip3 install slixmpp`

Instalar servidor XMPP ejabberd

`sudo apt install ejabberd`

Registrar el JID del bot en el servidor XMPP ejabberd

`sudo ejabberdctl register data-bot <vhost> <contraseña>`





