import random
import string


class Utilities:

    @staticmethod
    def generate_random_email():
        domain_name = "automation.com"
        email_length = 10
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(email_length))
        email = random_string + "@" + domain_name
        return email
