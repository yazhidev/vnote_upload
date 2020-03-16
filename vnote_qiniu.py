from qiniu import Auth, put_file, etag
import qiniu.config
import re
import time

def get_time_str():
    now = time.time()
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y%m%d_%H%M%S", timeArray)
    return otherStyleTime

def get_file_name_from_path(path):
    array = path.split("/")
    if len(array) > 1:
        return array[len(array) - 1]
    else:
        return ""

def upload_to_qiniu(path, name):
    print("")
    #需要填写你的 Access Key 和 Secret Key
    access_key = '0Lm6gzT6hHbXVS_uJ-VHkoIpx204Oxk8xJJbi8T5'
    secret_key = 'KWqXDtRSOPsH3VLRq5EOxdiaw0zp22Tymmbp9TAB'
    #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'yazhidev'
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, name, 3600)
    ret, info = put_file(token, name, path)
    print(info)

def find_md_img_path(path):
    position = path.find("](", 0)
    if position >= 0:
        return path[position+2:len(path)-1]
    else:
        return ""

def scan_md_file(path):
    f = open(path)  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        if len(line.strip()) > 0:
            print(line.strip())
            # \!\[. *\]\(.* \)
            # \!\[(.* ?)\)
            resultArray = re.findall("!\[. *\]\(.* \)", line.strip())
            # print("result: ")
            print(resultArray)
            # if len(resultArray) > 0:
                #找到了图片
                # for md_img in resultArray:
                    # print(find_md_img_path(md_img))

        # print()  # 在 Python 3中使用
        line = f.readline()
    f.close()

# get_time_str()
md_path = '/Users/yazhi/cloud/vnote_notebooks/dev/工具/Vnote七牛图床.md'
# path = '/Users/yazhi/cloud/vnote_qinu/WechatIMG5.jpeg'
# file_name = get_file_name_from_path(path)
# if len(file_name) > 0:
#     upload_name = get_time_str() + "_" + file_name
#     upload_to_qiniu(path, upload_name)

scan_md_file(md_path)

resultArray = re.findall(r'(.*?)\)', "d5./;.sd] j)k56jfs)./jfis54")
# print(resultArray)

# print(get_file_name_from_path("/1ya/123/133/124/ahte.png"))
# print(get_file_name_from_path(""))
