import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="translate-po",  # Replace with your own username
    version="1.0.13-post1",
    author="Erlend Eelmets(original),mtakagishi(modifications)",
    author_email="mtakagishi@gmail.com",
    description="Automatic PO file translator (with async support for Python 3.13)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mtakagishi/translate-po",
    packages=setuptools.find_packages(
        exclude=['docs', 'tests', 'translated', 'untranslated']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Internationalization',
    ],
    python_requires='>=3.6',
    keywords='po translate automatic google',
    project_urls={
        'Source': 'https://github.com/mtakagishi/translate-po',
        'Original Source': 'https://github.com/zcribe/translate-po',
        'Original Author': 'http://www.erlend.ee',
    },
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    install_requires=[
        'polib>=1.2.0',
        'googletrans==4.0.2'
    ],
    setup_requires=[
        'polib>=1.2.0',
        'googletrans==4.0.2'
    ],
)
