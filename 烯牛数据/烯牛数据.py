import time

import requests
import execjs
import pandas
cookies = {
    'btoken': 'O8K5ZI4WXDYPXBIK9CSY0YI86W37C7CF',
    'hy_data_2020_id': '186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1678249454,1678273837',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1678275586',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    # 'cookie': 'btoken=O8K5ZI4WXDYPXBIK9CSY0YI86W37C7CF; hy_data_2020_id=186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22186bf766b6c23-04ca06f1ec32ef-74525476-921600-186bf766b6df7%22%7D; sajssdk_2020_cross_new_user=1; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1678249454,1678273837; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1678275586',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
}
start_time = time.time()
js_code = open('烯牛数据参数生成2.js', 'r', encoding='utf-8').read()
list_data = []
for page in range(0, 201, 20):
    parames = execjs.compile(js_code).call('main', page)
    json_data = {
        'payload': parames['payload'],
        'sig': parames['sig'],
        'v': 1,
    }

    response = requests.post(
        'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()
    js_code1 = open('烯牛数据逆向.js', 'r', encoding='utf-8').read()
    data = execjs.compile(js_code1).call('main1', response['d'])
    for dict_data in data['list']:
        datas = {
            '名称': dict_data['name'],
            '数量': dict_data['countCompany'],
            '介绍': dict_data['event'],
            '最近获投': [a['name'] for a in dict_data['companyVOs']],
            # '最近更新': dict_data['lastUpdateVO']['lastUpdateNews'],
            '更新时间': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(round(
                      dict_data['lastUpdateVO']['lastUpdateTime'] / 1000)))

        }
        list_data.append(datas)
pandas.DataFrame(list_data).to_excel('烯牛数据.xlsx', index=False)
print(list_data)
end_time = time.time()
print(end_time-start_time)
