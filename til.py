import os
import requests
from datetime import datetime


TIL_WEBHOOK_URL = os.environ.get('TIL_WEBHOOK_URL')

def post_message(message):
    requests.post(TIL_WEBHOOK_URL, json={"text": message})

date_string = datetime.now().strftime("%Y-%m-%d")
TIL_NOTICE = f"""<!channel> 오늘의 TIL을 공유할 시간입니다! 아래의 템플릿을 참고하여 작성해주세요.

**[템플릿]**

📆 {date_string}
⏰ 공부 시간
> h시간 m분

📚 공부한 내용
* 공부한 내용에 대해 간단히 정리해주세요.
* TIL을 정리한 링크를 공유해주셔도 좋습니다

💭 회고
* 오늘의 공부를 통해 느낀 점을 자유롭게 적어주세요.
"""

if __name__ == "__main__":
    post_message(TIL_NOTICE)
