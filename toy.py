import requests
import json

def draw_person_image(prompt, gender=1, step=30):
    """
    Send a request to the image drawing API to generate a person's portrait.
    
    :param prompt: Text description for the image generation
    :param gender: Gender of the person (1 for male, 0 for female, default is 1)
    :param step: Generation step parameter (default is 30)
    :return: API response
    """
    # API endpoint
    url = "http://1247426312861996.cn-beijing.pai-eas.aliyuncs.com/api/predict/image_draw/image/draw_person/v1"
    
    # Headers
    headers = {
        'Authorization': 'ZDJmZWM1NzYyMDg1M2I5YTE0NmY2MTc3MTgyMjVkYjQyZTcyNjk4Mg==',
        'content-type': 'application/json'
    }
    
    # Request payload
    payload = {
        "gender": gender,
        "step": step,
        "prompt": prompt
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Return the response JSON
        return response.json()
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = "Portrait, oil painting, male with features similar to Xijinping"
    result = draw_person_image(prompt)
    if result:
        print("API Response:", result)