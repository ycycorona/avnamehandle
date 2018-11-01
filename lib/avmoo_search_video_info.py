import requests as request
import config.config_params as config_params
from config.proxy import Proxy
from config.request_header import RequestHeader
from pyquery import PyQuery as pq

proxy = Proxy(config_params.proxy_url)
request_header = RequestHeader(config_params.headers)


# 获取影片详情地址
def find_video_href(url) -> str:
    return _find_video_href(_re_search_video(url))


# 获取影片全名
def find_video_fullname(url) -> str:
    return _find_video_fullname(_re_search_video(url))


# _获取影片全名
def _find_video_fullname(html) -> str:
    doc = pq(html)
    target_doc = doc('#waterfall .item').eq(0)

    video_id_selector = target_doc('.photo-info span date:first-of-type')
    video_name_selector = target_doc('.photo-info span')

    if len(video_id_selector) and len(video_id_selector):
        video_id = video_id_selector.text()  # [0].text  # 番号
        video_name = video_name_selector.contents()[0].encode('utf-8').decode('utf-8')  # 片名
    else:
        video_id = ''
        video_name = ''
    return video_id + ' ' + video_name


# _获取影片详情地址
def _find_video_href(html) -> str:
    doc = pq(html)
    target_doc = doc('#waterfall .item').eq(0)
    video_detail_selector = target_doc('.movie-box')
    if len(video_detail_selector):
        video_detail_href = video_detail_selector.attr('href')  # 详情地址
    else:
        video_detail_href = ''
    return video_detail_href


# 搜索影片
def _re_search_video(url) -> str:
    res = request.get(url, headers=request_header.get_header(), timeout=15, proxies=proxy.get_proxy())
    res.encoding = 'utf-8'
    # with open('find_video_href.html', 'w+', encoding='utf-8') as file:
    #     file.write(res.text)
    return res.text


def _is_invalid_html(html) -> bool:
    doc = pq(html)
    return not bool(len(doc('.alert.alert-danger')))


if __name__ == '__main__':
    def test_re_search_video():
        url = 'https://avmoo.net/cn/search/TKI-089'
        fvh_res = find_video_fullname(url)
        print(fvh_res)

    def test_find_video_fullname():
        url = 'https://avmoo.net/cn/search/DAVK-011'

        res = find_video_fullname(url)
        pass

    def test_find_video_href():
        with open('find_video_href_error.html', 'r', encoding='utf-8') as file:
            file_str = file.read()
        res = _find_video_href(file_str)
        pass

    def test_is_invalid_html():
        with open('find_video_href_error.html', 'r', encoding='utf-8') as file:
            file_str = file.read()
        res = _is_invalid_html(file_str)
        pass

    test_find_video_fullname()

    print('end')
