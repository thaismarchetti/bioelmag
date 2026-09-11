"""
bioelmag: Numerical methods in electrobiomagnetism

The '__init__.py' file of the bioelmag package. It imports all the main modules and functions for easy access.
It defines the public API of the package. For example, instead of importing the 
module directly with 'import bioelmag.ptb_opm_protocol as pop', its functions can be exposed through 
'__init__.py' and imported directly from the package. Ex: 'from bioelmag import <function>'.

TODO: Modify the '__init__.py' file to include the main functions used in the preprocessing pipeline.

Main modules:
  - ptb_opm_protocol: Load sensor metadata and raw data
  - lead_selection: Covariance analysis and channel selection
  - vector_functions: Geometric operations and dipole utilities
  - plot_functions: Visualization (PSD, sensor 3D, etc.)
  - ptb_flthdr: Bin (FLT) file format reading

"""

__version__ = "0.0.1"
__author__ = "Urban Marhl"
__author_email__ = "urban.marhl@imfm.si"

from bioelmag.lead_selection import (
    EvokedMaps,
    covariance_matrix,
    get_covariance_matrix,
    get_leadsel_matrix,
    get_mne_EvokedMaps,
)
from bioelmag.plot_functions import plot_psd, plot_sensors_pyvista1
from bioelmag.ptb_opm_protocol import (
    create_mne_raw,
    read_fnirs_chan_info,
    read_meas_info,
    read_sens_info,
    read_sens_info_v2,
)
from bioelmag.ptb_flthdr import imp_bin_data, imp_hdr_param, imp_samp_freq
from bioelmag.vector_functions import (
    create_2d_square_me,
    create_net_sphere_hex,
    create_rand_dipole_sphere,
    rotation_x,
    rotation_y,
    rotation_z,
    trans_cart_spher,
    trans_spher_cart,
)

__all__ = [
    # OPM Protocol
    "read_sens_info",
    "read_sens_info_v2",
    "read_meas_info",
    "read_fnirs_chan_info",
    "create_mne_raw",
    # FLT File Format
    "imp_bin_data",
    "imp_hdr_param",
    "imp_samp_freq",
    # Lead Selection
    "EvokedMaps",
    "covariance_matrix",
    "get_covariance_matrix",
    "get_leadsel_matrix",
    "get_mne_EvokedMaps",
    # Plotting
    "plot_psd",
    "plot_sensors_pyvista1",
    # Vector Functions
    "trans_cart_spher",
    "trans_spher_cart",
    "rotation_x",
    "rotation_y",
    "rotation_z",
    "create_2d_square_me",
    "create_net_sphere_hex",
    "create_rand_dipole_sphere",
]
