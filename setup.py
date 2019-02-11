import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='drf-replace-ordering-filter',
    version='1.0.1',
    author='Emil Santurio',
    author_email='emilsas@gmail.com',
    description='Django Rest Framework OrderingFilter backend to replace field name in ordering params.',
    long_description=long_description,
    url='https://github.com/emilsas/drf-replace-ordering-filter',
    packages=setuptools.find_packages(),
    install_requires=[
        'djangorestframework'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
