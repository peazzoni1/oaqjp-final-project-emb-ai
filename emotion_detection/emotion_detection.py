import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'Content-Type': 'application/json',
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        
        if 'emotionPredictions' in result and len(result['emotionPredictions']) > 0:
            emotions = result['emotionPredictions'][0]['emotion']
            
            dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]

            formatted_result = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
            
            return formatted_result
    else:
        return {
            "error": f"Request failed with status code {response.status_code}",
            "details": response.text
        }