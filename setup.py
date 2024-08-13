from setuptools import setup

setup(
    name='sonnet',
    version='0.1.0',
    py_modules=['sonnet'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'sonnet = sonnet:sonnet',
            'send_mail = sonnet:send_mail',
            'check_mail = sonnet:check_mail',
            'burn_mail = sonnet:burn_mail',
        ],
    },
)