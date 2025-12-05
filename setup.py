
from setuptools import setup

setup(
    name='stop_words',
    version='0.1.0',
    description='A collection of data structures to remove stop words, including domain-specific stopwords.',
    # long_description=open('README.md').read(),
    author='Amartya Chatterjee',
    author_email='amartya.chatterjee@gmail.com',
    license='MIT',

    install_requires=[
        'spacy',
        'gensim',
        'nltk',
        'numpy==1.26.4',
        'pandas',
        'contractions',
        'requests',
        'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl',
        'en_core_web_lg @ https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl',
        'wordcloud',
        'build',
        'unidecode',
        'setuptools',
    ],
    dependency_links=[
        '''https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl''',
        '''https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl'''
    ]
)
