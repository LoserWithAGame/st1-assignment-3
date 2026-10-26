

"""Stage 6 appointment cancellation service tests."""

import pytest

from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def test_cancel_appointment_returns_retained_cancelled_object():
    store = SmartCareDataStore()
    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    appointment_service = AppointmentService(store)

    patient_service.register_patient('P1', 'Alex Jones')
    practitioner_service.register_practitioner(
        'D1',
        'Taylor Swift',
        'General',
    )
    appointment = appointment_service.book_appointment(
        'A1',
        'P1',
        'D1',
        datetime(2026, 10, 1, 9),
    )

    result = appointment_service.cancel_appointment('A1')

    assert result is appointment
    assert result.status is AppointmentStatus.CANCELLED
    assert store.find_appointment('A1') is appointment
    
    
def create_booked_appointment() -> tuple[
    SmartCareDataStore,
    AppointmentService,
    Appointment,
]:
    """Create a fresh store containing one scheduled appointment."""
    store = SmartCareDataStore()
    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    appointment_service = AppointmentService(store)

    patient_service.register_patient('P1', 'Alex Jones')
    practitioner_service.register_practitioner(
        'D1',
        'Taylor Swift',
        'General',
    )
    appointment = appointment_service.book_appointment(
        'A1',
        'P1',
        'D1',
        datetime(2026, 10, 1, 9),
    )

    return store, appointment_service, appointment


def test_unknown_appointment_raises_lookup_error_and_preserves_state() -> None:
    store, appointment_service, appointment = create_booked_appointment()

    with pytest.raises(LookupError):
        appointment_service.cancel_appointment('UNKNOWN')

    assert store.list_appointments() == [appointment]
    assert appointment.status is AppointmentStatus.SCHEDULED
    
    
@pytest.mark.parametrize('invalid_id', ['', '   ', None, 123])
def test_invalid_appointment_id_raises_value_error(invalid_id) -> None:
    store, appointment_service, appointment = create_booked_appointment()

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment(invalid_id)

    assert store.list_appointments() == [appointment]
    assert appointment.status is AppointmentStatus.SCHEDULED
    
    
def test_repeated_cancellation_is_rejected_and_retains_history() -> None:
    store, appointment_service, appointment = create_booked_appointment()

    appointment_service.cancel_appointment('A1')

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')

    assert appointment.status is AppointmentStatus.CANCELLED
    assert store.find_appointment('A1') is appointment
    assert store.list_appointments() == [appointment]
    
    
def test_completed_appointment_cannot_be_cancelled() -> None:
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient(
        'P1',
        'Alex Jones',
    )
    practitioner = PractitionerService(store).register_practitioner(
        'D1',
        'Taylor Swift',
        'General',
    )
    appointment_service = AppointmentService(store)

    completed_appointment = Appointment(
        'A1',
        patient,
        practitioner,
        datetime(2026, 10, 1, 9),
        status=AppointmentStatus.COMPLETED,
    )
    store.add_appointment(completed_appointment)

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')

    assert completed_appointment.status is AppointmentStatus.COMPLETED
    assert store.find_appointment('A1') is completed_appointment
    assert store.list_appointments() == [completed_appointment]