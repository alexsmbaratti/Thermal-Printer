from flask import Flask

import api_utils
import print_utils

app = Flask(__name__)


@app.route("/")
def hello_world():
    if print_utils.has_paper():
        return str(200)
    else:
        return str(410)  # Out of paper status code


@app.route('/api/pixel-shelf/library/size', methods=['POST'])
def print_library_count():
    count = api_utils.getLibraryCount()
    print_utils.print_library_size(count)
    return str(count)


@app.route('/api/pixel-shelf/library', methods=['POST'])
def print_library_entry():
    # TODO: Read request body and print a library entry based on the request body
    return str(501)


@app.route('/api/pixel-shelf/library/<id>', methods=['POST'])
def print_library_entry(id):
    entry = api_utils.getLibraryEntry(id)
    print_utils.print_library_entry(entry)
    return str(200)
