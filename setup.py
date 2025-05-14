from setuptools import setup, find_packages

setup(
    name='magazine_app',
    version='0.0.1',
    description='Magazine Management App for Frappe',
    author='Your Name',
    author_email='email@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe']
)
