from flask import Flask

import api_utils
import print_utils
import oled_utils

app = Flask(__name__)

oled_utils.display_idle()

@app.route("/")
def hello_world():
    return str(200)


@app.route('/api/pixel-shelf/library/size', methods=['POST'])
def print_library_count():
    oled_utils.display_status('Printing library size...')
    count = api_utils.getLibraryCount()
    print_utils.print_library_size(count)
    oled_utils.display_idle()
    return str(count)


@app.route('/api/pixel-shelf/library/<id>', methods=['POST'])
def print_library_entry_from_id(id):
    oled_utils.display_status('Printing library entry...')
    entry = api_utils.getLibraryEntry(id)
    print_utils.print_library_entry(entry)
    oled_utils.display_idle()
    return str(200)


@app.route('/api/pixel-shelf/library', methods=['POST'])
def print_library_entry():
    # TODO: Read request body and print a library entry based on the request body
    return str(501)
