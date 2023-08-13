from setuptools import setup

REQUIRES = [
    'records',
    'structlog',
    'sqlalchemy',
    'allure-pytest'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/GalinaN-create/orm_client.git',
    license='MIT',
    author='Galina Nosova',
    author_email='-',
    install_requires=REQUIRES,
    description='orm_client'
)
