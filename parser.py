def parse_num_list():
    global soup
    global counter
    global job_finished
    global post_numbers
    global post_number
    post_numbers = soup.find_all("td", class_="bc-s-post_seq")
    numbers_count = len(post_numbers)
    print("\n[INFO] 게시글 번호 파싱 작업 시작.\n")
    while not job_finished:
        print("\n[INFO] " + str(counter + 1) + "번째 프로세스")
        post_number = str(post_numbers[counter])
        print("\n[INFO] 추출 전: " + str(post_number))
        post_number = post_number.replace("<td class=\"bc-s-post_seq\">", "")
        post_number = post_number.replace("\n                    ", "")
        post_number = post_number.replace("        </td>", "")
        post_number = post_number.replace("\r", "")
        print("\n[INFO] 추출 후: " + str(post_number) + "\n")
        post_numbers[counter] = post_number
        if counter == (numbers_count - 1):
            print("\n[INFO] 게시글 번호 파싱 작업 완료.\n")
            job_finished = True
        else:
            counter += 1
    counter = 0
    job_finished = False

def parse_title_list():
    global job_finished
    global post_title
    global counter
    global posts
    global posts_count
    print("\n[INFO] 게시글 제목 파싱 작업 시작\n")
    posts_count = len(posts)
    while not job_finished:
        print("\n[INFO] " + str(counter + 1) + "번째 프로세스")
        post_title = str(posts[counter])
        print("\n[INFO] 파싱 전 " + str(posts[counter]))
        post_title = post_title.replace("<span style=\"\" title=\"", "")
        post_title = post_title.replace("\">", "")
        post_title = post_title.replace("</span>", "")
        post_title = post_title[int(len(post_title) / 2):]
        print("\n[INFO] 파싱 후: " + str(post_title) + "\n")
        posts[counter] = post_title
        if counter == (posts_count - 1):
            print("\n[INFO] 게시글 제목 파싱 작업 완료.\n")
            job_finished = True
        else:
            counter += 1
    job_finished = False