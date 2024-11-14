import requests
from io import BytesIO, StringIO
from PIL import Image

if __name__ == '__main__':
    img_url = "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E5%A3%81%E7%BA%B8&step_word=&hs" \
              "=0&pn=2&spn=0&di=7308398814245683201&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8" \
              "&in=&cl=2&lm=-1&st=-1&cs=1203194706%2C2118846670&os=3045495621%2C71317&simid=3450163824%2C86973320" \
              "&adpicid=0&lpn=0&ln=1830&fr=&fmq=1526269427171_R&fm=&ic=0&s=undefined&hd=undefined&latest=undefined" \
              "&copyright=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=wallpaper&bdtype=0" \
              "&oriquery=&objurl=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2%2F5859e7ee330bb.jpg&fromurl=ippr_z2C" \
              "%24qAzdH3FAzdH3Fooo_z%26e3Botg9aaa_z%26e3Bv54AzdH3Fowssrwrj6_kt2_88b9ma_d_z%26e3Bip4s&gsm=1e&rpstart=0" \
              "&rpnum=0&islist=&querylist=&nojc=undefined&lid=6130229279147653830 "
    response = requests.get(img_url)
    f = BytesIO(response.content)
    print(response.status_code)
    print(response.text)
    # img = Image.open(f)
    # print(img.size)
