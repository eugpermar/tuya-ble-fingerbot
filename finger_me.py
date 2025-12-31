from pyfingerbot import FingerBot

# Use https://github.com/redphx/tuya-local-key-extractor to get these values
LOCAL_KEY = ''
MAC = ''
UUID = ''
DEV_ID = ''

fingerbot = FingerBot(MAC, LOCAL_KEY, UUID, DEV_ID)
fingerbot.connect()
