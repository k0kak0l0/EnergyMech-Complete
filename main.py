#!/usr/bin/env python3
"""
EnergyMech2026 v.1.0 COMBO Release
Bot de IRC mejorado con sistema de juego RPG e IA
"""

import threading
import logging
from bot_irc import EnergyMechBot
from game_system import GameSystem
from ai_image_generator import AIImageGenerator
import signal
import sys

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data/logs/sistema.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class EnergyMech2026:
    def __init__(self):
        self.game_system = GameSystem()
        self.ai_generator = AIImageGenerator()
        self.irc_bot = None
        self.running = True
        
    def start(self):
        """Inicia todos los sistemas del bot"""
        logger.info("🚀 Iniciando EnergyMech2026 v.1.0 COMBO Release")
        
        # Iniciar generador de imágenes IA
        if self.ai_generator.initialize():
            logger.info("✅ Generador de imágenes IA inicializado")
        else:
            logger.warning("⚠️  Generador de imágenes IA no disponible")
        
        # Iniciar sistema de juego
        self.game_system.load_all_data()
        logger.info("✅ Sistema de juego cargado")
        
        # Iniciar bot de IRC
        self.irc_bot = EnergyMechBot(
            game_system=self.game_system,
            ai_generator=self.ai_generator
        )
        
        # Configurar señal de terminación
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        
        # Iniciar en hilo separado
        bot_thread = threading.Thread(target=self.irc_bot.start)
        bot_thread.daemon = True
        bot_thread.start()
        
        logger.info("✅ Bot de IRC iniciado. Conectando...")
        
        # Mantener el programa en ejecución
        try:
            while self.running and bot_thread.is_alive():
                bot_thread.join(1)
        except KeyboardInterrupt:
            self.shutdown(None, None)
    
    def shutdown(self, signum, frame):
        """Apagado controlado del sistema"""
        logger.info("🔻 Apagando EnergyMech2026...")
        self.running = False
        if self.irc_bot:
            self.irc_bot.stop()
        sys.exit(0)

if __name__ == "__main__":
    bot = EnergyMech2026()
    bot.start()
