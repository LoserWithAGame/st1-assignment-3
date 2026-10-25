
"""Stage 6 practitioner lookup tests - Issue #3."""

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PractitionerService


def create_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    practitioner = service.register_practitioner(
        "D1", "Taylor Example", "General"
    )
    return store, service, practitioner


def test_find_existing_practitioner():
    store, service, practitioner = create_practitioner()

    result = service.find_practitioner("D1")

    assert result is practitioner
    assert result is store.find_practitioner("D1")


def test_find_practitioner_with_spaces():
    _, service, practitioner = create_practitioner()

    assert service.find_practitioner("  D1  ") is practitioner


def test_unknown_practitioner_raises_lookup_error():
    _, service, _ = create_practitioner()

    with pytest.raises(LookupError):
        service.find_practitioner("D99")


def test_practitioner_id_is_case_sensitive():
    _, service, _ = create_practitioner()

    with pytest.raises(LookupError):
        service.find_practitioner("d1")


@pytest.mark.parametrize("invalid_id", ["", "   "])
def test_blank_practitioner_id_raises_value_error(invalid_id):
    _, service, _ = create_practitioner()

    with pytest.raises(ValueError):
        service.find_practitioner(invalid_id)


def test_failed_lookup_does_not_modify_practitioner():
    store, service, practitioner = create_practitioner()

    with pytest.raises(LookupError):
        service.find_practitioner("UNKNOWN")

    assert store.find_practitioner("D1") is practitioner
    assert len(store.list_practitioners()) == 1
