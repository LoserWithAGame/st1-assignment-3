
"""Stage 6 patient and  practitioner lookup tests."""

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService

# Practitioner tests

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


# Patient lookup tests

def test_find_patient_returns_registered_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    patient = service.register_patient("P1", "Burnt Peanut")
    result = service.find_patient("P1")

    assert result is patient


def test_unknown_patient_raises_lookup_error():
    store = SmartCareDataStore()
    service = PatientService(store)
    service.register_patient("P1", "Burnt Peanut")

    with pytest.raises(LookupError):
        service.find_patient("P992")


def test_find_patient_with_spaces():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient("P1", "Burnt Peanut")

    result = service.find_patient("  P1  ")

    assert result is patient


def test_patient_id_is_case_sensitive():
    store = SmartCareDataStore()
    service = PatientService(store)
    service.register_patient("P1", "Burnt Peanut")

    with pytest.raises(LookupError):
        service.find_patient("p1")


@pytest.mark.parametrize("invalid_id", ["", "  ", None, 123])
def test_invalid_patient_id_raises_value_error(invalid_id):
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient(invalid_id)


def test_failed_lookup_does_not_modify_patient():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient("P1", "Burnt Peanut")

    with pytest.raises(LookupError):
        service.find_patient("UNKNOWN")

    assert store.find_patient("P1") is patient
    assert patient.patient_id == "P1"
    assert patient.name == "Burnt Peanut"
    assert len(store.list_patients()) == 1