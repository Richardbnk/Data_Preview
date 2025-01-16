import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='Data_Preview',
    version='1.0.47',
    author="Richard Raphael Banak",
    description="Robot Specialist Library for Robot Process Automation",
    url="https://github.com/Richardbnk/Data_Preview",
    packages=['data_preview'],
    
    py_modules = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'plotly-express', 'streamlit'],
    
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
