import requests
import os.path
import sched, time
s = sched.scheduler(time.time, time.sleep)
headers = {
    'Content-Type': 'application/json',
}

def requests_version():

    r = requests.get('xxxxx')
    if r.status_code == requests.codes.ok:
        print("Get json!")
    check_version(r.content['url'], r.content['name'], r.content['version'])
    s.enter(60, 1, requests_version)

def check_version(url, name, version):
    filename = name + ".txt"
    if not os.path.isfile(filename):
        fp = open(filename, "w+")
        fp.write(version)
    else:
        fp = open(filename, "r")
        old_version = fp.read()
        fp.close()
        fp = open(filename, "w+")
        print(version)
        print(old_version)
        if version > old_version:
            print("Update.")
            fp.write(version)
            data = {'url': url, 'name': name, 'version': version}
            requests.post("http://localhost:5555", headers=headers, data=data)
        else:
            print("It has been the latest version.")

check_version("https://i.imgur.com/Jvh1OQm.jpg", "hello", "1.0.6")
#s.enter(60, 1, requests_version)
#s.run()
