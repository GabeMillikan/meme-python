# IGNORE THIS FILE!
# THERE IS NO NEED TO READ OR UNDERSTAND THIS FILE
# But if you're interested:
# This file makes it possible to do `import meme` from
# the other example files by using some less-than-ideal
# importlib hacking to import `meme` via its absolute path

import sys, pathlib, importlib.util

examples_folder = pathlib.Path(__file__).parent
repository_folder = examples_folder.parent
library_entry_point = repository_folder / 'meme' / '__init__.py'

meme_spec = importlib.util.spec_from_file_location('meme', str(library_entry_point.absolute()))
meme = importlib.util.module_from_spec(meme_spec)
sys.modules['meme'] = meme
meme_spec.loader.exec_module(meme)
