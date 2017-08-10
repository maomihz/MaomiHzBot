from setuptools import setup

setup(
    name='maomihzbot',
    version='0.1',
    description='@MaomiHzBot telegram bot',
    long_description=open('README.rst').read(),
    url='https://github.com/maomihz/MaomiHzBot',
    author='Dexter MaomiHz',
    author_email='maomihz@gmail.com',
    license='MIT',
    packages=['maomihzbot'],
    include_package_data=True,
    install_requires=[
        'flask',
        'python-telegram-bot',
        'gunicorn',
    ]
)
