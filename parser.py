


def parse_num_list(soup):
    counter = 0
    job_finished = False
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
    return post_numbers


def parse_title_list(posts):
    job_finished = False
    counter = 0
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


def parse_post_list(posts, title_count):
    job_finished = False
    counter = 0
    counter_0 = 0
    counter_1 = 2
    print("\n[INFO] 게시글 목록 추출 작업 시작.\n")
    del posts[counter_0:counter_1]
    counter_0 = 1
    counter_1 = 3
    while not job_finished:
        print("\n[INFO] " + str(counter + 1) + "번째 프로세스")
        del posts[counter_0:counter_1]
        print("\n" + str(posts) + "\n")
        counter_0 += 1
        counter_1 += 1
        span_count = len(posts)
        if counter_0 > span_count:
            job_finished = True
            print("\n[INFO] " + "게시글 목록 추출 완료!\n[INFO] 추출된 게시글 수: " + str(title_count) + "\n")
        elif counter_1 > span_count:
            job_finished = True
            print("\n[INFO] " + "게시글 목록 추출 완료!\n[INFO] 추출된 게시글 수: " + str(title_count) + "\n")
        else:
            counter += 1

    #print(posts)