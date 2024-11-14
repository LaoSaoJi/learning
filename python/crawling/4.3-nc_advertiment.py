import re
from typing import List

import requests

from douban import ask_url


if __name__ == '__main__':
    # 招行广告跳转链接
    url1 = "https://cmb-recruitment-mobile.paas.cmbchina.com/recommendList?qrCodeId=3C61ECB6-8B65-446C-A8EB" \
          "-E05FCE354031&recruitmentTypeId=670980EA-30B6-455A-93C2-5CD5258B8A36&orgId=100003"

    # 招行广告二跳链接
    url2 = "https://cmb-recruitment-mobile.paas.cmbchina.com/positionDetail/school?qrCodeId=3C61ECB6-8B65-446C-A8EB" \
           "-E05FCE354031&recommendType=2&recruitmentTypeId=670980EA-30B6-455A-93C2-5CD5258B8A36&publishId=D3C329C4" \
           "-C755-4801-92A2-29732703E6BA "
    
    # 百信银行春招广告链接
    url3 = "https://app.mokahr.com/campus-recruitment/aibank/118868#/"

    # 联想广告链接
    url4 = "https://talent.lenovo.com.cn/position?projectType=1"

    # r1 = ask_url(url1)
    # r2 = ask_url(url2)
    # r3 = ask_url(url3)
    r4 = ask_url(url4)
    print(r4.text)
