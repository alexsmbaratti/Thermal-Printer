from flask import Flask

import api_utils
import print_utils
import oled_utils

app = Flask(__name__)

@app.route("/")
def hello_world():
    return str(200)


@app.route('/api/pixel-shelf/library/size', methods=['POST'])
def print_library_count():
    count = api_utils.getLibraryCount()
    print_utils.print_library_size(count)
    return str(count)


@app.route('/api/pixel-shelf/library', methods=['POST'])
def print_library_entry():
    data = request.data
    print(str(data))
    print_utils.print_library_entry(data)
    return str(200)

