class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...
    def initialize(self, name, email, password):
        self.name = name   #self.name의 name은 인스턴스 변수를 나타내고, 우항의 name은 initialize method를 불러왔을 때 parameter 중 하나로 입력받은 name을 말하는 것이다.
        self.email = email
        self.password = password

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
