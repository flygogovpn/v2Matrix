import os

print(os.getenv('FLASK_CONFIG') or 'default')

print(os.getenv('AAA'))

print(os.getenv('AAA'), 'ddd')