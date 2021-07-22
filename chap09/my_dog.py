from chuachua import Chuachua as C
from bulldog import Bulldog as B


my_dog = C('Fifi', 6, 'Chuachua', 'brown and white')
your_dog = B('Spottie', 8, 'English bulldog', 'white with black spots')

my_dog.get_description()
my_dog.sit()
my_dog.roll_over()

your_dog.get_description()
your_dog.sit()
your_dog.roll_over()