import base64

def base64_to_str(x):
    return base64.b64decode(x).decode('utf-8')