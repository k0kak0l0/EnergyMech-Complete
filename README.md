# EnergyMech-Complete
EnergyMech es un sistema de juego basado en IRC (Internet Relay Chat), que simula un entorno virtual donde los usuarios pueden interactuar, atacar, defenderse, completar misiones, unirse a clanes, y tener un sistema de niveles, monedas, inventario y estadísticas.


🚀 EnergyMech Bot IRC - Versión Final 2026

Este bot IRC permite interactuar con usuarios registrados mediante la API de Groq, realizar ataques simulados, y ofrecer ayuda pedagógica en los comandos.
✅ Características

    Sistema de usuarios con registro y login
    Ataques reales (físicos, mágicos, con efectos)
    Conversaciones con la API de Groq
    Ayuda interactiva y pedagógica
    Log de mensajes y usuarios
    Optimizado y escalable
    Economía virtual
    Niveles de usuarios
    Estadísticas de ataque y defensa
    Inventario con armas y armaduras
    Habilidades únicas por nivel
    Monedas para comprar habilidades
    Misiones y recompensas
    Clanes y equipos
    Ataques en grupo

## 📌 Comandos Disponibles
	Conéctate a un servidor IRC (ejemplo: irc.libera.chat) y usa los comandos.

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
📌 Instalación en Linux

    1. Instalar dependencias:

sudo apt update
sudo apt install python3 python3-pip

    2. Clonar el repositorio:

git clone https://github.com/EnergyMech/energymech.git
cd energymech

    3. Crear carpeta y mover archivos:

mkdir energy-mech-irc
mv * energy-mech-irc/
cd energy-mech-irc

    4. Instalar dependencias:

pip3 install -r requirements.txt

    5. Ejecutar el bot:

python3 main.py

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
