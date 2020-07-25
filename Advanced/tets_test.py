#!/router/bin/python
import requests
from time import sleep

try:
    print()
    put_url = "https://appcheck.cisco.com/api/upload/TestOneComp.war"
    # put_url = "https://appcheck.cisco.com/api/upload/TestZeroComp.war"
    data = open("/auto/blackduck/OneComponent.war", 'rb').read()
    headers_put = {
        "Content-Type": "application/binary",
        "Group": "20",
        'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='
    }
    upload = requests.put(put_url, data=data, headers=headers_put)
    print ("Upload Response code ::: ", upload.status_code)
    if upload.status_code != 200:
        print ("Upload of file unsuccessful")
        exit(1)
    print ("Sleeping 10 secs")
    sleep(10)
    dic = upload.json()
    print ("Upload file Response ::: ", dic)
    product_id = dic['results']['product_id']
    print ("Product uploaded : ", product_id)
    url = "https://appcheck.cisco.com/api/product/" + str(product_id) + "/csv-libs"
    # url = "https://appcheck.cisco.com/api/product/156172/csv-libs"
    # url = "https://appcheck.cisco.com/api/product/156868/csv-libs"
    params = {'columns': 'component'}

    headers = {'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='}
    r = requests.get(url, params=params, headers=headers)

    # print r.status_code
    if r.status_code == 200:
        comp = list((r.text).split("\n"))
        comp = [i.strip() for i in comp]
        comp = [i.strip("\"") for i in comp]
        comp.remove("")
        # print type(comp)
        if comp[0] == 'Component':
            comp.pop(0)
        print ("Component Count ::: ", len(comp))
        print ("Components are :::::: ", comp)
        if len(comp) == 0:
            print ("Component count in the Product is less than 1 when components were added. Please check !!!")
            print ("Sending email !!!")
            exit(1)
        else :
            del_url = "https://appcheck.cisco.com/api/product/" + str(product_id) + "/"
            delete_ser = requests.delete(del_url,headers=headers)
            if delete_ser.status_code ==200:
                print ("Sucessfully deleted result with product_id : ",str(product_id))
except Exception as e:
    print ("Exception ::: ", e)

# # !/router/bin/python
# import requests
#
# put_url = "https://appcheck.cisco.com/api/upload/TestOneComp.war"
# # put_url = "https://appcheck.cisco.com/api/upload/TestZeroComp.war"
# data = open("/auto/blackduck/OneComponent.war", 'rb').read()
# headers_put = {
#     "Content-Type": "application/binary",
#     "Group": "1",
#     'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='
# }
# upload = requests.put(put_url, data=data, headers=headers_put)
# print
# "Upload Response code ::: ", upload.status_code
# if upload.status_code != 200:
#     print
#     "Upload of file unsuccessful"
#     exit(1)
# dic = upload.json()
# print
# "Upload file Response ::: ", dic
# product_id = dic['results']['product_id']
# url = "https://appcheck.cisco.com/api/product/" + str(product_id) + "/csv-libs"
# # url = "https://appcheck.cisco.com/api/product/156172/csv-libs"
# # url = "https://appcheck.cisco.com/api/product/156868/csv-libs"
# params = {'columns': 'component'}
#
# headers = {'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='}
# r = requests.get(url, params=params, headers=headers)
#
# # print r.status_code
# if r.status_code == 200:
#     comp = list((r.text).split("\n"))
#     comp = [i.strip() for i in comp]
#     comp = [i.strip("\"") for i in comp]
#     comp.remove("")
#     # print type(comp)
#     if comp[0] == 'Component':
#         comp.pop(0)
#     print
#     "Component Count ::: ", len(comp)
#     print
#     "Components are :::::: ", comp
#     if len(comp) == 0:
#         print
#         "Component count in the Product is less than 1 when components were added. Please check !!!"
#         print
#         "Sending email !!!"
#         exit(1)
#         # mail  service render to go here
#
#
