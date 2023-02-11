from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="machaao",
    version="0.3.13",
    author="Abhishek Raj",
    author_email="abhishek@machaao.com",
    description="A module for python developers looking to build, prototype & deploy deeply personalized chatbots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/machaao/machaao-py",
    packages=find_packages(),
        entry_points={
            'console_scripts': [
                'machaao = machaao.machaao:main'
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "pyjwt",
        "asyncio",
        "flask",
        "httpx",
        "bs4",
        "Flask-API",
        "click",
        "certifi",
        "websockets",
        "aiohttp",
    ],
)
