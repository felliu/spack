# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFutureApply(RPackage):
    """Apply Function to Elements in Parallel using Futures.

    Implementations of apply(), by(), eapply(), lapply(), Map(), mapply(),
    replicate(), sapply(), tapply(), and vapply() that can be resolved using
    any future-supported backend, e.g. parallel on the local machine or
    distributed on a compute cluster. These future_*apply() functions come with
    the same pros and cons as the corresponding base-R *apply() functions but
    with the additional feature of being able to be processed via the future
    framework."""

    cran = "future.apply"

    version('1.8.1', sha256='0d5bc3cb0289665bb27ae4ccad51fcc5ebf6dca46872b0a4e57790b9dc0aa6c7')
    version('1.7.0', sha256='2ffa6adb55f239918ce9679b7eac8dcc4bf2e6bed35c9cbedf4bf90d906345db')
    version('1.3.0', sha256='6374eca49bb81e05c013509c8e324cf9c5d023f9f8217b29ce7b7e12025ca371')

    depends_on('r@3.2.0:', type=('build', 'run'))
    depends_on('r-future@1.13.0:', type=('build', 'run'))
    depends_on('r-future@1.17.0:', type=('build', 'run'), when='@1.7.0:')
    depends_on('r-future@1.21.0:', type=('build', 'run'), when='@1.8.1:')
    depends_on('r-globals@0.12.4:', type=('build', 'run'))
    depends_on('r-globals@0.12.5:', type=('build', 'run'), when='@1.7.0:')
    depends_on('r-globals@0.14.0:', type=('build', 'run'), when='@1.8.1:')
