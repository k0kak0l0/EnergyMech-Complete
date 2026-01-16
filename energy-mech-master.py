import json
import random
import threading
import time
from data import users, stats, logs, inventory, missions, clans, group_attacks

class EnergyMechMaster:
    def __init__(self):
        self.users = users.load_users()
        self.stats = stats.load_stats()
        self.logs = logs.load_logs()
        self.inventory = inventory.load_inventory()
        self.missions = missions.load_missions()
        self.clans = clans.load_clans()
        self.group_attacks = group_attacks.load_group_attacks()

    def start(self):
        self._start_threads()

    def _start_threads(self):
        # Hilo para manejar misiones
        threading.Thread(target=self._manage_missions).start()

        # Hilo para manejar clanes
        threading.Thread(target=self._manage_clans).start()

        # Hilo para manejar ataques en grupo
        threading.Thread(target=self._manage_group_attacks).start()

    def _manage_missions(self):
        while True:
            time.sleep(60)
            for user in self.users:
                if user["missions"]:
                    mission = random.choice(self.missions)
                    user["missions"].append(mission)
                    self._log(f"{user['name']} ha recibido la misión: {mission}")

    def _manage_clans(self):
        while True:
            time.sleep(300)
            for user in self.users:
                if user["clan"] == "Sin clan":
                    self._log(f"{user['name']} no está en ningún clan")

    def _manage_group_attacks(self):
        while True:
            time.sleep(10)
            for user in self.users:
                if user["group_attack"]:
                    self._log(f"{user['name']} está en un ataque en grupo")

    def _log(self, message):
        self.logs.append({
            "message": message,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        logs.save_logs(self.logs)

    def _save_users(self):
        users.save_users(self.users)

    def _save_stats(self):
        stats.save_stats(self.stats)

    def _save_logs(self):
        logs.save_logs(self.logs)

    def _save_inventory(self):
        inventory.save_inventory(self.inventory)

    def _save_missions(self):
        missions.save_missions(self.missions)

    def _save_clans(self):
        clans.save_clans(self.clans)

    def _save_group_attacks(self):
        group_attacks.save_group_attacks(self.group_attacks)