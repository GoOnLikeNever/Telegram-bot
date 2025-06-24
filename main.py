#!/usr/bin/env python3
"""
Telegram Article Forwarder Bot
Main entry point for the bot application
"""

import logging
import os
import sys
import time
from config import Config
from bot_handlers import ArticleBot

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('bot.log', mode='a', encoding='utf-8')
        ]
    )
    
    # Reduce telebot library logging level
    logging.getLogger('telebot').setLevel(logging.WARNING)
    
    return logging.getLogger(__name__)

def main():
    """Main function to initialize and run the bot"""
    logger = setup_logging()
    logger.info("Starting Telegram Article Forwarder Bot...")
    
    try:
        # Initialize configuration
        config = Config()
        config.validate()
        
        # Initialize bot
        bot = ArticleBot(config)
        
        logger.info("Bot initialized successfully")
        logger.info(f"Target channel: {config.CHANNEL_USERNAME}")
        logger.info("Bot is running and ready to receive messages...")
        
        # Start bot polling
        bot.start_polling()
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
