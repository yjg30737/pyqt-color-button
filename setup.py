from setuptools import setup, find_packages

setup(
    name='pyqt-color-button',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='circle-shaped color button',
    url='https://github.com/yjg30737/pyqt-color-button.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)