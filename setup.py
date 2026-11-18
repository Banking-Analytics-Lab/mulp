import setuptools
with open("README.md", "r") as fh:
    long_descripiton = fh.read()

setuptools.setup(
    name="mulp",
    version="1.1.1",
    author="Cristián Bravo, Sigurjon Thorsteinsson, Emiliano Penaloza, María Óskarsdóttir",
    author_email="cbravoro@uwo.ca",
    description="Python implementation of the Multilayer Credit Scoring algorithm from Óskarsdóttir & Bravo (2021)",	
    long_description=long_descripiton,
    long_description_content_type="text/markdown",
    project_urls={
        'GitHub': 'https://github.com/Banking-Analytics-Lab/mulp',
        'Changelog': 'https://github.com/Banking-Analytics-Lab/mulp/blob/master/CHANGELOG.md',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "numpy>=2.0.2",
        "networkx>=3.4.2",
        "scipy>=1.14.1",
        "scikit-learn>=1.5.2" ,
        "pandas>=2.2.3",
        "igraph>=0.11.2",
    ]
)