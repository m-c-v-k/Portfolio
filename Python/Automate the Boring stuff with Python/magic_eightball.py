### A Simple Magic 8Ball program ###

import random

messages = ['It is certain.',
            'It is decidedly so.',
            'Yes, definetely.',
            'Reply hazy, try agian.',
            'Ask again later.',
            'Concentrate and ask again.',
            'My reply is no.',
            'Outlook not so good.',
            'Very doubtful.']

print(messages[random.randint(0, len(messages) - 1)])
