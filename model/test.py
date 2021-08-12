import os
import shutil

import requests


def get_questions():
    testId = "testId123"
    topic = "topic456"
    api = "questions"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/"+api+"/"
    values = {'testId': testId, 'topic': topic}
    r = requests.get(url, params=values)
    if r.headers['content-type'] == "application/octet-stream":
        with open("my.zip", 'wb') as f:
            f.write(r.content)


def post_questions():
    testId = "testId456"
    topic = "topic789"
    api = "questions"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/" + api + "/"
    files = {'file': open('model.txt', 'rb')}
    # files = {'file': ('nameoffile', open('namoffile', 'rb'), 'text/html', 'other header'),
    #          'file2': ('nameoffile2', open('nameoffile2', 'rb'), 'application/xml', 'other header')}
    values = {'testId': testId, 'topic': topic}
    r = requests.post(url, files=files, data=values)
    print(r)


def get_tests():
    userId = "ljw"
    testId = "testId123"
    submitId = "submitId123"
    topic = "topic456"
    api = "tests"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/"+api+"/"
    values = {'userId':userId, 'testId': testId, 'submitId': submitId, 'topic': topic}
    r = requests.get(url, params=values)
    print(r.headers['filePath'])
    if r.headers['content-type'] == "application/octet-stream":
        with open("my.txt", 'wb') as f:
            f.write(r.content)


def post_tests():
    userId = "ljw"
    testId = "testId123"
    submitId = "submitId123"
    topic = "topic456"
    api = "tests"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/" + api + "/"
    files = {'file': open('model.txt', 'rb')}
    # files = {'file': ('nameoffile', open('namoffile', 'rb'), 'text/html', 'other header'),
    #          'file2': ('nameoffile2', open('nameoffile2', 'rb'), 'application/xml', 'other header')}
    values = {'userId':userId, 'testId': testId, 'submitId': submitId, 'topic': topic}
    r = requests.post(url, files=files, data=values)
    print(r)


def get_bits():
    userId = "ljw"
    testId = "testId123"
    submitId = "submitId123"
    topic = "topic456"
    api = "bits"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/"+api+"/"
    values = {'userId':userId, 'testId': testId, 'submitId': submitId, 'topic': topic}
    r = requests.get(url, params=values)
    print(r.headers['filePath'])
    if r.headers['content-type'] == "application/octet-stream":
        with open("my.txt", 'wb') as f:
            f.write(r.content)


def post_bits():
    userId = "ljw"
    testId = "testId123"
    submitId = "submitId123"
    topic = "topic456"
    api = "bits"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/" + api + "/"
    files = {'file': open('model.txt', 'rb')}
    # files = {'file': ('nameoffile', open('namoffile', 'rb'), 'text/html', 'other header'),
    #          'file2': ('nameoffile2', open('nameoffile2', 'rb'), 'application/xml', 'other header')}
    values = {'userId':userId, 'testId': testId, 'submitId': submitId, 'topic': topic}
    r = requests.post(url, files=files, data=values)
    print(r)


def get_logs():
    userId = "ljw"
    testId = "testId123"
    submitId = "submitId123"
    topic = "topic456"
    api = "logs"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/"+api+"/"
    values = {'userId':userId, 'testId': testId, 'submitId': submitId, 'topic': topic}
    r = requests.get(url, params=values)
    print(r.headers['filePath'])
    if r.headers['content-type'] == "application/octet-stream":
        with open("my.txt", 'wb') as f:
            f.write(r.content)


def post_logs():
    userId = "ljw"
    testId = "testId123"
    submitId = "submitId123"
    topic = "topic456"
    api = "logs"
    # url = "http://127.0.0.1:8010/download/?deviceId=1&userName=ljw&fid=9057116c-7d85-11eb-8f1b-000c291dfee8&count=18&bitFileName=default_10.bit"
    url = "http://localhost:8010/" + api + "/"
    files = {'file': open('model.txt', 'rb')}
    # files = {'file': ('nameoffile', open('namoffile', 'rb'), 'text/html', 'other header'),
    #          'file2': ('nameoffile2', open('nameoffile2', 'rb'), 'application/xml', 'other header')}
    values = {'userId':userId, 'testId': testId, 'submitId': submitId, 'topic': topic}
    r = requests.post(url, files=files, data=values)
    print(r)


def get_help():
    api = "help"
    url = "http://localhost:8010/"+api+"/"
    r = requests.get(url)
    print(r.headers['filePath'])
    if r.headers['content-type'] == "application/octet-stream":
        with open("my.txt", 'wb') as f:
            f.write(r.content)


def get_ping():
    api = "ping"
    url = "http://localhost:8010/"+api+"/"
    values = {"type": "md"}
    r = requests.get(url, data=values)
    print(r)


if __name__ == "__main__":
    shutil.copyfile("model.txt", "ter2")
    path = os.path.join("/tmp", "model.txt")
    print(path)
    # get_help()
    # get_questions()
    # post_questions()
    # post_tests()
    # get_tests()
    # post_bits()
    # get_bits()
    # post_logs()
    # get_logs()



