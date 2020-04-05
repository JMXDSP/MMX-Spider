#https://v.douyin.com/v2AjDG/
import requests
import json
import re
import os
headers={
'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) '
                  'Version/11.0 Mobile/15A372 Safari/604.1'
}

VIDEO_URLS_LIST=[]
PAGE = 1

def get_info(url):
    user_id = None
    name = None
    dytk = None

    try:
        response = requests.get(url, headers=headers)
        print(response.url)
        user_id=response.url.split('/')[5].split('?')[0]
        name = re.search(r'class="nickname">(.*?)<', response.text)[1]
        dytk = re.search(r"dytk: '(.*?)'", response.text)[1]
    except Exception as e:
        print('获取用户信息失败')
    return user_id, name, dytk

def make_dir(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    else:
        pass
url = 'https://v.douyin.com/v2AjDG/'
user_id, name, dytk = get_info(url)
make_dir(name)

def get_all_video(user_id ,max_cursor, dytk):
    url='https://www.iesdouyin.com/web/api/v2/aweme/post/?'
    params = {'user_id': user_id,
              'count': 21,
              'max_cursor': max_cursor,
              'dytk': dytk}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        a=response.json()

        if a['aweme_list'] != []:
            for data in a['aweme_list']:
                video_name = data['desc']
                video_url = data['video']['play_addr']['url_list'][0]
                VIDEO_URLS_LIST.append([video_name, video_url])
            global PAGE
            if a.get('has_more'):
                print("正在获取第{}页视频".format(PAGE))
                PAGE += 1
                get_all_video(user_id, a['max_cursor'], dytk)
            else:
                print("获取完毕！")
        else:
            get_all_video(user_id, max_cursor, dytk)

get_all_video(user_id, 0, dytk)
print("总共有{}个视频".format(len(VIDEO_URLS_LIST)))

def dowload_video(url, name, video_name):
    video_file = "{}/{}.mp4".format(name, video_name)
    with open(video_file, 'wb') as f:
        response = requests.get(url, headers=headers)
        f.write(response.content)


if __name__ == '__main__':
    for i, video in enumerate(VIDEO_URLS_LIST,1):
        print("下载第{}个视频".format(i))
        dowload_video(video[1], name, video[0])













        #if __name__ == '__main__':
#    pass
#https://www.iesdouyin.com/web/api/v2/aweme/post/?
# sec_uid=MS4wLjABAAAAlR2QZWAIecBjz4vqb_LZFHQzeNMEUdRsQvHtSRmu5Z8&
## count=21
# #max_cursor=1581597183000&
# #aid=1128&
# _signature=4x9uhBARvacLxUz531Ka4eMfbp&
# dytk=dced502bfe0b2e376b829d0d2a4d96d6