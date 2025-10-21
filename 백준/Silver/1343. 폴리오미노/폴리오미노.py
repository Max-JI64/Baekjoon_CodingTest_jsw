import sys

def solve():
    # 입력 보드판을 한 줄로 받습니다.
    # rstrip()을 사용하여 개행 문자를 제거합니다.
    try:
        board = sys.stdin.readline().rstrip()
    except:
        return

    # 1. '.'을 기준으로 'X' 블록 분리
    # 'X'만 있는 블록들만 남게 됩니다. (예: "XX.XXXXXX" -> ["XX", "", "XXXXXX"])
    blocks = board.split('.')

    result_blocks = []
    
    # 2. 각 'X' 블록 치환
    for block in blocks:
        length = len(block)
        
        # 블록의 길이가 0이면 빈 문자열 그대로 유지
        if length == 0:
            result_blocks.append("")
            continue

        # 길이가 4의 배수도 2의 배수도 아닌 홀수라면 덮을 수 없음
        if length % 2 != 0:
            print(-1)
            return

        # 3. 그리디 치환: 'AAAA'를 먼저 채우고 남은 2의 배수를 'BB'로 채움
        # 'AAAA'로 덮을 수 있는 횟수
        num_AAAA = length // 4
        # 'AAAA'로 덮고 남은 길이 (이는 2의 배수임이 보장됨)
        remainder = length % 4 
        
        # 'BB'로 덮을 수 있는 횟수
        num_BB = remainder // 2 

        # 치환된 문자열 생성 (사전순으로 앞서기 위해 AAAA를 먼저 배치)
        covered_block = 'AAAA' * num_AAAA + 'BB' * num_BB
        result_blocks.append(covered_block)
        
    # 4. 결과 출력
    # 분리했던 'X' 블록들을 '.'을 구분자로 다시 합칩니다.
    final_board = '.'.join(result_blocks)
    print(final_board)

if __name__ == "__main__":
    solve()