import requests
import pandas as pd

def lambda_handler(event, context):
    response = requests.get("https://api.github.com")
    data = response.json()
    
    # Example pandas usage: converting JSON data to a DataFrame
    df = pd.DataFrame([data])
    
    return {
        'statusCode': 100,
        'body': df.to_json()
    }

if __name__ == "__main__":
    print(lambda_handler(None, None))
