import os
import requests
import pytz
from datetime import datetime


TIL_WEBHOOK_URL = os.environ.get('TIL_WEBHOOK_URL')

def post_message(message):
    requests.post(TIL_WEBHOOK_URL, json={"text": message})

kst = pytz.timezone("Asia/Seoul")
date_string = datetime.now(kst).strftime("%Y-%m-%d")
TIL_NOTICE = f"""
📖 {date_string} 스터디 리마인더 📖
<!channel> 오늘은 스터디가 진행되는 날입니다!
다음과 같은 포맷으로 스레드를 만든 뒤, 스터디를 진행해주세요.

EX] {date_string} 성준, 석호 `라이브코딩` 스터디 스레드

오늘도 화이팅입니다. 😀
"""

if __name__ == "__main__":
    post_message(TIL_NOTICE)