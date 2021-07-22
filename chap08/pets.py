def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'Half-Tail')
# describe_pet(animal_type='cat', pet_name='Mischa')
describe_pet(pet_name='Ajax')