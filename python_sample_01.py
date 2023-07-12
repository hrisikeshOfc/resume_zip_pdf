class AnimalIdentifier:
    def __init__(self, text):
        self.text = text
    
    def identify_animal(self):
        animal_list = self.text.split(' ')
        for word in animal_list:
            if word == 'cat':
                print('this text contains a cat')
            elif word == 'dog':
                print('this text contains a dog')


if __name__ =="__main__":
    text ="I love cat"
    animal_finder = AnimalIdentifier(text)
    animal_finder.identify_animal()
