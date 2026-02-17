# Content Moderation Bot - Phase 2: Toxicity Detection
# Using a model specifically trained for toxic content

from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

class ContentModerator:
    def __init__(self):
        """Initialize the content moderator with toxicity detection model"""
        print("Loading toxicity detection model...")
        print("(First time may take 2-3 minutes to download)")
        
        # Using a model specifically trained for toxicity detection
        self.classifier = pipeline(
            "text-classification",
            model="unitary/toxic-bert",
            top_k=None  # Get all toxicity scores
        )
        print("✓ Model loaded successfully!\n")
    
    def check_content(self, text, threshold=0.5):
        """
        Check if content is toxic
        
        Args:
            text (str): The text to analyze
            threshold (float): Confidence threshold (0.0 to 1.0)
            
        Returns:
            dict: Contains toxicity analysis
        """
        results = self.classifier(text)[0]
        
        # Find the toxic label
        toxic_result = None
        for result in results:
            if 'toxic' in result['label'].lower():
                toxic_result = result
                break
        
        if toxic_result:
            is_toxic = toxic_result['score'] > threshold
            confidence = round(toxic_result['score'] * 100, 2)
        else:
            is_toxic = False
            confidence = 0.0
        
        return {
            'text': text,
            'is_toxic': is_toxic,
            'confidence': confidence,
            'status': 'FLAGGED' if is_toxic else 'SAFE',
            'threshold': threshold * 100
        }
    
    def moderate_batch(self, texts, threshold=0.5):
        """
        Moderate multiple texts at once
        
        Args:
            texts (list): List of texts to analyze
            threshold (float): Confidence threshold
            
        Returns:
            list: Results for each text
        """
        results = []
        for text in texts:
            results.append(self.check_content(text, threshold))
        return results
    
    def get_statistics(self, results):
        """Get statistics from moderation results"""
        total = len(results)
        flagged = sum(1 for r in results if r['is_toxic'])
        safe = total - flagged
        
        return {
            'total': total,
            'flagged': flagged,
            'safe': safe,
            'flagged_percentage': round((flagged / total * 100), 2) if total > 0 else 0
        }


# Test the upgraded moderator
if __name__ == "__main__":
    print("=" * 60)
    print("CONTENT MODERATION BOT - TOXICITY DETECTION")
    print("=" * 60)
    print()
    
    # Initialize moderator
    moderator = ContentModerator()
    
    # Test cases - mix of safe and toxic content
    test_texts = [
        "Thank you so much for your help!",
        "You're an idiot and nobody likes you.",
        "Great work on the presentation today!",
        "I hate you and I hope you fail.",
        "The weather is nice today.",
        "This is a terrible product, complete waste of money.",
        "You should be ashamed of yourself, loser.",
        "Can you please help me with this issue?",
        "I'm going to hurt you if you don't stop.",
        "This restaurant has amazing food!"
    ]
    
    print("Analyzing {} comments...\n".format(len(test_texts)))
    
    # Run moderation
    results = moderator.moderate_batch(test_texts, threshold=0.5)
    
    # Display results
    for i, result in enumerate(results, 1):
        status_symbol = "🚫" if result['is_toxic'] else "✓"
        print(f"{status_symbol} Test {i}: [{result['status']}]")
        print(f"   Text: \"{result['text']}\"")
        print(f"   Toxicity Confidence: {result['confidence']}%")
        print()
    
    # Show statistics
    stats = moderator.get_statistics(results)
    print("=" * 60)
    print("MODERATION STATISTICS")
    print("=" * 60)
    print(f"Total Comments: {stats['total']}")
    print(f"✓ Safe: {stats['safe']}")
    print(f"🚫 Flagged: {stats['flagged']}")
    print(f"Flagged Rate: {stats['flagged_percentage']}%")
    print()