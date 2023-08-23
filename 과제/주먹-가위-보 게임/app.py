import random

rps_list = ['주먹(rock)', '가위(scissors)', '보(paper)']
random.shuffle(rps_list)
computer_rps = rps_list[0]


def player_selection():
    while True:
        rps = input(
            '\n► [ 주먹(rock) / 가위(scissors) / 보(paper) ] 중 하나를 입력해주세요. ( 영어도 가능 )\n: [일시정지] = "잠깐" 입력\n: ')

        if rps.lower() in ('rock', 'paper', 'scissors') or rps in ('주먹', '가위', '보'):
            return rps

        elif rps == '잠깐':
            while True:
                ans = input(
                    "\n[일시정지] 게임을 처음부터 다시 하시겠습니까? ( 돌아가기 / 다시하기 / 종료하기 )\n" + ('=' * 40) + "\n\t\t⌜주의⌟\n'종료하기' 입력 시 저장은 불가능합니다.\n" + ('=' * 40) + "\n: ").strip()

                if ans == '돌아가기':
                    break

                if ans == '다시하기':
                    print('\n게임을 다시 시작합니다.')
                    global computer_rps, player_rps, win, draw, lose
                    player_name = input('\n닉네임을 입력해주세요!!\n: ')
                    player_list.append(
                        {'name': player_name, 'win': win, 'draw': draw, 'lose': lose})
                    intro()
                    win = 0
                    draw = 0
                    lose = 0
                    random.shuffle(rps_list)
                    computer_rps = rps_list[0]
                    break

                if ans == '종료하기':
                    return ans

                if ans not in ('돌아가기', '다시하기', '종료하기'):
                    print(
                        "\n" + ('-' * 55) + "\n\t\t\t<정보>\n\n질문에 ( 돌아가기 / 다시하기 / 종료하기 )로 대답해주세요.\n" + ('-' * 55) + '\n\n')
                    pass

        else:
            print("\n" + ('-' * 50) +
                  "\n\t\t    <정보>\n\n( 주먹 / 가위 / 보 ) 중 하나입니다. 다시 입력하세요.\n또는 ( rock / paper / scissors )\n" + ('-' * 50) + '\n\n')


win = 0
draw = 0
lose = 0

player_list = [{'name': '개발자', 'win': 4, 'draw': 6, 'lose': 5}]


def intro():
    print('\n' + ('='*60) + '\n' + '\t\t     주먹-가위-보 게임\n' + ('='*60) + '\n')
    for i, x in enumerate(player_list, 1):
        name = x['name']
        win = x['win']
        draw = x['draw']
        lose = x['lose']
        print(i, f'닉네밍: {name}     \t승리: {win}   무승부: {draw}   패배: {lose}')


intro()
player_rps = player_selection()

while True:
    if computer_rps == "주먹(rock)":
        if player_rps.lower() == 'rock' or player_rps == '주먹':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t  무승부 ?!\n')
            draw += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        elif player_rps.lower() == 'paper' or player_rps == '보':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t   승리 !!!\n')
            win += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        elif player_rps.lower() == 'scissors' or player_rps == '가위':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t    패배... \n')
            lose += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        else:
            print('\n게임을 종료합니다.\n')
            break

    if computer_rps == "가위(scissors)":
        if player_rps.lower() == 'scissors' or player_rps == '가위':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t  무승부 ?!\n')
            draw += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        elif player_rps.lower() == 'rock' or player_rps == '주먹':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t   승리 !!!\n')
            win += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        elif player_rps.lower() == 'paper' or player_rps == '보':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t    패배... \n')
            lose += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        else:
            print('\n게임을 종료합니다.\n')
            break

    if computer_rps == "보(paper)":
        if player_rps.lower() == 'paper' or player_rps == '보':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t  무승부 ?!\n')
            draw += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        elif player_rps.lower() == 'scissors' or player_rps == '가위':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t   승리 !!!\n')
            win += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        elif player_rps.lower() == 'rock' or player_rps == '주먹':
            print('\n' + ('=' * 45) +
                  f'\n 컴퓨터: {computer_rps}\tvs\t 나: {player_rps}\n\n\t\t    패배... \n')
            lose += 1
            print(f'\t      승: {win}  무: {draw}  패: {lose}' +
                  '\n' + ('=' * 45) + '\n')
            random.shuffle(rps_list)
            computer_rps = rps_list[0]
            player_rps = player_selection()

        else:
            print('\n게임을 종료합니다.\n')
            break
