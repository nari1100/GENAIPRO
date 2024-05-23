from setuptools import find_packages, setup

setup(
    name="MCQ",
    version="0.0.1",
    author="Naren",
    author_email="Naren.sompalle@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)