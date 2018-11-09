from bs4 import BeautifulSoup
import requests
#import datetime
#import time
import db_handler
import parser

#게시판 URL
notice_board_URL = "http://portal.koreatech.ac.kr/ctt/bb/bulletin?b=14&dm=l&px=&sc=title&sw=근로장학생&csdt=&cedt=&cuid="


#게시글 베이스 URL
notice_URL = "http://portal.koreatech.ac.kr/ctt/bb/bulletin?b=14&ls=20&ln=1&dm=r&p="


#잡다한 변수들
"""
counter = 0 #전반적인 카운터 (보통 사용 전 or 후 0으로 초기화.)
counter_0 = 0 #게시글 목록 추출, DB 조회 작업시 사용하는 카운터
counter_1 = 2 #게시글 목록 추출, 시 사용하는 카운터
counter_2 = 0 #DB 작업시 사용하는 카운터
counter_3 = 0 #read_db()에서 사용되는 카운터
prog_stat = True #True일 동안에 계속 프로그램이 돌게끔 while 문 설계
job_finished = False #각 작업시 완료 여부 판단하는 변수
second = 7 #잠자기 초 정의
"""


print("\n\n[INFO] 한기대 근장알리미 ver.0.3b by.pangin\n\n")

#Make it Run!
#print(telegram_chat_id)
print("\n[INFO] 게시판을 불러오는 중...\n")
#print(repr(notice_board_URL))
request = requests.get(notice_board_URL)
request.encoding = "utf-8"
notice_board = request.text
print("\n[INFO] 파싱하는 중...\n")
soup = BeautifulSoup(notice_board, "html.parser")
"""print("\nUnescaping...\n")
notice_board.unescape(soup)"""  #Problem with Function
posts = soup.find_all("span")
span_count = len(posts)
title_count = int(span_count / 3)
parser.parse_post_list(posts, title_count)
post_numbers = parser.parse_num_list(soup)
parser.parse_title_list(posts)
db_handler.search_db(post_numbers)
"""
print("\n[INFO] " + str(second) + "초 대기.\n")
time.sleep(second)
"""