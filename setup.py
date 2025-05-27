from setuptools import setup, find_packages

setup(
    name="rtrimmer",
    version="0.1.0",
    description="Lightweight RTTM and audio trimmer package.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
    ],  # Add dependencies here
    entry_points={
        'console_scripts': [
            'rttm-trim = rtrimmer.cli:main',
        ],
    },
    python_requires='>=3.8',
    include_package_data=True,
    url="https://github.com/yourusername/rtrimmer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)
