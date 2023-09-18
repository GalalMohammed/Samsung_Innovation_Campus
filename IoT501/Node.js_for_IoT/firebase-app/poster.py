#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    payload = {'name': 'test_app', 'age': 1}
    requests.post('http://localhost:3000', data=payload, timeout=0.001)
