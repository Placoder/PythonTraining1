import requests
product_id = 159460
headers = {'Authorization': 'Basic cHBhdHRuYWk6UHVwdW5+ODM1OQ=='}
del_url = "https://appcheck.cisco.com/api/product/" + str(product_id) + "/"
delete_ser = requests.delete(del_url,headers=headers)

print(delete_ser)

print(delete_ser.status_code)