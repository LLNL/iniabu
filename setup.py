from setuptools import setup

# long description
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

#
setup(
    name='iniabu',
    version='0.2.3',
    packages=[''],
    url='https://github.com/trappitsch/iniabu',
    license='',
    author='Reto Trappitsch',
    author_email='trappitsch1@llnl.gov',
    description='Solar System initial isotopic abundance reader.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # add the data files into the system folder
    data_files=[('iniabu_data', ['iniabu/iniabu_data/lodders09.dat'])],
    # the script to install
    scripts=['iniabu/iniabu.py'],
    install_requires=['numpy', 'sys']
)