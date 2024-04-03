import random
import string

class randomGen:
    @staticmethod
    def random_email(size=8, chars=string.ascii_lowercase + string.digits):
        prefix = random.choice(string.ascii_lowercase)  # Ensure the first character is an alphabet
        prefix += ''.join(random.choice(chars) for _ in range(size - 1))  # Generate remaining characters
        suffix = "@mailcatch.com"
        # suffix = "@yopmail.com"
        # suffix = "@yopmail.com" //https://moakt.com/en
        return prefix + suffix


    @staticmethod
    def random_Ranfirst_name(size=7, chars=string.ascii_lowercase + string.digits):
        prefix = random.choice(string.ascii_lowercase)  # Ensure the first character is an alphabet
        prefix += ''.join(random.choice(chars) for _ in range(size - 1))  # Generate remaining characters
        return prefix
    # @staticmethod
    # def random_first_name():
    #     random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
    #     return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_first_name():
        # List of common first names
        first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack',
                       'Kate', 'Liam', 'Mia', 'Noah', 'Olivia', 'Parker', 'Quinn', 'Riley', 'Samuel', 'Taylor',
                       'Uma', 'Victor', 'Willow', 'Xander', 'Yasmine', 'Zane', 'Abigail', 'Benjamin', 'Chloe',
                       'Daniel', 'Emily', 'Finn', 'Gabriella', 'Hudson', 'Isabella', 'Jacob', 'Kylie', 'Lucas',
                       'Madison', 'Nathan', 'Olivia', 'Peyton', 'Quentin', 'Rebecca', 'Sophia', 'Tyler', 'Ursula',
                       'Violet', 'Wyatt', 'Xena', 'Yara', 'Zachary', 'Ava', 'Bryan', 'Cora', 'Dylan', 'Elena',
                       'Felix', 'Gemma', 'Hector', 'Isla', 'Jason', 'Katherine', 'Leo', 'Megan', 'Nina', 'Oscar',
                       'Penelope', 'Quincy', 'Rose', 'Sebastian', 'Tessa', 'Ulysses', 'Vivian', 'Winston', 'Ximena',
                       'Yasmine', 'Zara', 'Amelia', 'Brody', 'Cecilia', 'Derek', 'Eliza', 'Fiona', 'Gavin', 'Harper',
                       'Ian', 'Jasmine', 'Kai', 'Luna', 'Milo', 'Nora', 'Owen', 'Piper', 'Quincy', 'Rachel']

        # Randomly select a name from the list
        random_name = random.choice(first_names)

        return random_name


    @staticmethod
    def random_company_name():
        first_part = randomGen.random_first_name()  # Access the random_first_name method using the class
        second_part = ['Technologies', 'Solutions', 'Innovations', 'Systems', 'Services', 'Creators']
        third_part = ['Private Limited', 'Inc.', 'LLC', 'Enterprises', 'Group']

        # Randomly choose words for the second and third parts of the company name
        company_name = first_part + ' ' + random.choice(second_part) + ' ' + random.choice(third_part)
        return company_name

    @staticmethod
    def random_phone_number():
        prefixes = ['6', '7', '8', '9']  # Valid starting digits for Indian mobile numbers

        prefix = random.choice(prefixes)
        remaining_digits = ''.join(random.choice('0123456789') for _ in range(9))

        return f'{prefix}{remaining_digits}'

    @staticmethod
    def random_Emp_Id():
        prefix = '9'  # Assuming '9' as the fixed prefix
        remaining_digits = ''.join(random.choice('0123456789') for _ in range(4))  # Generating 4 random digits

        return f'{prefix}{remaining_digits}'

    @staticmethod
    def random_Title():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f"Test{random_part}"

    @staticmethod
    def random_Description():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f"Test{random_part}"

    @staticmethod
    def random_overviwDescription():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(50))  # Random part after "test"
        return f"Test{random_part}"

    @staticmethod
    def random_last_name():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_degree():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_specialization():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(10))  # Random part after "test"
        return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_university():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(10))  # Random part after "test"
        return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_addressInput():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(10))  # Random part after "test"
        return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_pinCode():
        prefixes = ['6', '7', '8', '9']  # Valid starting digits for Indian mobile numbers

        prefix = random.choice(prefixes)
        remaining_digits = ''.join(random.choice('0123456789') for _ in range(7))

        return f'{prefix}{remaining_digits}'

    # ===================krishna==========================
    @staticmethod
    def random_categorytitle():
        prefix = 'Test Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_subcategorytitle():
        prefix = 'Test Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_subcategorytitle1():
        prefix = 'Test Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_subcategorytitle2():
        prefix = 'Test Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_subcategorytitle3():
        prefix = 'Test Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_subcategorytitle4():
        prefix = 'Test Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_contenttitle():
        prefix = 'Test Content Title '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_contentsectionname():
        prefix = 'Test section name '  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(7))

        return f'{prefix}{random_part}'

    @staticmethod
    def random_acronym1():
        prefix = 'T'  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"

        return f'{prefix}{random_part}'

    @staticmethod
    def random_acronym2():
        prefix = 'e'  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f'{prefix}{random_part}'

    @staticmethod
    def random_certificationname():
        prefix = 'Certificate'  # Assuming '9' as the fixed prefix
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f'{prefix}{random_part}'