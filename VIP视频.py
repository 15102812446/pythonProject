import requests
import json

url = 'https://haokan.baidu.com/videoui/api/videorec?tab=gaoxiao&act=pcFeed&pd=pc&num=20&shuaxin_id=1584866887932'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'cookie': 'BAIDUID = 74DF3564617B2C9FA9D0468C96EA2D5B: FG = 1;BIDUPSID =  74DF3564617B2C9FA9D0468C96EA2D5B;PSTM = 1575894957;BDRCVFR[TfzreFuSob] =  mk3SLVN4HKm;delPer = 0;PSINO = 6;H_PS_PSSID =;BDORZ =  FFFB88E999055A3F8A630C64834BD6D0;BDSFRCVID = OV8sJeCCxG3HHcRuJgPnSaVvNIfB4Z1  - g_EP3J;H_BDCLCKID_SF = tR333R7oKRu_HRjYbb__ -  P4DHUjHfRO2X5REVh7CfPOkeqOJ2Mt5yMkS0loZKhOXLK6pLqrY5q_MoCDzbpnp05tpexbH55uetn  - f_U5;PC_TAB_LOG =  haokan_website_page;Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5 =  1584866867;Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5 = 1584866869;reptileData  = % 7B % 22data % 22 % 3A %  2242da399b6855dc02a8c72001523e8685c0ec37b2f26178d68783bd941cca8e26e937dbe59953fb090211f372d6eb955dc20beb8396b045e5df4d725d5fedac7aaa415293534710428b39a3ce5851c795051c61beacdb88b1de6226323caf92f6a0c55a67f60dc0e50896f95dc05d54fa4803a75c5e3ba3751015d7b13e253544  % 22 % 2C % 22key_id % 22 % 3A % 2230 % 22 % 2C % 22sign % 22 % 3A %  22fd3d5c98 % 22 % 7D '}

respons = requests.get(url, headers=headers)
text = respons.text
# print(respons.text)

data = json.loads(text)  # 字典
# print(data)
list1 = data['data']['response']['videos']
# print(list1)

for id in list1:
    print(id)
    video_title = id['title']
    video_url = id['play_url']
    print(video_title, video_url)
    print('下载')
    video_data = requests.get(video_url, headers=headers).content

    with open('video\\' + video_title, 'wb') as f:
        f.write(video_data)
print('完成')