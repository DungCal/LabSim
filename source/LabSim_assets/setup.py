from setuptools import setup, find_namespace_packages

setup(
    name="LabSim_assets",
    version="0.1.0",
    description="Assets package for LabSim",
    author="LabSim Team",
    packages=find_namespace_packages(include=["LabSim_assets*"]),
    install_requires=[
        "numpy",
        "scipy",
    ],
    extras_require={
        "full": ["isaacgym"],
    },
    python_requires=">=3.7",
)