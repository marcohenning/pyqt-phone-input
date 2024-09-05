from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as fh:
    readme = "\n" + fh.read()

setup(
    name='pyqt-phone-input',
    version='1.0.0',
    author='Marco Henning',
    license='MIT',
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        'pyqt_phone_input.flag_icons': ['*.png']
    },
    install_requires=[
        'QtPy>=2.4.1'
    ],
    python_requires='>=3.7',
    description='A clean and modern phone number input widget for PyQt and PySide',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/marcohenning/pyqt-phone-input',
    keywords=['python', 'pyqt', 'qt', 'phone'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
