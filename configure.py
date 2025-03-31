import json

def generate_json():
    data = {
        "PH_DEV_MON_CUSTOM_JSON": {
            "reptVendor": "GitHub.com",
            "reptModel": "GitHub",
            "reptDevName": "GitHub.com",
            "reptDevIpAddr": "1.1.1.1",
            "palavra-chave": "push",
            "json": {
                "ref": "refs/heads/main",
                "antes": "dbfa142e6111162311[...]"
            }
        },
        "repo": "RAFAEL849412/Sat-lite",
        "repoID": 957016666,
        "description": "Acelere seu desenvolvimento com o GitHub Satellite. Mude a maneira como você codifica! O GitHub Satellite é sua nova ferramenta de programação, alimentada por tecnologia de satélite que sugere linhas de código e funções inteiras conforme você as escreve.",
        "languages": [
            {"name": "C++", "percent": 54.3},
            {"name": "Python", "percent": 45.6},
            {"name": "C", "percent": 0.1}
        ]
    }
    
    json_output = json.dumps(data, indent=4)
    return json_output

if __name__ == "__main__":
    print(generate_json())
    
