from pprint import pprint
import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password = hashed_password

    def info(self):
        print('\n' + ('='*30) + '\n\t< 회원 정보 >\n' + ('='*30))
        print(
            f'회원의 이름\t: {self.name}\n아이디\t\t: {self.username}\n')


class Post(Member):
    def __init__(self, title, content, author):
        super().__init__(author.username, author.name, author.password)
        self.title = title
        self.content = content
        self.author = author.username

    def info2(self):
        print('\n' + ('='*30) + '\n\t  < 게시물 >\n' + ('='*30))
        print(
            f'게시물 제목\t: {self.title}\n게시물 내용\t: {self.content}\n작성자\t\t: {self.author}')


def member_input():
    member = Member(input('\n1. 당신의 이름을 입력해주세요.\n: '), input(
        '\n2. 당신의 아이디를 입력해주세요.\n: '), input('\n3. 당신의 비밀번호를 설정해 주세요.\n: '))
    return member


def members_append(member):
    members.append({'name': member.name, 'username': member.username,
                    'password': member.password})


def post_input(member):
    post = Post(input('\n게시물 제목: '), input('게시물 내용: '), member)
    return post


def posts_append(post):
    posts.append({'title': post.title, 'content': post.content,
                  'author': post.author})


members = []
posts = []

# 각 회원 당 3개의 게시물 만들기
for i in range(3):
    print('\n' + '-'*10 + '[ 회원 가입 ]' + '-'*10 + '\n(회원' + str(i+1) + ')')
    # 회원 정보 저장
    member = member_input()
    # 회원 정보 members 리스트에 추가
    members_append(member)

    for j in range(3):
        print('\n' + '-'*10 + '< 게시물 작성하기 >' + '-'*10 +
              '\n\n(회원' + str(i+1) + '의 게시물' + str(j+1) + ')')
        # 해당 요소 회원의 게시물 작성
        post = post_input(member)
        # 작성된 게시물 posts 리스트에 추가
        posts_append(post)

print('\n' + ('='*50) + '\n\t\t  회원 이름 목록\n' + ('='*50))
# 리스트에 저장된 회원들의 이름만 출력
for i, x in enumerate(members, 1):
    name = x['name']
    print('회원' + str(i) + ' ' + name)

while True:
    try:
        num = int(
            input('\n특정 회원이 작성한 게시물의 제목을 확인하고 싶으면 해당 회원 번호를 입력하세요.\n: 회원1 -> "1" 입력\n: '))

        if num == int(num):
            특정유저 = members[num-1]['username']

            print('\n' + ('='*50) + '\n\t특정 유저가 작성한 게시물 제목입니다.\n' + ('='*50))

            for i in posts:
                if 특정유저 in i['author']:
                    pprint(i['title'])
            break

    except ValueError:
        print('\n회원 목록에 있는 회원 번호를 입력하세요.')

    except IndexError:
        print('\n회원 목록에 있는 회원 번호를 입력하세요.')


while True:
    특정단어 = input(
        '\n특정 단어가 포함된 게시물의 제목을 확인하고 싶으면 특정 단어를 입력하세요.\n: 특정 단어 입력\n: ')

    if 특정단어 in i['content']:
        print('\n' + ('='*50) + '\n\t특정 단어가 포함된 게시물 제목입니다.\n' + ('='*50))

        for i in posts:
            if 특정단어 in i['content']:
                pprint(i['title'])
        break
    else:
        print('\n입력하신 단어는 게시물 내용에 없습니다.. 다시 입력하세요.')

print('\n소셜 미디어를 종료함니다.\n')
