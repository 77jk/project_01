class KoreanWordChainGame:
    def __init__(self):
        self.words = []  # 입력된 단어를 저장하는 리스트
        self.last_word = None  # 마지막 단어를 저장하는 변수
        self.scores = {'A': 0, 'B': 0}  # 플레이어 A와 B의 점수를 저장하는 딕셔너리
        self.current_player = 'A'  # 현재 차례를 나타내는 변수

    def start_game(self):
        print("한글 끝말잇기 게임을 시작합니다!")
        print("(10자 이하로 입력하세요.)")
        print("플레이어 A의 차레입니다.")

    def is_valid_word(self, word):
        if not word:
            return False  # 공백은 유효하지 않음
        if self.last_word is None:
            return True  # 게임이 시작되면 어떤 단어든 유효함
        last_char = self.last_word[-1]  # 마지막 단어의 마지막 글자
        return word[0] == last_char  # 첫 글자가 마지막 글자와 일치하는지 확인
    
    def is_valid_length(self, word):
        return len(word) <= 10  # 10글자 이하의 단어만 유효함
    
    def is_unique_word(self, word):
        return word not in self.words  # 이미 사용된 단어는 유효하지 않음

    def print_prompt(self): # 끝말을 알려줌
        if self.last_word:
            print(f'플레이어 {self.current_player}의 차례입니다.')
            print(f'"{self.last_word[-1]}"(으)로 시작하는 ')

    def play(self, word):
        # 입력된 단어가 모두 한글로만 이루어져 있고 끝말잇기 규칙, 글자길이 제한, 중복 여부를 따른다면 게임을 진행
        if all('가' <= char <= '힣' for char in word) and self.is_valid_word(word) and self.is_valid_length(word) and self.is_unique_word(word):
            self.words.append(word)
            self.last_word = word
            print(f'"{word}"을(를) 입력했습니다.')
            self.scores[self.current_player] += 1  # 점수 증가
            self.switch_player()  # 플레이어 교체
        else:
            self.scores[self.current_player] -= 1  # 점수 감소
            if not self.is_valid_word(word): 
                print(f'"{word}"을(를) 사용할 수 없습니다.') # if문 점수 감소 적용 방법???
            elif not self.is_valid_length(word):
                print("글자수 초과입니다.")
                print("10자 이하로 입력하세요.")
            elif not self.is_unique_word(word):
                print("이미 사용된 단어입니다.")
                print("다른 단어를 입력하세요.")
            

    def switch_player(self):
        if self.current_player == 'A':
            self.current_player = 'B'
        else:
            self.current_player = 'A'       
            

# 게임 인스턴스 생성
game = KoreanWordChainGame()
game.start_game()

while True:
    game.print_prompt()  # 메시지 출력
    user_input = input("단어를 입력하세요: ")
    if all('가' <= char <= '힣' for char in user_input):
        game.play(user_input)
        print("-------------------------------------")
        print(f"플레이어 A: {game.scores['A']} 점, 플레이어 B: {game.scores['B']} 점")
        print("-------------------------------------")
    else:
        print("영어, 숫자, 특수문자, 공백은 입력할 수 없습니다. ")


    
    
 
