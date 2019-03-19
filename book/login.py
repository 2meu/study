import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

## 아톰에서 파이썬 실행 시 스크립트 한글 깨짐 해결 코드
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


USER = 'zlslsp54'
PASS = 'eodgus54'

# 세션 시작하기
session = requests.session()
#로그인하기
login_info = {
    "m_id": USER,
    "m_passwd": PASS
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

# 마이페이지에 접근하기
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기

soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").string
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지 = ", mileage)
print("이코인 = ", ecoin)
