import os

BOT_TOKEN = os.environ.get("5990439424:AAHFCbdr3nWyizVc6yhzVtJLCLJ7XbY90E0")
WATERMARK = str(os.environ.get("WATERMARK", "ATN_NEWS"))
FONT_SIZE = int(os.environ.get("FONT_SIZE", 17))
FONT_NAME = "Space_Age.ttf"  # check tools/fonts
TRANSPARENCY = float(os.environ.get("TRANSPARENCY", 0.75))
QUALITY = int(os.environ.get("QUALITY", 100))
