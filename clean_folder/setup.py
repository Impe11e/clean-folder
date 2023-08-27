from setuptools import setup, find_namespace_packages

setup(name='clean folder',
      version='0.0.1',
      description='This is package that can help ypu to sort your junk in folders.',
      author='Mariia Khorunzha',
      author_email='1mpellee@gmail.com',
      url='https://github.com/Impe11e/module6_homework.git',
      packages=find_namespace_packages(),
      license='MIT',
      include_package_data=True,
      entry_points={'console_scripts': ['clean-folder = clean_folder.main:main']}
)