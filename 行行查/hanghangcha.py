import json
import time
import execjs
import requests
import pandas

cookies = {
    'UM_distinctid': '186c104e53c657-03a67924cd5a29-74525476-e1000-186c104e53d84',
    'Hm_lvt_1521e0fb49013136e79181f2888214a7': '1678275569,1678434395',
    'JSESSIONID': '4A62E9150CA9B36EB4D0455DA8D10AA8',
    'Hm_lpvt_1521e0fb49013136e79181f2888214a7': '1678439149',
    '_ACCOUNT_': 'MDU5ZDZiNTk1MDE4NDU0M2E2MDI2YWMzMTQ1MzQ4NTIlNDAlNDBtb2JpbGU6MTY3'
                 'OTY1NDY3OTU2NzoxYzdlNWUwMzk0MTIxYzUyNzY4ZTc3YzFmYTRmOTQ2YQ',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Auth-Plus': '',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=186c104e53c657-03a67924cd5a29-74525476-e1000-186c104e53d84; '
              'Hm_lvt_1521e0fb49013136e79181f2888214a7=1678275569,1678434395; '
              'JSESSIONID=4A62E9150CA9B36EB4D0455DA8D10AA8; Hm_lpvt_1521e0fb49013136e79181f2888214a7=1678439149; '
              '_ACCOUNT_=MDU5ZDZiNTk1MDE4NDU0M2E2MDI2YWMzMTQ1MzQ4NTIlNDAlNDBtb2JpbGU6MTY3OTY1NDY3'
              'OTU2NzoxYzdlNWUwMzk0MTIxYzUyNzY4ZTc3YzFmYTRmOTQ2YQ',
    'Origin': 'https://www.hanghangcha.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.63',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.0',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'filter': '{"city":"","lv":null,"province":"","userId":3037069,"companyId":null,"limit":20,"skip":0,'
              '"keyword":null,"companyType":"local"}',
}

response = requests.get('https://api.hanghangcha.com/hhc/invest/getProduct', params=params, cookies=cookies, headers=headers).json()

js_code = open('行行查decrypt.js', 'r', encoding='utf-8').read()
datas = execjs.compile(js_code).call('decrypt', response['data'])
json_data = json.loads(datas)
list_data = []
for data in json_data['data']['data']:
    sj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['timestamp']))
    dict_data = {
        '项目名称': data['product_name'],
        '业务简述': data['business'],
        '项目地区': data['area'],
        '轮次': data['round'],
        '时间': sj,
        '金额': data['amount'],
        '投资方': data['investor']

    }
    list_data.append(dict_data)
# pandas.DataFrame(list_data).to_excel(f'行行查{time.time()}.xlsx', index=False)
pandas.DataFrame(list_data).T.reset_index().T.to_excel(f'行行查{time.time()}.xlsx', index=False, header=False)

