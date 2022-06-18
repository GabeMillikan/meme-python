from setuptools import setup, find_packages


setup(
    name='meme-python',
    version='1.0.0',
    license='MIT',
    author='Gabe Millikan',
    url='https://github.com/GabeMillikan/meme-python',
    install_requires=['Pillow'],
    python_requires='>=3',
    description='Meme Generator',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(include=['meme']),
    package_data={
        'meme': ['static/*'],
    },
)
