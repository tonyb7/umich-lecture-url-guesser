import requests
from concurrent.futures import ThreadPoolExecutor

g_seconds_in_two_days = 172800
g_seconds_in_five_days = 432000
g_seconds_in_week = 604800

g_seconds_spread = 7

g_original_url = 'http://s3.amazonaws.com/leccap.engin.umich.edu/media/nrl18ht1ep0is8dnb2n/1578491884-124-O-c23-13.mp4'
g_base_front = 'http://s3.amazonaws.com/leccap.engin.umich.edu/media/nrl18ht1ep0is8dnb2n/'
g_orig_time = 1578491884
g_base_back = '-O-c23-13.mp4'

# TODO this is terrible style but...
g_current_url_front = ''

def form_url_front(time):
    url_front = g_base_front + f"{time:010d}" + '-'
    return url_front

def form_url_back(code):
    url = g_current_url_front + f"{code:03d}" + g_base_back
    return url

def form_url(time, code):
    url = g_base_front + f"{time:010d}" + '-' + f"{code:03d}" + g_base_back
    return url

def check_head(url):
    r = requests.head(url)
    if (r.status_code < 400):
        print(url)

def guess(center_time):

    start_time = center_time - g_seconds_spread
    end_time = center_time + g_seconds_spread

    times = range(start_time, end_time)
    codes = range(0, 1000)

    url_fronts = []
    with ThreadPoolExecutor() as executor:
        url_fronts = executor.map(form_url_front, times)
    
    urls = []
    for url_front in url_fronts:
        global g_current_url_front
        g_current_url_front = url_front
        with ThreadPoolExecutor() as executor:
            full_urls = executor.map(form_url_back, codes)
        for url in full_urls:
            urls.append(url)

    # for url in urls:
    #     print(url)
    with ThreadPoolExecutor() as executor:
        executor.map(check_head, urls)

def guess_all():
    weeks_of_lecture = 7
    for week in range(weeks_of_lecture):
        wednesday_time = g_orig_time + ((week + 1) * g_seconds_in_week)
        monday_time = wednesday_time - g_seconds_in_two_days
        guess(monday_time)
        guess(wednesday_time)
    # guess(g_orig_time + (6 * g_seconds_in_week) - g_seconds_in_two_days)


if __name__ == '__main__':
    guess_all()
    # check_head(g_orig_time, 124)
    # check_head(1234, 123)
