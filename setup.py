import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="machaao",
    version="0.1.4",
    author="Abhishek Raj",
    author_email="abhishek@machaao.com",
    description="An easy to use module for python developers looking to build and develop chat apps using MessengerX.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/machaao/machaao-py",
    packages=setuptools.find_packages(),
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
    scripts=['bin/machaao']
)