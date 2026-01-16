from energy_mech_master import EnergyMechMaster
from energy_mech_irc import IRCBot
from energy_mech_chat import ChatBot

if __name__ == "__main__":
    master = EnergyMechMaster()
    master.start()

    bot = IRCBot()
    bot.start()

    chat = ChatBot()
    chat.start()