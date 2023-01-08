from setuptools import setup, find_packages

long_desc = """
Rest client with all available request to inmo-backend
"""


setup(
    name='RestClient',
    version='0.1',
    description="Rest client to backend access",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Santiago Gómez',
    author_email='sgvilar@esei.uvigo.es',
    license='MIT',
    packages=find_packages(exclude=[]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=["requests"],
    tests_require=[],
    entry_points={}
)
