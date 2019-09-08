import requests
dictToSend = {'name':'sthDifferent'}
requests.post('http://localhost:5000/process', json=dictToSend)
