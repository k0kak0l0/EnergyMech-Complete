import irc.client
import threading
from energy_mech_master import EnergyMechMaster
from data import users, stats, logs, inventory, missions, clans, group_attacks

class IRCBot:
    def __init__(self):
        self.master = EnergyMechMaster()
        self.irc = irc.client.IRC()
        self.server = "irc.libera.chat"
        self.port = 6697
        self.nickname = "EnergyMech"
        self.channel = "#energymech"
        self.connection = None
        self.connection_thread = None

    def start(self):
        self.connection_thread = threading.Thread(target=self._start_connection)
        self.connection_thread.start()

    def _start_connection(self):
        self.connection = self.irc.IRC()
        self.connection.connect(self.server, self.port, self.nickname)
        self.connection.process_forever()

    def on_connect(self, connection, event):
        connection.join(self.channel)

    def on_pubmsg(self, connection, event):
        self.handle_message(event)

    def handle_message(self, event):
        message = event.arguments[0]
        nick = event.source.nick
        channel = event.target
        self.master._log(f"{nick} ({channel}): {message}")

        if message.startswith("!register "):
            self._register(nick, message.split(" ")[1], channel)
        elif message.startswith("!login "):
            self._login(nick, message.split(" ")[1], channel)
        elif message.startswith("!attack "):
            self._attack(nick, message.split(" ")[1], channel)
        elif message.startswith("!defend"):
            self._defend(nick, channel)
        elif message.startswith("!chat"):
            self._chat(nick, channel)
        elif message.startswith("!help"):
            self._help(nick, channel)
        elif message.startswith("!stats"):
            self._stats(nick, channel)
        elif message.startswith("!logs"):
            self._logs(nick, channel)
        elif message.startswith("!level"):
            self._level(nick, channel)
        elif message.startswith("!coins"):
            self._coins(nick, channel)
        elif message.startswith("!inventory"):
            self._inventory(nick, channel)
        elif message.startswith("!upgrade"):
            self._upgrade(nick, channel)
        elif message.startswith("!mission"):
            self._mission(nick, channel)
        elif message.startswith("!clan"):
            self._clan(nick, channel)
        elif message.startswith("!group_attack "):
            self._group_attack(nick, message.split(" ")[1], channel)