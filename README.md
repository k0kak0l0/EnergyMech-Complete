🎮 EnergyMech2026 v.1.0 COMBO Release - Bot de IRC Mejorado

Sistema completo con bot de IRC y características de juego RPG, generación de imágenes IA y funcionalidades mejoradas.

📁 Estructura del Proyecto Final
text
EnergyMech2026//
├── main.py 
├── bot_irc.py
├── game_system.py
├── ai_image_generator.py
├── network_utils.py
├── config//
│   ├── settings.json
│   └── characters.json
├── data//
│   ├── users//
│   │   └── perfiles.json
│   ├── clans//
│   │   └── clanes.json
│   ├── items//
│   │   ├── weapons.json
│   │   ├── armors.json
│   │   └── currencies.json
│   ├── game//
│   │   ├── levels.json
│   │   └── skills.json
│   └── logs//
│       └── sistema.log
├── assets//
│   ├── characters//
│   ├── clan_badges//
│   ├── items//
│   └── backgrounds//
├── requirements.txt
└── README.md


## ✅ Descripción

🚀 Características Mejoradas del Sistema
Nuevas Funcionalidades:

Sistema de Clanes Completo: Creación, gestión y batallas entre clanes

Generación de Imágenes IA: Integración con OpenAI DALL-E/Stable Diffusion

Economía del Juego: Monedas, tienda, comercio entre jugadores

Sistema de Niveles: 100 niveles con recompensas progresivas

PVP Mejorado: Ataques, duelos y sistema de recompensas

Inventario Avanzado: Armas, armaduras y objetos especiales

Logs y Estadísticas: Seguimiento completo de todas las acciones

Sistema de Administración: Herramientas para moderadores

Seguridad Mejorada:
Protección contra flood y spam

Sistema de baneo con registro

Verificación de comandos administrativos

Logs detallados de todas las acciones

Optimizaciones:
Código modular y escalable

Sistema de archivos JSON para persistencia

Hilos separados para operaciones lentas

Cache de imágenes generadas

📋 Instalación y Uso
bash
# 1. Clonar el repositorio
git clone https://github.com/EnergyMech/energymech.git EnergyMech2026
cd EnergyMech2026

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar API keys
cp config/ai_settings.example.json config/ai_settings.json
# Editar el archivo con tus API keys

# 4. Crear directorios necesarios
mkdir -p data/users data/clans data/logs assets/characters

# 5. Iniciar el bot
python main.py
⚠️ IMPORTANTE: Consideraciones Éticas y Legales
Los ataques de red reales son ILEGALES sin autorización expresa

El sistema de escaneo incluido es SOLO DEMOSTRATIVO

Siempre obtener permiso antes de escanear cualquier red

Este bot es para USO EDUCATIVO Y DE APRENDIZAJE únicamente

Respetar las políticas de los servidores de IRC

No usar para actividades maliciosas

🔧 Personalización
Puedes modificar fácilmente:

Personajes en config/characters.json

Configuración del IRC en config/settings.json

Sistema económico en game_system.py

Comandos disponibles en bot_irc.py
