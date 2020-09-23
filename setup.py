from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='ldep',
        version = '0.1',
        description = 'Local dependency traversal tool',
        long_description = readme(),
        url = 'https://github.com/estcube/GUnit',
        author = 'Mathias Plans',
        author_email = 'mathiasplans15@gmail.com',
        license = 'MIT',
        packages = ['sdepend'],
        install_requires = [],
        include_package_data=True,
        zip_safe = False)
