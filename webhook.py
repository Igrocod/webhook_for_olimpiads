import json

import requests
from random import sample

url = 'https://tools.aimylogic.com/api/googlesheet2json?sheet=Список&id=1CPFLd6y_KQxY2T5nAMeWQMcpkhCyNtfGMHMWrE9LH4M'

resp = requests.get(url)
resp.encoding = 'utf-8'
resp_js = resp.json()



def webhook(session):
    action = session['action']
    if resp.status_code == 200:
        if action == 'event1':
            check = (list(filter(
                lambda item: item['response'] == session["subject"] and (
                        item["min_class"] <= session['u_class'] and item["max_class"] >= session['u_class']),
                resp_js)))
            ln = len(check)
            if ln > 0:
                session["name"] = sample(check, 1)[0]
            else:
                session['name'] = False
        elif action == 'event2':
            session["name"] = sample(resp_js, 1)[0]
    else:
        session['name'] = False





    return json.dumps(session)

