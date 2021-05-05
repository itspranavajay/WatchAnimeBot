import glob
import logging
from pathlib import Path
from AnimeWatchBot.helper import load_plugins
from AnimeWatchBot import GogoAnime

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "AnimeWatchBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully")
print("Enjoy")

if __name__ == "__main__":
    GogoAnime.run_until_disconnected()
