# EnergyMech - Sistema de Juego en IRC

## ✅ Descripción

EnergyMech es un sistema de juego completo que simula un entorno virtual en IRC. Permite a los usuarios:

- Registrar y loguearse.
- Atacar y defenderse.
- Completar misiones.
- Unirse a clanes.
- Usar la API de Groq para conversar.
- Subir de nivel y mejorar habilidades.
- Tener un inventario y monedas.
- Ver estadísticas y logs.

## 🚀 Instalación

1. Instala Python 3 y pip:
sudo apt update sudo apt install python3 python3-pip


2. Clona el repositorio:

git clone https://github.com/EnergyMech-Complete.git cd EnergyMech-Complete


3. Instala dependencias:

pip install -r requirements.txt


4. Ejecuta el sistema:

python3 main.py


5. Conéctate a un servidor IRC (ejemplo: irc.libera.chat) y usa los comandos.

## 📌 Comandos Disponibles

- `!register <nombre>` - Registrar un nuevo usuario.
- `!login <nombre>` - Iniciar sesión.
- `!attack <usuario>` - Atacar a otro usuario.
- `!defend` - Defenderse de un ataque.
- `!chat` - Conversar usando la API de Groq.
- `!help` - Mostrar esta ayuda.
- `!stats` - Mostrar estadísticas.
- `!logs` - Mostrar logs.
- `!level` - Mostrar nivel.
- `!coins` - Mostrar monedas.
- `!inventory` - Mostrar inventario.
- `!upgrade` - Subir nivel.
- `!mission` - Ver misiones.
- `!clan` - Unirse a un clan.
- `!group_attack <usuario>` - Ataque en grupo.

## 🧾 Licencia

Este proyecto se distribuye bajo la licencia MIT.

## 📌 Nota

¡Este sistema está listo para usar y funciona en tu sistema! Puedes personalizarlo según tus necesidades.
-----------------------------------------------------------------------------------------------------------------
📌 Explicación de Conceptos Clave
🛡️ Inventario con armas y armaduras

El inventario permite que los usuarios lleven armas y armaduras, lo que afecta el daño y la defensa. Por ejemplo, un usuario puede tener una espada que aumenta su daño físico o una armadura que reduce el daño recibido.
🔥 Habilidades únicas por nivel

Cada nivel te da una habilidad nueva, como "Defensa reflejada" o "Ataque crítico". Estas habilidades pueden mejorar tu rendimiento en combate.
💰 Monedas para comprar habilidades

Las monedas son la moneda virtual del juego. Puedes usarlas para mejorar habilidades o comprar armas.
🎯 Misiones y recompensas

Las misiones son tareas que puedes completar para ganar recompensas, como monedas o habilidades.
🤝 Clanes y equipos

Puedes unirte a un clan para jugar en equipo y tener beneficios adicionales.
🧑‍🤝‍🧑 Ataques en grupo

Los ataques en grupo permiten que múltiples usuarios ataquen juntos a un objetivo, lo que aumenta el daño y la efectividad de los ataques.
