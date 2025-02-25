# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPythonCertifiWin32(PythonPackage):
    """This package patches certifi at runtime to also include certificates from the
    windows certificate store."""

    homepage = "https://gitlab.com/alelec/python-certifi-win32"
    git      = "https://gitlab.com/alelec/python-certifi-win32.git"

    # Tarball missing version information, need to use git checkout
    version('1.6', tag='v1.6')

    depends_on('py-setuptools', type='build')
    depends_on('py-setuptools-scm', type='build')
    depends_on('py-wrapt@1.10.4:', type=('build', 'run'))
    depends_on('py-wincertstore', type=('build', 'run'), when='^python@:3.3')
    depends_on('py-certifi', type=('build', 'run'))
