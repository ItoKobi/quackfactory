from discord import Intents

def get_intents() -> Intents:
  intents = Intents.all()
  intents.reactions = True
  intents.members = True
  return intents

LOG_FILENAME = 'quack.log'
TOKEN = ''
