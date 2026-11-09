from datetime import datetime
import pytest

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
