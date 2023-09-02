import requests

def test_process_conv():
    url = "http://127.0.0.1:5000/process/conv"
    files = {'blob': open('/Users/i564228/Desktop/freeflow/3min_coversation.m4a', 'rb')}
    response = requests.post(url, files=files)
    print("Response from /process/conv:")
    print(response.json())

def test_process_prompt():
    url = "http://127.0.0.1:5000/process/prompt"
    data = {'prompt': 'Who are you?'}
    response = requests.post(url, data=data)
    print("Response from /process/prompt:")
    print(response.json())

if __name__ == "__main__":
    test_process_conv()
    #test_process_prompt()