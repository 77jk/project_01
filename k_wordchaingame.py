class KoreanWordChainGame:
    def __init__(self):
        self.words = []  # 입력된 단어를 저장하는 리스트
        self.last_word = None  # 마지막 단어를 저장하는 변수
        self.scores = {'A': 0, 'B': 0}  # 플레이어 A와 B의 점수를 저장하는 딕셔너리
        self.current_player = 'A' # 현재 차례를 나타내는 변수

    def get_player_name(self, player):
        while True:
            name = input(f'플레이어 {player}의 이름을 입력하세요: ')
            if name:
                return name
            else:
                print("유효한 이름을 입력하세요.")

    def setup_players(self):
        self.player_a = self.get_player_name('A')
        self.player_b = self.get_player_name('B')

    def start_game(self):
        print("한글 끝말잇기 게임을 시작합니다!")
        print("(10자 이하로 입력하세요.)")
        print(f"플레이어 {self.player_a}의 차례입니다.")

    def is_valid_word(self, word):
        if word is None:
            return False  # 입력된 단어가 none인지 아닌지 확인함
        if self.last_word is None:
            return True  # 게임이 시작되면 어떤 단어든 유효함
        return word[0] == self.last_word[-1]  # 첫 글자가 앞 단어의 마지막 글자와 일치하는지 확인
    
    def is_valid_length(self, word):
        return len(word) <= 10  # 10글자 이하의 단어만 유효함
    
    def is_unique_word(self, word):
        return word not in self.words  # 이미 사용된 단어는 유효하지 않음

    def print_prompt(self): # 끝말을 알려줌
        if self.last_word:
            print(f'플레이어 {self.current_player}의 차례입니다.')
            print(f'"{self.last_word[-1]}"(으)로 시작하는 ')

    def is_valid_rule(self, word: str): 
        # 게임의 규칙(입력된 단어는 모두 한글, 끝말잇기 규칙, 글자길이 제한, 중복 여부)을 모두 충족해야 게임 진행
        if not all('가' <= char <= '힣' for char in word):
            return False
        if not self.is_valid_word(word):
            return False
        if not self.is_valid_length(word):
            return False
        if not self.is_unique_word(word):
            return False
        return True

    def play(self, word):
        if self.is_valid_rule(word): # is_valid_rule을 따른다면 게임 진행
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
            
    class InvalidUsernameException(Exception):
        pass

    def switch_player(self):  # 플레이어 교체
        if self.current_player == self.player_a:
            self.current_player = self.player_b
        elif self.current_player == self.player_b:
            self.current_player = self.player_a
        else:
            InvalidUsernameException()
                        

if __name__ == "__main__":

    # 게임 인스턴스 생성
    game = KoreanWordChainGame()
    game.setup_players()  # 플레이어 이름 설정
    game.start_game()

    while True:
        game.print_prompt()  # 메시지 출력
        
        user_input = input("단어를 입력하세요: ")
        if all('가' <= char <= '힣' for char in user_input):
            game.play(user_input)
            print("-------------------------------------")
            print(f"{game.player_a}: {game.scores['A']} 점, {game.player_b}: {game.scores['B']} 점")
            print("-------------------------------------")
        else:
            print("영어, 숫자, 특수문자, 공백은 입력할 수 없습니다. ")