from setuptools import setup, find_packages

setup(
    name="emotion_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Aaron Peazzoni",
    author_email="peazzonil@gmail.com",
    description="A package to detect emotions in text using Watson NLP API",
    keywords="emotion, nlp, watson",
    url="https://github.com/peazzoni1/emotion_detection"
)