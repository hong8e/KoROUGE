import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KoROUGE", # Replace with your own username
    version="1.0.0",
    author="Hongseok Kwon",
    author_email="hkwon@postech.ac.kr",
    description="Calculating ROUGE scores for Korean",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hong8e/KoROUGE.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	entry_points={
			'console_scripts': [
			'KoROUGE=KoROUGE:main'
			 ]
	},
    python_requires='>=3.6',
)
