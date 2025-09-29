# Copyright (c) 2022-2025, LabSim Team
# All rights reserved.

"""Package containing asset and sensor configurations."""

import os
import toml

# Conveniences to other module directories via relative paths
LABSIM_ASSETS_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
"""Path to the extension source directory."""

LABSIM_ASSETS_DATA_DIR = os.path.join(LABSIM_ASSETS_EXT_DIR, "data")
"""Path to the extension data directory."""

LABSIM_ASSETS_METADATA = toml.load(os.path.join(LABSIM_ASSETS_EXT_DIR, "config", "extension.toml"))
"""Extension metadata dictionary parsed from the extension.toml file."""

# Configure the module-level variables
__version__ = LABSIM_ASSETS_METADATA["package"]["version"]

from .robots import *
from .sensors import *
