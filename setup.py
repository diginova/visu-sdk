import setuptools

setuptools.setup(
    name="visu-sdk",
    version="0.0.1",
    author="DigiNova",
    author_email='info@diginova.com.tr',
    description="VISU SDK",
    url='https://github.com/diginova/visu-sdk',
    license='MIT',
    install_requires=['numpy'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=['visu'],
    package_dir={'visu': 'src'},
    python_requires=">=3.6"
)