from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=['certifi>=2019.3.9', 'pypandoc>=1.4','pytest>=4.3.1','pytest-runner>=4.4'],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/<github_account>/titanic_datascience',
    author='Amol Patel',  # Substitute your name
    author_email='me@myemail.com',  # Substitute your email
    license='MIT',
    packages=['titanic'],
)