import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion":None
        }
    emotion_dict = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    max_key = max(emotion_dict, key=emotion_dict.get)
    emotion_dict["dominant_emotion"] = max_key
    return emotion_dict

if __name__ == "__main__":
    answer = emotion_detector("")
    print(answer)