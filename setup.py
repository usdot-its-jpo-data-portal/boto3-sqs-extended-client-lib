from setuptools import setup, find_packages

setup(
    name="pysqs-extended-client",
    version="0.0.5",
    description="Amazon SQS Extended Client Library for Python for sending large payloads that exceed sqs limitations via S3",
    packages=find_packages()
)
