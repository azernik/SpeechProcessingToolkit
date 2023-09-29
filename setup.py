from setuptools import setup, find_packages

setup(
    name='SpeechProcessingToolkit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',  # and any other dependencies you have
    ],
    entry_points={
        'console_scripts': [
            # If you want to create any command-line scripts
        ]
    }
)
