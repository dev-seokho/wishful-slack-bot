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
😺 {date_string} TIL 리마인더 😺
<!channel> 오늘의 TIL을 공유할 시간입니다!

💭 구글폼 링크
- 공부한 내용에 대해 간단히 정리해주세요.
- TIL을 정리한 링크를 공유해주셔도 좋습니다.
- 성장을 위해 투자한 시간이 있다면 함께 작성해주세요.
- <https://docs.google.com/forms/d/e/1FAIpQLSddHG66sF7okeqFqYBliYYsoR6NdID3qpeLGs5-vwHGbey65Q/viewform|구글폼 작성하러 가기>

📋 구글시트 링크
- 위의 구글폼을 작성하시면, 자동으로 구글시트에 작성됩니다.
- 구성원들이 성장하고 있는지 함께 확인해주세요.
- <https://docs.google.com/spreadsheets/d/12t2ApDFbx6tt2j56Sw0_Fz61SgWgyO2mjWpffP0rkSk/edit?resourcekey=&gid=854817029#gid=854817029|TIL 기록 구글시트 열기>

구글폼 작성을 마쳤다면 ✅ 이모지를 달아주세요. 
"""

if __name__ == "__main__":
    post_message(TIL_NOTICE)