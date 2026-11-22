import logging
from core .locale import _
from core .logger import Logger
from .import config ,wallet ,networking
class VKCoinBot (object ):
    def __init__ (self ,server_url ,bot_config =None )->None :
        self .server_url =server_url
        self .logger =logging .getLogger (__file__ )
        self .config =config .BotConfig (bot_config )
        self .wallet =wallet .BotWallet ()
        self .messenger =None
        self .running =False
    @property
    def is_connected (self ):
        return self .messenger and self .messenger .connected
    async def run (self )->None :
        Logger .log_system (_ ("Сеанс бота VKCoinPy начинается"))
        Logger .log_system (_ ("Подключение к серверу приложений VK Coin"))
        reconnect =1
        while reconnect :
            self .messenger =networking .BotMessenger (self .server_url ,self )
            reconnect =await self .messenger .run ()