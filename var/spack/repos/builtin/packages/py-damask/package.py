# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyDamask(PythonPackage):
    """Pre- and post-processing tools for DAMASK"""

    homepage = "https://damask.mpie.de"
    url      = "https://damask.mpie.de/download/damask-3.0.0.tar.xz"

    maintainers = ['MarDiehl']

    version('3.0.0-alpha4', sha256='0bb8bde43b27d852b1fb6e359a7157354544557ad83d87987b03f5d629ce5493')
    version('3.0.0-alpha5', sha256='2d2b10901959c26a5bb5c52327cdafc7943bc1b36b77b515b0371221703249ae')

    depends_on('python@3.7:', type=('build', 'run'))
    depends_on('py-setuptools@40.6:', type='build')
    depends_on('vtk+python', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-matplotlib', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))

    build_directory = 'python'
