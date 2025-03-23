import argparse
import os

import polib
from googletrans import Translator

from .utilities.constants import UNTRANSLATED_PATH, TRANSLATED_PATH, LANGUAGE_SOURCE, LANGUAGE_DESTINATION
from .utilities.io import read_lines, save_lines
from .utilities.match import recognize_po_file


async def translate(source: str, arguments) -> str:
    """ Translates a single string into target language. """
    translator = Translator()
    result = await translator.translate(source, dest=arguments.to, src=arguments.fro)
    return result.text

def create_close_string(line: str) -> str:
    """ Creates single .po file translation target sting. """
    return r"msgstr " + '"' + line + '"' + "\n"


async def solve(new_file: str, old_file: str, arguments):
    """ Translates single file. """
    lines = read_lines(old_file)
    for line in lines:
        line.msgstr = polib.unescape(
            await translate(polib.escape(line.msgid), arguments))
        print(f"Translated {lines.percent_translated()}% of the lines.")
    save_lines(new_file, lines)


async def run(**kwargs):
    """ Core process that translates all files in a directory.
     :parameter fro:
     :parameter to:
     :parameter src:
     :parameter dest:
     """
    found_files = False

    parser = argparse.ArgumentParser(
        description='Automatically translate PO files using Google translate.')
    parser.add_argument('--fro', type=str, help='Source language you want to translate from to (Default: en)',
                        default=kwargs.get('fro', LANGUAGE_SOURCE))
    parser.add_argument('--to', type=str, help='Destination language you want to translate to (Default: et)',
                        default=kwargs.get('to', LANGUAGE_DESTINATION))
    parser.add_argument('--src', type=str, help='Source directory or the files you want to translate',
                        default=kwargs.get('src', UNTRANSLATED_PATH))
    parser.add_argument('--dest', type=str, help='Destination directory you want to translated files to end up in',
                        default=kwargs.get('dest', TRANSLATED_PATH))

    arguments = parser.parse_args([])

    if os.path.isfile(arguments.src):
        if recognize_po_file(arguments.src):
            found_files = True
            await solve(arguments.dest, arguments.src, arguments)
    else:
        found_files = False
        for file in os.listdir(arguments.src):
            if recognize_po_file(file):
                found_files = True
                await solve(os.path.join(arguments.dest, file),
                      os.path.join(arguments.src, file), arguments)

    if not found_files:
        # raise Exception(f"Couldn't find any .po files at: '{arguments.src}'")
        print(f"Couldn't find any .po files at: '{arguments.src}'")
        pass


if __name__ == '__main__':
    run()
