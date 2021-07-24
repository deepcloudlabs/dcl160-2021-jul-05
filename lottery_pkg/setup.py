import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='dcllottery',  
     version='0.1',
     scripts=['dcl-lottery'] ,
     author="Binnur Kurt",
     author_email="info@deepcloudlabs.com",
     description="Lottery utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/deepcloudlabs/lottery",
     packages=setuptools.find_packages(where="src"),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    package_dir={"": "src"},
    python_requires=">=3.6",
 )