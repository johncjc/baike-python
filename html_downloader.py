import urllib.request
import request

"""
Html下载器
"""


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        headers = {'User-Agent': user_agent}
        """
        下载该页面
        :param url:
        :return:
        """
        if url is None:
            return None
        # 打开一个url,返回一个 http.client.HTTPResponse
        response = urllib.request.urlopen(url,timeout=1)
        # 若请求失败
        if response.getcode() != 200:
            return None
        return response.read()
