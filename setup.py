from setuptools import setup, find_packages

setup(
    name='mits_similarity_BJP',
    version='0.1',
    packages=find_packages(),
    description='similarity coefficients and hamming distance',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jaswanthmuthineedi/mits_similarity_BJP',
    author='BinduSree Pallavi Jaswanth',
    author_email='jaswanthmuthineedi@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)