# Test script for Content Moderation API

import requests
import json

# API base URL
BASE_URL = "http://localhost:5000"

print("=" * 60)
print("TESTING CONTENT MODERATION API")
print("=" * 60)

# Test 1: Health check
print("\n1. Testing /health endpoint...")
response = requests.get(f"{BASE_URL}/health")
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 2: Moderate single text (safe)
print("\n2. Testing /moderate with SAFE text...")
data = {
    "text": "Thank you so much for your help!",
    "threshold": 0.5
}
response = requests.post(f"{BASE_URL}/moderate", json=data)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 3: Moderate single text (toxic)
print("\n3. Testing /moderate with TOXIC text...")
data = {
    "text": "You're an idiot and I hate you!",
    "threshold": 0.5
}
response = requests.post(f"{BASE_URL}/moderate", json=data)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 4: Batch moderation
print("\n4. Testing /moderate/batch with multiple texts...")
data = {
    "texts": [
        "Great job on the project!",
        "You should be ashamed of yourself.",
        "The weather is nice today.",
        "I'm going to hurt you."
    ],
    "threshold": 0.5
}
response = requests.post(f"{BASE_URL}/moderate/batch", json=data)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Statistics: {json.dumps(result.get('statistics'), indent=2)}")
print(f"Total results: {len(result.get('results', []))}")

print("\n" + "=" * 60)
print("API TESTING COMPLETE!")
print("=" * 60)