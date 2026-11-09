from datetime import datetime
import pytest

from smartcare import queries
from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.queries import select_appointments
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def test_select_appointments_only_returns_requested_practitioner():
    # arrage: create fresh records using one shared store
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Peanut Butter")
    practitioners.register_practitioner("D1", "Davy Jones", "General")
    practitioners.register_practitioner("D2", "Jacko Lantern", "Cardiology")

    when = datetime(2026, 10, 1, 9)

    appointment_d1 = appointments.book_appointment("A1", "P1", "D1", when)
    appointments.book_appointment("A2", "P1", "D2", when)

    #act: request D1's appointments from a list containing both practitioners'
    result = select_appointments(store.list_appointments(), "D1")

    # assert: exactly one result, containing the original D1 appointment
    assert len(result) == 1
    assert result[0] is appointment_d1

@pytest.mark.parametrize(
    "status",
    [
        None,
        AppointmentStatus.SCHEDULED,
        AppointmentStatus.CANCELLED,
        AppointmentStatus.COMPLETED,
    ],
)
def test_select_appointments_filters_by_status(status):
    # arrange: create registered participants
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient("P1", "Burnt Peanut")
    practitioner = PractitionerService(store).register_practitioner(
        "D1", "Crispy Peanut", "General"
    )

    # these query fixtures represent appointments in different states.
    scheduled = Appointment(
        "A1", patient, practitioner, datetime(2026, 10, 1, 9), AppointmentStatus.SCHEDULED
    )
    cancelled = Appointment(
        "A2", patient, practitioner, datetime(2026, 10, 1, 10), AppointmentStatus.CANCELLED
    )
    completed = Appointment(
        "A3", patient, practitioner, datetime(2026, 10, 1, 11), AppointmentStatus.COMPLETED
    )
    source = [scheduled, cancelled, completed]

    # act: exercise the default seperately from an explicit status.
    if status is None:
        result = select_appointments(source, "D1")
        expected = [scheduled, cancelled, completed]
    else:
        result = select_appointments(source, "D1", status)
        expected = {
            AppointmentStatus.SCHEDULED: [scheduled],
            AppointmentStatus.CANCELLED: [cancelled],
            AppointmentStatus.COMPLETED: [completed],
        } [status]

        # assert: the exact expected appointments are returned.
    assert result == expected

def test_select_appointments_returns_empty_when_status_has_no_matches():
    # arrange: D1 has one scheduled appointment.
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioner = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Burnt Peanut")
    practitioner.register_practitioner("D1", "Crispy Peanut", "General")

    appointment = appointments.book_appointment(
        "A1", "P1", "D1", datetime(2026, 10, 1, 9)
    )

    # Act: ask for cancelled appointments.
    result = select_appointments(
        store.list_appointments(), "D1", AppointmentStatus.CANCELLED
    )

    # assert: there are no matches, and the stored appointment is unchanged.
    assert result == []
    assert store.find_appointment("A1") is appointment
    assert appointment.status is AppointmentStatus.SCHEDULED

def test_select_appointments_sorts_without_changing_source():
    # arrange: create participants and deliberately unordered appointments.
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient("P1", "Burnt Peanut")
    practitioner = PractitionerService(store).register_practitioner(
        "D1", "Crispy Peanut", "General"
    )

    later = Appointment(
        "A3", patient, practitioner, datetime(2026, 10, 1, 10),
        AppointmentStatus.SCHEDULED,
    )
    earlier_b = Appointment(
        "A2", patient, practitioner, datetime(2026, 10, 1, 9),
        AppointmentStatus.CANCELLED,
    )
    earlier_a = Appointment(
        "A1", patient, practitioner, datetime(2026, 10, 1, 9),
        AppointmentStatus.COMPLETED,
    )

    source = [later, earlier_b, earlier_a]

    # save the original order and field values before calling the query.
    original_order = source.copy()
    original_fields = [
        (
            appointment.appointment_id,
            appointment.patient,
            appointment.practitioner,
            appointment.date_time,
            appointment.status,
        )
        for appointment in source
    ]

    #act.
    result = select_appointments(source, "D1")
    repeated_result = select_appointments(source, "D1")

    # assert: earlier time first, then appointment ID for equal times.
    assert result == [earlier_a, earlier_b, later]
    assert result is not source
    assert result[0] is earlier_a
    assert result[1] is earlier_b
    assert result[2] is later

    #each call gives us a seperate result list.
    assert repeated_result is not result
    assert repeated_result is not source

    # the original list order and appointment fields must stay unchanged.
    assert source == original_order
    assert [
        (
            appointment.appointment_id,
            appointment.patient,
            appointment.practitioner,
            appointment.date_time,
            appointment.status,
        )
        for appointment in source
    ] == original_fields

def test_select_appointments_returns_fresh_empty_list():
    source = []

    result = select_appointments(source, "D1")

    assert result == []
    assert result is not source
    assert source == []

def test_select_appointments_returns_fresh_list_when_already_sorted():
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient("P1", "Burnt Peanut")
    practitioner = PractitionerService(store).register_practitioner(
        "D1", "Crispy Peanut", "General"
    )

    first = Appointment(
        "A1", patient, practitioner, datetime(2026, 10, 1, 9),
        AppointmentStatus.SCHEDULED,
    )
    second = Appointment(
        "A2", patient, practitioner, datetime(2026, 10, 1, 10),
        AppointmentStatus.SCHEDULED,
    )
    source = [first, second]

    result = select_appointments(source, "D1")

    assert result == [first, second]
    assert result is not source
    assert result[0] is first
    assert result[1] is second
    assert source == [first, second]

def test_named_sort_key_values_and_use(monkeypatch):
    store = SmartCareDataStore()
    patient = PatientService(store).register_patient("P1", "Burnt Peanut")
    practitioner = PractitionerService(store).register_practitioner(
        "D1", "Crispy Peanut", "General"
    )
    later = Appointment(
        "A2", patient, practitioner, datetime(2026, 10, 1, 10),
        AppointmentStatus.SCHEDULED,
    )
    earlier = Appointment(
        "A1", patient, practitioner, datetime(2026, 10, 1, 9),
        AppointmentStatus.SCHEDULED,
    )

    # check the named key directly.
    original_key = queries.appointment_sort_key
    assert original_key(later) == (datetime(2026, 10, 1, 10), "A2")

    calls = []

    # record which appointments are passed to the to the named key.
    def record_key_call(appointment):
        calls.append(appointment)
        return original_key(appointment)

    monkeypatch.setattr(queries, "appointment_sort_key", record_key_call)

    result = queries.select_appointments([later, earlier], "D1")

    assert result == [earlier, later]
    assert len(calls) == 2
    assert {appointment.appointment_id for appointment in calls} == {"A1", "A2"}

def test_service_listing_returns_fresh_empty_list_for_known_practitioner():
    # arrange: D1 exists but has no appointments.
    store = SmartCareDataStore()
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    practitioner = practitioners.register_practitioner(
        "D1", "Crispy Peanut", "General"
    )

    # ACT: request the list twice.
    first = appointments.list_practitioner_appointments("D1")
    second = appointments.list_practitioner_appointments("D1")

    # assert: both are emtpy, seperate lists.
    assert first == []
    assert second == []
    assert first is not second

    # Listing leaves the registered practitioner and store unchanged.
    assert store.find_practitioner("D1") is practitioner
    assert store.list_appointments() == []

@pytest.mark.parametrize(
    "practitioner_id, expected_error",
    [
        ("UNKNOWN", LookupError),
        ("", ValueError),
        ("  ", ValueError),
        (None, ValueError),
        (123, ValueError),
    ],
)
def test_service_listing_rejects_unknown_and_invalid_ids(
    practitioner_id, expected_error
):
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Burnt Peanut")
    practitioners.register_practitioner("D1", "Crispy Peanut", "General")

    original = appointments.book_appointment(
        "A1", "P1", "D1", datetime(2026, 10, 1, 9)
    )

    # Act and assert: the rejected request raises the expected error.
    with pytest.raises(expected_error):
        appointments.list_practitioner_appointments(practitioner_id)

    # the existing appointment remains stored and unchanged.
    assert store.find_appointment("A1") is original
    assert store.list_appointments() == [original]
    assert original.status is AppointmentStatus.SCHEDULED

@pytest.mark.parametrize("invalid_status", ["scheduled", "pending", 123])
def test_service_listing_rejects_invalid_status(invalid_status):
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Burnt Peanut")
    practitioners.register_practitioner("D1", "Crispy Peanut", "General")

    original = appointments.book_appointment(
        "A1", "P1", "D1", datetime(2026, 10, 1, 9)
    )

    # Act and assert: the rejected request raises the expected error.
    with pytest.raises(ValueError):
        appointments.list_practitioner_appointments("D1", invalid_status)

    assert store.find_appointment("A1") is original
    assert store.list_appointments() == [original]
    assert original.status is AppointmentStatus.SCHEDULED