import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, page_url, html_content):
        """
        解析该页面
        :param page_url:
        :param html_content:
        :return:
        """
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        """
        获取该页面中所有的符合检验规则的url
        :param page_url:
        :param soup:
        :return:
        """
        # 新的带爬取的url集合
        new_urls = set()
        # 获取所有符合检验规则的url
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            new_url = link['href']
            # 将相对路径的url拼接成绝对路径的url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        """
        整合页面的数据
        :param page_url:
        :param soup:
        :return:
        """
        # 该页面整合的数据
        res_data = {'url': page_url}

        """
        获取爬取页面的标题
        <dd class="lemmaWgt-lemmaTitle-title">
        <h1 >Python</h1>
        """
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        gettitle= title_node.get_text()
        res_data['title'] = gettitle.strip('\n')

        """
        获取爬取页面的概要
        <div class="para" label-module="para">
        吴芮（约公元前241年—公元前201年），是
        秦汉交替时期的
        百越
        部落
        领袖，江西历史上第一个有明确记载的杰出人物。南昌城赣江岸边的
        滕王阁
        第四楼，有一幅巨大的江西历史文化名人壁画。在这些杰出人物中，鄱阳县人吴芮居第一。
        他是第一个响应秦末农民起义的秦吏，项羽分封诸侯，吴芮被封为衡山王；
        &nbsp;
        汉朝建立，改封为长沙王。卒于公元前201年，谥“文王”。</div>
        """




        summary_node = soup.find('div', class_='para')
        gettitle = summary_node.get_text()#得到class=summary文本内容
        p = re.compile('\n\[.*?\]')
        c = re.compile('\（.*?\）')
        q = re.compile('\(.*?\)')
        n = re.compile('\n')
        k = re.compile('&nbsp')
        v = re.compile('\[.*?\]')
        gettitle1 = gettitle.replace("\n。", "")
        gettitle18 = gettitle1.replace("\n，", ",")
        gettitle19 = gettitle18.replace("\n、", "、")
        gettitle22 = gettitle19.replace("；\n", "；")
        gettitle23 = p.sub('', gettitle22, 10)
        gettitle24 = c.sub('', gettitle23, 10)
        gettitle25 = q.sub('', gettitle24, 10)
        gettitle26 = n.sub('', gettitle25, 10)
        gettitle27 = k.sub('', gettitle26, 10)
        gettitle28 = v.sub('', gettitle27, 10)
        cd = len(gettitle28)
        if cd>200:
            res_data['if'] = "大于200"
        else:
            res_data['if'] = "小于200"
        res_data['summary'] = gettitle28.strip('\n')
        res_data['len'] = cd#统计数字，需要的话可以 添加在html_outputer.py中，倒数第二行


        tag_list= soup.find('span',class_='taglist')
        gettaglist = tag_list.get_text()
        gettaglist1= gettaglist.strip('\n')
        res_data['tag']=gettaglist1
        # tag = "科学百科信息科学分类"
        # if gettaglist1== tag:
        #     print("true")
        return res_data
        # else:
        #     return

        # root_tag = '软件'
        # taglist1=str(res_data['taglist'])
        # a = root_tag.encode('gb2312')
        # b = taglist1.encode('gb2312')
        # print(a,b)
        # if a==b:
        #     print('t')
        # else:
        #     print('false')
        #     print(str(res_data['taglist']))

        # if res_data['taglist'] == root_tag:
        #     return res_data
        # else:
        #     print('这个名词不是%s分类的' % (root_tag))
