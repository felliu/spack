# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class XcbUtilXrm(AutotoolsPackage):
    """XCB util-xrm module provides the 'xrm' library, i.e.  utility functions
    for the X resource manager."""

    homepage = "https://github.com/Airblader/xcb-util-xrm"
    git      = "https://github.com/Airblader/xcb-util-xrm.git"

    # This GitHub project includes some git submodules, which must be fetched
    # in order to build it.
    version('1.2', tag='v1.2', submodules=True)

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('pkgconfig', type='build')

    depends_on('libxcb@1.4:')
