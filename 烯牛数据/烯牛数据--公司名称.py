import execjs
import requests

cookies = {
    'btoken': 'O8K5ZI4WXDYPXBIK9CSY0YI86W37C7CF',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1678249454',
    'hy_data_2020_id': '186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1678250355',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    # 'cookie': 'btoken=O8K5ZI4WXDYPXBIK9CSY0YI86W37C7CF; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1678249454; hy_data_2020_id=186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%7D; sajssdk_2020_cross_new_user=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1678250355',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
}

js_code = open('烯牛数据参数生成.js', 'r', encoding='utf-8').read()
parames = execjs.compile(js_code).call('main')
json_data = {
    'payload': parames['payload'],
    'sig': parames['sig'],
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_home/list_home_tag_company',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
js_code1 = open('烯牛数据逆向.js', 'r', encoding='utf-8').read()
parames1 = execjs.compile(js_code1).call('main1', response["d"])
for data in parames1['list']:
    print(data['fullName'])
