import threading
from core .manager import VKCoinBotManager
threading .current_thread ().name ="Менеджер ботов VKCoinPy"
bot =VKCoinBotManager ()
bot .start ()