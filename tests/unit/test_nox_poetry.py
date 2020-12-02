"""Unit tests."""
import pytest
from nox.sessions import Session

import nox_poetry
from nox_poetry.poetry import DistributionFormat


@pytest.mark.parametrize("distribution_format", [nox_poetry.WHEEL, nox_poetry.SDIST])
def test_install(session: Session, distribution_format: DistributionFormat) -> None:
    """It installs the dependencies."""
    nox_poetry.install(session, distribution_format, "pip")


@pytest.mark.parametrize("distribution_format", [nox_poetry.WHEEL, nox_poetry.SDIST])
def test_installroot(session: Session, distribution_format: DistributionFormat) -> None:
    """It installs the package."""
    nox_poetry.installroot(session, distribution_format=distribution_format)


def test_export_requirements(session: Session) -> None:
    """It exports the requirements."""
    nox_poetry.export_requirements(session).touch()
    nox_poetry.export_requirements(session)


def test_patch(session: Session) -> None:
    """It patches Session.install."""
    import nox_poetry.patch  # noqa: F401

    Session.install(session, ".")