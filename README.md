# xmpp-bot-example

Ejemplo de un bot XMPP que devuelve datos del covid referidos a Euskadi.

## Setup

Instalar librería slixmpp (soporte de XMPP en python)

`pip3 install slixmpp`

Instalar servidor XMPP ejabberd

`sudo apt install ejabberd`

Registrar el JID del bot en el servidor XMPP ejabberd

`sudo ejabberdctl register data-bot <vhost> <contraseña>`



