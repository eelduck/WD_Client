from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

setup(
    name='WD_Client',
    version='0.0.1',
    description="Client application of weapon detection system",
    author="Ildar Azamatov",
    author_email='ildar.azamatov.personal@gmail.com',
    url='https://github.com/eelduck/WD_Client',
    packages=['wd_client', 'wd_client.images',
              'wd_client.tests'],
    package_data={'wd_client.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'wd_client=wd_client.wd_client:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='WD_Client',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
