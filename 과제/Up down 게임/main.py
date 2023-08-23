import random


def number_check():
    while True:
        try:
            num = int(
                input('\n► 비교할 숫자를 입력해주세요. ( 1 ~ 100 )\n: [일시정지] = 아무 문자 입력\n: '))
            if num < 1 or num > 100:
                print("\n" + ('-' * 50) +
                      "\n\t\t    <정보>\n\n숫자 범위는 1 ~ 100까지 입니다. 다시 입력하세요.\n" + ('-' * 50) + '\n\n')

            if num >= 1 and num <= 100:
                return num

        except ValueError:

            print("\n" + ('-' * 40) +
                  "\n\t\t<정보>\n\n   게임은 문자말고 숫자를 입력해주세요.\n" + ('-' * 40) + '\n')
            while True:
                ans = input(
                    "\n[일시정지] 게임을 처음부터 다시 하시겠습니까? ( 돌아가기 / 다시하기 / 종료하기 )\n" + ('=' * 40) + "\n\t\t⌜주의⌟\n'종료하기' 입력 시 저장은 불가능합니다.\n" + ('=' * 40) + "\n: ").strip()

                if ans == '돌아가기':
                    break

                if ans == '다시하기':
                    print('\n게임을 다시 시작합니다.')
                    global random_number, player_number, count
                    player_name = input('\n닉네임을 입력해주세요!!\n: ')
                    win = '실패'
                    player_list.append(
                        {'name': player_name, 'count': count, 'win': win})
                    intro()
                    count = 0
                    player_number = 0
                    random_number = random.randint(1, 100)
                    break

                if ans == '종료하기':
                    return ans

                if ans not in ('돌아가기', '다시하기', '종료하기'):
                    print(
                        "\n" + ('-' * 40) + "\n\t\t<정보>\n\n질문에 ( 돌아가기 / 다시하기 / 종료하기 )로 대답해주세요.\n" + ('-' * 40) + '\n\n')
                    pass


count = 0
player_list = [{'name': '개발자', 'count': 23, 'win': '성공!'}]


def intro():
    print('\n' + ('='*60) + '\n' + '\t\t       업-다운 게임\n' + ('='*60) + '\n')
    for i, x in enumerate(player_list, 1):
        name = x['name']
        count = x['count']
        win = x['win']
        print(i, f'닉네밍: {name}     \t시도 횟수: {count} \t   게임 클리어: {win}')


intro()
random_number = random.randint(1, 100)
player_number = number_check()

while True:
    try:
        if player_number > random_number:
            print('\n' + ('=' * 15) + f'\n"{player_number}" 다운!!\n')
            count += 1
            print("시도한 횟수 : " + str(count) + '\n' + ('=' * 15) + '\n')
            player_number = number_check()

        if player_number < random_number:
            print('\n' + ('=' * 15) + f'\n"{player_number}" 업!!\n')
            count += 1
            print("시도한 횟수 : " + str(count) + '\n' + ('=' * 15) + '\n')
            player_number = number_check()

        if player_number == random_number:
            print('\n' + ('✶' * 30) +
                  f'\n야호~!! 숫자를 찾았다!!!!!!!\n정답은 "{player_number}" !!!\n')
            count += 1
            print("시도한 횟수 : " + str(count) + '\n' +
                  ('✶' * 30) + '\n\n')
            player_name = input('축하합니다~!\n닉네임을 입력해주세요!!\n: ')
            win = '성공!'
            player_list.append(
                {'name': player_name, 'count': count, 'win': win})

            while True:
                ans = input(
                    f"\n{player_name}님!! 게임을 다시 하시겠습니까? ( 다시하기 / 종료하기 )\n: ").strip()

                if ans == '다시하기':
                    print('\n게임을 다시 시작합니다.')
                    intro()

                    count = 0
                    random_number = random.randint(1, 100)
                    player_number = number_check()
                    break

                if ans == '종료하기':
                    break

                if ans not in ('다시하기', '종료하기'):
                    print(
                        "\n" + ('-' * 40) + "\n\t\t<정보>\n\n질문에 ( 다시하기 / 종료하기 )로 대답해주세요.\n" + ('-' * 40) + '\n\n')
                    pass

            if ans == '종료하기':
                print('\n게임을 종료함니다.')
                break
            else:
                pass

    except TypeError:
        print('\n게임을 종료합니다.')
        break
