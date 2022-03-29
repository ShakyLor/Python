class Presenter():
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print(self.name)

presenter = Presenter('gochu')
presenter.say_hello()
presenter.name = 'Gonchu'
presenter.say_hello()
