import json
import pymysql

conn = pymysql.connect("localhost", "root", "1234567", "test")  # 创建数据库连接
cursor = conn.cursor()  # 获取游标


def response(flow):
    # https://search-hl.amemv.com/aweme/v1/general/search/single/?os_api=22&device_type=SM-G955F&ssmix=a&manifest_version_code=800&dpi=240&js_sdk_version=1.25.4.2&uuid=355757491360810&app_name=aweme&version_name=8.0.0&ts=1579698640&app_type=normal&ac=wifi&update_version_code=8002&channel=wandoujia_aweme2&_rticket=1579698644370&device_platform=android&iid=96709029055&version_code=800&openudid=634e6ad608100482&device_id=70292605260&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007
    # 综合视频保存
    if 'aweme/v1/general/search/single/' in flow.request.url:
        print('aweme/v1/general/search/single/')
        try:
            for aweme in json.loads(flow.response.text)['data']:
                if aweme['type'] == 1:
                    try:
                        aweme_info = aweme['aweme_info']
                        user_info = aweme['aweme_info']['author']
                        # region 视频信息
                        aweme_uid = aweme_info['author_user_id']  # 用户编号
                        aweme_id = aweme_info['aweme_id']  # 视频id
                        aweme_desc = aweme_info['desc']  # 视频标题
                        aweme_share_url = aweme_info['share_url']  # 视频地址
                        aweme_create_time = aweme_info['create_time']  # 视频发布时间
                        aweme_comment_count = aweme_info['statistics']['comment_count']  # 评论数
                        aweme_digg_count = aweme_info['statistics']['digg_count']  # 点赞数
                        aweme_download_count = aweme_info['statistics']['download_count']  # 下载数
                        aweme_forward_count = aweme_info['statistics']['forward_count']
                        aweme_share_count = aweme_info['statistics']['share_count']  # 转发数
                        aweme_play_music = aweme_info['music']['play_url']['uri']  # 背景音乐
                        aweme_owner_nickname = aweme_info['music']['owner_nickname']  # 背景音乐名称
                        aweme_origin_cover = aweme_info['video']['origin_cover']['url_list'][0]  # 默认图片 视频默认显示
                        aweme_cover = aweme_info['video']['cover']['url_list'][0]  # 默认图片 视频中
                        # endregion

                        sSql = "INSERT INTO dy_aweme_bc(uid, aweme_id, str_desc, share_url, create_time, comment_count, digg_count, download_count, forward_count, share_count, play_music,owner_nickname,origin_cover,cover,sType) " \
                               "VALUES ('{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, '{}','{}','{}','{}','{}')".format(
                            aweme_uid, aweme_id, aweme_desc, aweme_share_url, aweme_create_time, aweme_comment_count,
                            aweme_digg_count, aweme_download_count, aweme_forward_count, aweme_share_count,
                            aweme_play_music, aweme_owner_nickname, aweme_origin_cover, aweme_cover, '综合1'
                        )

                        print(sSql)
                        cursor.execute(sSql)
                        conn.commit()
                    except Exception as e:
                        print('*' * 1000, e, 'aweme/v1/general/search/single/aweme')
                    # region 发布视频人信息
                    try:
                        user_uid = user_info['uid']  # 用户id
                        user_id = user_info.get('unique_id') if user_info.get('unique_id') else ""  # 抖音号
                        user_name = user_info['nickname']  # 用户名
                        user_birthday = user_info.get('birthday') if user_info.get('birthday') else ""  # 生日
                        user_aweme_count = user_info['aweme_count']  # 作品数
                        user_favoriting_count = user_info['favoriting_count']  # 喜欢数
                        user_follower_count = user_info['follower_count']  # 粉丝
                        user_following_count = user_info['following_count']  # 关注
                        user_total_favorited = user_info['total_favorited']  # 获赞数
                        user_gender = user_info['gender']  # 性别
                        user_signature = user_info['signature']  # 个性签名
                        # endregion

                        sSql = "INSERT INTO dy_user_bc(uid, user_id, user_name, birthday, aweme_count, favoriting_count, follower_count, following_count, total_favorited, user_gender, signature, sType) " \
                               " VALUES ('{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, '{}', '{}')".format(
                            user_uid, user_id, user_name, user_birthday, user_aweme_count, user_favoriting_count,
                            user_follower_count, user_following_count, user_total_favorited, user_gender,
                            user_signature, '综合1'
                        )

                        print(sSql)
                        cursor.execute(sSql)
                        conn.commit()
                    except Exception as e:
                        print('*' * 1000, e, 'aweme/v1/general/search/single/user')

        except Exception as e:
            print(e.args, '     single')

    # 通过抓包软包软件获取请求的接口
    # https://aweme-hl.snssdk.com/aweme/v1/user/?
    if 'aweme/v1/user/' in flow.request.url:
        # 数据的解析
        try:
            user = json.loads(flow.response.text)['user']
            # print(user)
            uid = user['uid']  # 用户id
            user_id = user['unique_id']  # 抖音号
            user_name = user['nickname']  # 用户名
            birthday = user.get('birthday') if user.get('birthday') else ""  # 生日
            aweme_count = user['aweme_count']  # 作品数
            favoriting_count = user['favoriting_count']  # 喜欢数
            follower_count = user['follower_count']  # 粉丝
            following_count = user['following_count']  # 关注
            total_favorited = user['total_favorited']  # 获赞数
            user_gender = user['gender']  # 性别
            signature = user['signature']  # 个性签名

            user_sql = "INSERT INTO dy_user_bc(uid,user_id,user_name,birthday,aweme_count,favoriting_count,follower_count,following_count,total_favorited,user_gender,signature, sType) VALUES('" + str(
                uid) + "','" + str(user_id) + "','" + str(user_name) + "','" + str(birthday) + "','" + str(
                aweme_count) + "','" + str(favoriting_count) + "','" + str(follower_count) + "','" + str(
                following_count) + "','" + str(total_favorited) + "','" + str(user_gender) + "','" + str(
                signature) + "','综合')"

            print(user_sql)
            cursor.execute(user_sql)
            conn.commit()
        except Exception as e:
            print('*' * 1000, e, 'aweme/v1/user/' )

    # https://aweme-hl.snssdk.com/aweme/v1/aweme/post/?source=0&max_cursor=0&sec_user_id=MS4wLjABAAAA2TqSbvtDgSsNOsW2TF7Hw5gqpANb48K9uQwctweMRNw&count=20&retry_type=no_retry&iid=93690127200&device_id=68731854608&ac=wifi&channel=update
    if 'aweme/v1/aweme/post/' in flow.request.url:
        for aweme in json.loads(flow.response.text)['aweme_list']:
            try:
                uid = aweme['author_user_id']  # 用户编号
                aweme_id = aweme['aweme_id']  # 视频id
                desc = aweme['desc']  # 视频标题
                share_url = aweme['share_url']  # 视频地址
                create_time = aweme['create_time']  # 视频发布时间
                comment_count = aweme['statistics']['comment_count']  # 评论数
                digg_count = aweme['statistics']['digg_count']  # 点赞数
                download_count = aweme['statistics']['download_count']  # 下载数
                forward_count = aweme['statistics']['forward_count']
                share_count = aweme['statistics']['share_count']  # 转发数
                play_music = aweme_info['music']['play_url']['uri']  # 背景音乐
                owner_nickname = aweme_info['music']['owner_nickname']  # 背景音乐名称
                origin_cover = aweme_info['video']['origin_cover']['url_list'][0]  # 默认图片 视频默认显示
                cover = aweme_info['video']['cover']['url_list'][0]  # 默认图片 视频中

                aweme_sql = "insert into dy_aweme_bc(uid,aweme_id,str_desc,share_url,create_time,comment_count,digg_count,download_count,forward_count,share_count,play_music,owner_nickname,origin_cover,cover,sType) values "
                aweme_sql += " ('%s','%s','%s','%s','%s',%s,%s,%s,%s,%s,'%s','%s','%s','%s','%s')" % (
                    uid,
                    aweme_id,
                    desc,
                    share_url,
                    create_time,
                    comment_count,
                    digg_count,
                    download_count,
                    forward_count,
                    share_count,
                    play_music,
                    owner_nickname,
                    origin_cover,
                    cover,
                    '综合'
                )
                print(aweme_sql)
                cursor.execute(aweme_sql)
                conn.commit()
            except Exception as e:
                print("*"*1000, e, 'aweme/v1/aweme/post/')

    if '/aweme/v2/comment/list/' in flow.request.url:
        for comment in json.loads(flow.response.text)['comments']:
            # region 评论信息
            try:
                cid = comment['cid']  # 评论id
                aweme_id = comment['aweme_id']  # 视频id
                create_time = comment['create_time']  # 评论时间
                digg_count = comment['digg_count']  # 喜欢数
                reply_comment_total = comment['reply_comment_total']  # 回复数
                status = comment['status']  # 评论状态
                stick_position = comment['stick_position']  # 是否置顶
                text = comment['text']  # 评论内容
                user_nickname = comment['user']['nickname']  # 用户名称
                user_uid = comment['user']['uid']  # 用户id
                is_author_digged = comment['is_author_digged']
                reply_id = comment['reply_id']
                reply_to_reply_id = comment['reply_to_reply_id']
                user_digged = comment['user_digged']
                # endregion

                # region 评论用户信息
                comment_user = comment['user']
                user_avatar_168x168 = comment_user['avatar_168x168']['url_list'][0]  # 头像168*168
                user_avatar_300x300 = comment_user['avatar_300x300']['url_list'][0]  # 头像300*300
                user_avatar_larger = comment_user['avatar_larger']['url_list'][0]  # 头像原图
                user_avatar_uri = comment_user['avatar_uri']  # 头像id
                user_birthday = comment_user.get('birthday') if comment_user.get('birthday') else ""  # 评论人生日
                user_nickname = comment_user['nickname']  # 评论人名称
                user_signature = comment_user['signature']  # 评论人签名
                user_gender = comment_user['gender']  # 评论人性别
                user_uid = comment_user['uid']  # 评论人ID
                user_city = comment_user.get('city') if comment_user.get('city') else ""
                # endregion
                sSql = "insert into dy_comments_bc(cid,aweme_id,create_time,digg_count,reply_comment_total,status,stick_position,text,user_nickname,user_uid,is_author_digged,reply_id,reply_to_reply_id,user_digged" \
                       ",user_avatar_168x168,user_avatar_300x300,user_avatar_larger,user_avatar_uri,user_birthday,user_signature,user_gender,user_city,sType) values " \
                       "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s','%s','%s'" \
                       ",'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                           cid, aweme_id, create_time, digg_count, reply_comment_total, status, stick_position, text,
                           user_nickname, user_uid, is_author_digged, reply_id, reply_to_reply_id, user_digged
                           , user_avatar_168x168, user_avatar_300x300, user_avatar_larger, user_avatar_uri, user_birthday,
                           user_signature, user_gender, user_city, '综合'
                       )
                print(sSql)
                cursor.execute(sSql)
                conn.commit()
            except Exception as e:
                print('*'*1000, e, '/aweme/v2/comment/list/')
