import logging

from slixmpp import ClientXMPP

import data_provider


class Bot(ClientXMPP):

    def __init__(self, jid: str, password: str) -> None:

        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler('session_start', self.start_session)
        self.add_event_handler('message', self.message_handler)

    async def start_session(self, event) -> None:
        self.send_presence()
        await self.get_roster()

    def message_handler(self, msg) -> None:
        if msg['type'] in ('chat', 'normal'):
            if 'datos' in msg['body'].casefold():
                msg.reply(f'{data_provider.get_data()}').send()


def start_bot(jid: str, password: str) -> None:

    xmpp_client = Bot(jid,  password)

    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

    xmpp_client.connect((jid.split('@')[1], 5222))
    xmpp_client.process(forever=True, timeout=None)
