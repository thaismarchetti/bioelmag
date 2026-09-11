from distutils.core import setup

setup(name='bioelmag',
      version='0.0.1',
      description='Python module for calculations in electrobiomagnetism',
      author='Urban Marhl',
      author_email='urban.marhl@imfm.si',
      url='https://urbanmarhl.com/',
      packages=['bioelmag'],
      install_requires=[
          'numpy',
          'scipy',
          'mne',
          'matplotlib',
      ],
      extras_require={
          'viz': ['pyvista'], # Used in plot_sensors_pyvista1, check with Urban if it should be a requirement or not
      },
     )
