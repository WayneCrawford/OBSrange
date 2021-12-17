import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

# version = {}
# with open("obscampaigninfo/version.py") as fp:
#    exec(fp.read(), version)

setuptools.setup(
    name="obsrange",
    # version=version['__version__'],
    version='??',
    author="Josh Russel",
    author_email="jrussell@ldeo.columbia.edu",
    description="Ocean bottom seismometer relocation",
    long_description=long_description,
    long_description_content_type="text/markdown; charset=UTF-8",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['numpy>=1.13.1',
                      'scipy>=0.91.1',
                      'matplotlib>=2.2.2',
                      'pymap3d>=1.7.4',
                      'ipython'],
#     entry_points={
#          'console_scripts': [
#              'experiment_to_campaigns=obscampaigninfo.experiment_to_campaigns:main',
#              'validate_campaign=obscampaigninfo.info_files:_validate_script'
#          ]
#     },
    python_requires='>=3.0',
    classifiers=(
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics"
    ),
    keywords='software'
)
