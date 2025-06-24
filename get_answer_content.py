import requests
from _env import token

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'access-control-allow-origin': '*',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json',
    'origin': 'https://co.elearn.vn',
    'priority': 'u=1, i',
    'referer': 'https://co.elearn.vn/',
    'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
}

def getAnswerById(id: str):
    json_data = {
        'baiLamId': id,
        'isTeacher': 1,
    }

    response = requests.post('https://exam-api.elearn.vn/api/bailam/chi-tiet-ket-qua', headers=headers, json=json_data)
    return response.json()["data"]["baiLamChiTiets"]

print(getAnswerById("23709730-55ae-4bee-8ea5-c59ace21ea8c"))