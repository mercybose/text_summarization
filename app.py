from flask import Flask, jsonify, request, abort
import model

app = Flask(__name__)


@app.route('/summarize', methods=['POST'])
def summarize():
    if (not request.json) or ('text_to_summarize' not in request.json):
        abort(400)

    txt = request.json['text_to_summarize']

    return jsonify({'original_txt': txt, 'summary': model.get_summarized_val(txt)}), 201


if __name__ == '__main__':
    app.run()
