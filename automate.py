import time
from selenium import webdriver


class Selenium:
    driver = None
    element = None

    def __init__(self):
        # https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.options
        options = webdriver.ChromeOptions()
        # ブラウザを立ち上げないで、ブラウザ操作すること。
        options.add_argument("--headless")
        # https://daily.belltail.jp/?p=2691
        options.add_argument("--no-sandbox")
        # http://chrome.half-moon.org/43.html#e25988df
        options.add_argument("--single-process")
        # https://developers.google.com/web/updates/2017/04/headless-chrome?hl=ja
        options.add_argument("--disable-gpu")
        # ウィンドウ幅設定
        options.add_argument("--window-size=1280x1696")
        # スクロールバーを表示しない
        options.add_argument("--hide-scrollbars")
        # ログ周り : https://qiita.com/grohiro/items/718239cdd36da42bd517#%E3%83%AD%E3%82%B0%E3%82%92%E5%87%BA%E3%81%99
        options.add_argument("--enable-logging")
        # ログ周り : https://qiita.com/grohiro/items/718239cdd36da42bd517#%E3%83%AD%E3%82%B0%E3%82%92%E5%87%BA%E3%81%99
        options.add_argument("--log-level=0")
        # ssh証明書周りのエラー回避
        options.add_argument("--ignore-certificate-errors")
        # https://daily.belltail.jp/?p=2691
        options.add_argument("--disable-dev-shm-usage")

        # LambdaのLayerを活用している。
        # Layerとは、Lambda内に含まれるサービス名で、重いファイルや共通で利用するファイルを配置する場所。
        # Lambdaとの紐付けを行うことで、紐づいたLambda関数ならば再利用可能。
        # Lambda関数実行時には、/opt/以下にファイルが配置される。
        options.binary_location = "/opt/headless/python/bin/headless-chromium"

        self.driver = webdriver.Chrome(
            executable_path="/opt/headless/python/bin/chromedriver",
            chrome_options=options
        )

    def access(self, url):
        self.driver.get(url)

    def stop(self, num):
        time.sleep(num)

    def quit(self):
        self.driver.quit()

    # スクリーンショットを撮影する。
    def saveScreenshot(self, filePath):
        self.driver.save_screenshot(filePath)
