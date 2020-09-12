import chromedriver_binary
from selenium import webdriver
import requests
import json
import datetime

#main class
class CsqrPost():
    def __init__(self,username, password, slack_api):
        self.username = username
        self.password = password
        self.slack_api = slack_api
        self.url = "https://www.c-sqr.net/login"
        #chrome driver -headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        #if you want debug 
        # self.driver = webdriver.Chrome()
    
    def main(self):
        driver = self.driver
        #Login window
        print("login window open")
        driver.get(self.url)
        username_box = driver.find_element_by_id("account")
        username_box.send_keys(self.username)
        password_box = driver.find_element_by_id("password")
        password_box.send_keys(self.password)
        submit_button = driver.find_elements_by_css_selector("button.p-public-form__login")[0]
        submit_button.submit()

        # ログイン後ページ取得
        if "https://www.c-sqr.net/" in driver.current_url:
            print("csqr open")
            element = driver.find_element_by_id("timeline_list")
            list2 = element.find_elements_by_css_selector('.p-timeline-box')

            # 投稿テキスト組み立て
            is_post = False

            now = datetime.datetime.now()
            title = now.strftime('%Y年%m月%d日%H時')

            text = title + 'のタイムライン\n\n'
            for item in list2:
                # 時間が見つからないときはスルー
                date = item.find_elements_by_css_selector('.c-updater__date')
                if len(date) == 0: 
                    continue
                dateStr = date[0].text
                # 新しいデータのみ取得
                if '秒前' in dateStr or '分前' in dateStr:
                    h2tag = item.find_element_by_tag_name('h2')
                    text += '■' + h2tag.text + '\n'
                    text += dateStr + '\n'
                    url = item.find_element_by_tag_name('a').get_attribute('href')
                    text += url + '\n\n'
                    # 投稿フラグ
                    is_post = True
            
            # 出欠アンケート
            if '出欠' in text or 'アンケート' or text:
                text = '<!channel> \n' + text
            
            # 送信
            if is_post:
                self.post(text)

            return text
    
    def post(self, text):
        # Slack api
        headers = {
            'Content-type': 'application/json',
        }
        data = json.dumps({'text': text})
        requests.post(self.slack_api, headers=headers, data=data)

    # destractor
    def __del__(self):
        print("del:driver")
        self.driver.quit()