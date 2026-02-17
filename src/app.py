# Content Moderation API
# Flask API to serve our toxicity detection model

from flask import Flask, request, jsonify
from flask_cors import CORS
from moderator import ContentModerator
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize moderator (load model once at startup)
print("Initializing Content Moderation API...")
moderator = ContentModerator()
print("API Ready!")

@app.route('/', methods=['GET'])
def home():
    """API documentation endpoint"""
    return jsonify({
        'message': 'Content Moderation API',
        'version': '1.0',
        'endpoints': {
            '/': 'API documentation (you are here)',
            '/health': 'Health check',
            '/moderate': 'POST - Moderate single text',
            '/moderate/batch': 'POST - Moderate multiple texts'
        },
        'usage': {
            '/moderate': {
                'method': 'POST',
                'body': {
                    'text': 'Your text here',
                    'threshold': 0.5
                }
            },
            '/moderate/batch': {
                'method': 'POST',
                'body': {
                    'texts': ['Text 1', 'Text 2'],
                    'threshold': 0.5
                }
            }
        }
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model': 'toxic-bert',
        'version': '1.0'
    })

@app.route('/moderate', methods=['POST'])
def moderate_text():
    """Moderate a single text"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'text' not in data:
            return jsonify({
                'error': 'Missing required field: text'
            }), 400
        
        text = data['text']
        threshold = data.get('threshold', 0.5)
        
        # Validate threshold
        if not 0 <= threshold <= 1:
            return jsonify({
                'error': 'Threshold must be between 0 and 1'
            }), 400
        
        # Run moderation
        result = moderator.check_content(text, threshold)
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/moderate/batch', methods=['POST'])
def moderate_batch():
    """Moderate multiple texts at once"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'texts' not in data:
            return jsonify({
                'error': 'Missing required field: texts (array)'
            }), 400
        
        texts = data['texts']
        threshold = data.get('threshold', 0.5)
        
        # Validate texts is a list
        if not isinstance(texts, list):
            return jsonify({
                'error': 'texts must be an array'
            }), 400
        
        # Validate threshold
        if not 0 <= threshold <= 1:
            return jsonify({
                'error': 'Threshold must be between 0 and 1'
            }), 400
        
        # Run batch moderation
        results = moderator.moderate_batch(texts, threshold)
        stats = moderator.get_statistics(results)
        
        return jsonify({
            'success': True,
            'results': results,
            'statistics': stats
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Run the API
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)