class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz(
                "영화 《기생충》의 감독은 누구일까?",
                ["봉준호", "박찬욱", "이창동", "김지운"],
                1
            ),
            Quiz(
                "《오징어 게임》에서 첫 번째 게임의 이름은?",
                ["무궁화 꽃이 피었습니다", "줄다리기", "구슬치기", "달고나 뽑기"],
                1
            ),
            Quiz(
                "해리 포터가 다니는 마법학교의 이름은?",
                ["보바통", "덤스트랭", "호그와트", "일버모니"],
                3
            ),
            Quiz(
                "드라마 《도깨비》에서 김신의 정체는?",
                ["저승사자", "도깨비", "구미호", "무당"],
                2
            ),
            Quiz(
                "영화 《타이타닉》에서 잭과 로즈가 탑승한 배의 이름은?",
                ["브리타닉", "올림픽", "루시타니아", "타이타닉"],
                4
            )
        ]

    def show_quizzes(self):
        print("\n===== 등록된 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}] {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"  {number}. {choice}")

    def play_quiz(self):
        print("\n===== 퀴즈 풀기 =====")

        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {index}. {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

            while True:
                answer = input("정답 번호를 입력하세요: ").strip()

                if not answer.isdigit():
                    print("숫자로 입력해 주세요.")
                    continue

                answer = int(answer)

                if answer < 1 or answer > len(quiz.choices):
                    print("선택지에 있는 번호를 입력해 주세요.")
                    continue

                break

            if answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n===== 퀴즈 결과 =====")
        print(f"총 {len(self.quizzes)}문제 중 {score}문제를 맞혔습니다.")

    def add_quiz(self):
        print("\n===== 퀴즈 추가하기 =====")

        question = input("문제를 입력하세요: ").strip()

        if not question:
            print("문제는 비워둘 수 없습니다.")
            return

        choices = []

        for i in range(4):
            choice = input(f"{i + 1}번 선택지를 입력하세요: ").strip()

            if not choice:
                print("선택지는 비워둘 수 없습니다.")
                return

            choices.append(choice)

        while True:
            answer = input("정답 번호를 입력하세요 (1~4): ").strip()

            if not answer.isdigit():
                print("숫자로 입력해 주세요.")
                continue

            answer = int(answer)

            if answer < 1 or answer > 4:
                print("1~4 중에서 선택해 주세요.")
                continue

            break

        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다!")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        print("아직 최고 점수 기록 기능은 준비 중입니다.")

    def show_menu(self):
        while True:
            print("\n===== 영화 및 드라마 퀴즈 게임 =====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가하기")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 보기")
            print("5. 종료")

            choice = input("메뉴를 선택하세요: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_best_score()
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 중에서 선택해 주세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.show_menu()