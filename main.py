from flask import Flask

import api_utils
import print_utils

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/pixel-shelf/library/size', methods=['POST'])
def print_library_entry():
    count = api_utils.getLibraryCount()
    print_utils.print_library_size(count)
    return str(count)
