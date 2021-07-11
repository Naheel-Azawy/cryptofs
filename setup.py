from setuptools import setup

setup(
    name="cryptofs",
    version="0.0.1",
    description="Encrypted filesystem",
    author="Naheel Azawy",
    author_email="naheelazawy@gmail.com",
    url="https://github.com/Naheel-Azawy/cryptofs",
    license="GPL-3.0",
    packages=["cryptofs"],
    install_requires=["fusepy", "pycryptodome"],
    entry_points={
        "console_scripts": [
            "cryptofs = cryptofs.cli:main"
        ]
    }
)
