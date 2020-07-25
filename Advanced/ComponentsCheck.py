import requests
import json
from time import sleep

try:
    print()
    put_url = "https://appcheck.cisco.com/api/upload/TestNew.war"
    data = open("C:\\Users\\ppattnai\\Desktop\\Blackduck\\OneComponent.war", 'rb').read()
    headers_put = {
        "Content-Type": "application/binary",
        "Group": "1",
        'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='
    }
    upload = requests.put(put_url, data=data, headers=headers_put)
    print(upload.status_code)
    if upload.status_code != 200:
        print("Upload of file unsuccessful")
        exit(1)
    print ("Sleep for 10 secs")
    sleep(10)
    dic = upload.json()
    # dic = json.dumps(upload.json())
    print(dic)
    product_id = dic['results']['product_id']
    url = "https://appcheck.cisco.com/api/product/" + str(product_id) + "/csv-libs"
    print(url)
    # url = "https://appcheck.cisco.com/api/product/156172/csv-libs"
    # url = "https://appcheck.cisco.com/api/product/156868/csv-libs"
    params = {'columns': 'component'}

    headers = {'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='}
    r = requests.get(url, params=params, headers=headers)

    print(r.status_code)
    print(r.text)
    if r.status_code == 200:
        comp = list((r.text).split("\n"))
        comp = [i.strip() for i in comp]
        comp = [i.strip("\"") for i in comp]
        comp.remove("")
        print(type(comp))
        if comp[0] == 'Component':
            comp.pop(0)
        if len(comp) <= 1:
            print("True")
            # mail  service render to go here
        print(comp)
        print(len(comp))
    else:
        print("Invalid response from \"", url, "\" with status code : ", r.status_code)
except Exception as e:
    print("Exception ::: ",e)



