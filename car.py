class Car:

    # 자동차 객체가 가질 속성 (모델, 색상, 현재 속도)
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    # 속도를 올려주는 메서드
    def accelerate(self):
        self.speed += 10

    # 속도를 낮춰주는 메서드
    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

    # 현재 속도를 리턴해주는 메서드
    def get_speed(self):
        return self.speed