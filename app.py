from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/verify": {"origins": "*"}})


@app.route('/verify', methods=['POST'])
def verify_faces():
    try:
        profile_image = request.files['profile_image']
        selfie_image = request.files['selfie_image']

        profile_image_path = os.path.join('uploads', 'profile_image.jpg')
        selfie_image_path = os.path.join('uploads', 'selfie_image.jpg')

        profile_image.save(profile_image_path)
        selfie_image.save(selfie_image_path)

        result = DeepFace.verify(profile_image_path, selfie_image_path)

        return jsonify({
            'verified': result['verified'],
            'distance': result['distance']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    @app.route('/hello', methods=['GET'])
    def index():
        return "Hello"

if __name__ == '__main__':
    app.run(debug=True)