import threading
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import json
import requests
import csv
import time
import argparse


class Crawler(object):
    def __init__(self, search_content, area):
        self.search_content = search_content
        self.area_code = self.get_area_code()[area]

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
        self.file = f"51job_{search_content}_{time.strftime('%Y%m%d-%H%M%S', time.localtime())}.csv"
        self.write_csv_header()
        print(f'你搜索的是{area}(城市码{self.area_code})的{search_content}')

    def write_csv_header(self):
        data = ('职位名称', '职位详情', '公司名', '公司类型', '公司主营', '公司详情', '薪资', '工作地点', '更新日期',
                '发布日期', '招聘人数', '学历要求', '工作经验', '福利')
        write_csv(self.file, data, mode='w', encoding='utf-8-sig')

    def get_area_code(self):
        url = 'https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js'
        r = requests.get(url)
        city_dict = json.loads(r.text.split('=')[1].rstrip(';'))
        city_dict = {v: k for k, v in city_dict.items()}
        return city_dict

    def get_job_json(self, page):
        search_keyword = quote_plus(quote_plus(self.search_content))  # urlencode
        url = f"https://search.51job.com/list/{self.area_code},000000,0000,00,9,99,{search_keyword},2,{page}.html"
        html = requests.get(url, headers=self.header).text
        bs = BeautifulSoup(html, 'lxml')
        script_tags = bs.find_all('script', {'type': 'text/javascript'})
        for script in script_tags:
            if script.string is not None:
                result_orig_str = script.string.strip('\r\nwindow.__SEARCH_RESULT__ = ')
                result_orig_json = json.loads(result_orig_str)
                result = result_orig_json['engine_search_result']
        if page == 1:
            print(f'开始访问第{page}页...并取得最大页数')
            max_page = result_orig_json['total_page']
            return result, max_page
        else:
            print(f'开始访问第{page}页...')
            return result

    def get_job(self, json_content, page):
        # print(json_content)
        company_name = json_content['company_name']
        company_kind = json_content['companytype_text']
        company_major = json_content['companyind_text']
        salary = json_content['providesalary_text']
        location = json_content['workarea_text']
        update_time = json_content['updatedate']
        post_time = json_content['issuedate']
        people_numba = json_content['attribute_text'][-1]
        educated_stat = json_content['attribute_text'][-2]
        if '经验' in json_content['attribute_text'][1]:
            work_exp = json_content['attribute_text'][1]
        else:
            work_exp = None  # 不然就是上一个单位的工作经验
        benefit = json_content['jobwelf']
        job_name = json_content['job_name']
        job_detail_link = json_content['job_href']
        company_detail_link = json_content['company_href']
        print(f'正在读取第{page}页的 {company_name} 的 {job_name} 工作详情...')
        job_duty = self.get_job_detail(job_detail_link)
        company_info = self.get_company_detail(company_detail_link)
        return (job_name, ''.join(job_duty), company_name, company_kind, company_major, company_info, salary,
                location, update_time, post_time, people_numba, educated_stat, work_exp, benefit)

    def get_job_detail(self, detail_link):
        duty = []
        try:
            info = requests.get(detail_link, headers=self.header).content
        except ConnectionError:
            return None
        bs = BeautifulSoup(info, 'lxml')
        if (position_detail := bs.find('div', class_='bmsg job_msg inbox')) is not None:
            position_detail_list = position_detail.get_text(strip=True).split()[1:-1]  # 最后有一个微信分享 最前有一个职责
            for index, content in enumerate(position_detail_list):
                if content.startswith('职能类别'):
                    continue
                else:
                    duty.append(content)
        return duty

    def get_company_detail(self, detail_link):
        try:
            info = requests.get(detail_link, headers=self.header).content
        except ConnectionError:
            return None
        bs = BeautifulSoup(info, 'lxml')
        if (detail_div := bs.find('div', class_='con_txt')) is not None:
            detail = detail_div.get_text()
        else:
            detail = None
        return detail

    def write_job(self, info):
        write_csv(self.file, info)

    def get_save(self, current_page, json_content):
        for i in range(0, len(json_content)):
            job_info = self.get_job(json_content[i], current_page)
            self.write_job(job_info)

    def thread_get_save(self, worker):
        print(f'启动进程{threading.currentThread().getName()}')
        for page in worker:
            if page == 1:
                continue
            json_content = self.get_job_json(page)
            self.get_save(page, json_content)

    def run(self):
        total_page = 3
        current_page = 1
        while current_page <= int(total_page):
            if current_page == 1:
                (json_content, total_page) = self.get_job_json(current_page)
                print(f'一共{total_page}页')
            else:
                json_content = self.get_job_json(current_page)
            self.get_save(current_page, json_content)
            current_page += 1

    def run_thread(self):
        current_page = 1
        (json_content, total_page) = self.get_job_json(current_page)
        print(f'一共{total_page}页')
        threading.Thread(target=self.get_save, args=(current_page, json_content)).start()
        workers = self.thread_worker(total_page)
        for worker in workers:
            thread_name = worker[0]
            threading.Thread(target=self.thread_get_save, name=thread_name, args=[worker]).start()

    def thread_worker(self, total_page):
        worker1 = []
        worker2 = []
        worker3 = []
        worker4 = []
        for i in range(1, int(total_page) + 1):
            list_name = f'worker{str(i % 4 + 1)}'
            eval(list_name).append(i)
        return [worker2, worker3, worker4, worker1]


def write_csv(file, data, mode='a+', encoding='utf-8-sig'):
    with open(file, mode=mode, encoding=encoding, newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='搜一下去哪里搬砖')
    parser.add_argument('-j', '--job', help='工作名', type=str, default='')
    parser.add_argument('-c', '--city', help='城市', type=str, default='上海')
    args = parser.parse_args()

    if args.job == '':
        args.job = input('你要搬啥砖:')
    if args.city == '上海':
        if input('你的城市是默认值上海,要不要换一下? Y/n:').upper() == 'Y':
            args.city = input('那要去哪儿搬砖:')

    taobao = Crawler(args.job, args.city)
    taobao.run_thread()
