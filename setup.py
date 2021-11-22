from setuptools import setup, find_packages

setup(
    name='color-button',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='circle-shaped color button',
    url='https://github.com/yjg30737/color-button.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)