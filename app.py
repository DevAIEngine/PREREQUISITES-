import os
import logging
from flask import Flask, request, jsonify, render_template

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='src/core_engine/live')

# Initialize Vertex AI
PROJECT_ID = os.environ.get("PROJECT_ID", "guce-project")
REGION = os.environ.get("REGION", "us-central1")
try:
    import vertexai
    vertexai.init(project=PROJECT_ID, location=REGION)
except Exception as e:
    logger.error(f"Failed to initialize Vertex AI: {e}")

from src.core_engine.obfuscation.phantom_jax_lora import phantom_jax_bp
app.register_blueprint(phantom_jax_bp)

@app.route('/', methods=['GET'])
def process_request():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# To support the original endpoint test
from src.core_engine.obfuscation.phantom_jax_lora import optimize_tensor_stream
app.add_url_rule('/', view_func=optimize_tensor_stream, methods=['POST'])


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

# CORE-ENGINE-FINGERPRINT: QXVyb3JhX09TSVJJU19Db3JlX0VuZ2luZQ==
