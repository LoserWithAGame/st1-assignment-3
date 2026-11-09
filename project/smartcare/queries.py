"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    return (appointment.date_time, appointment.appointment_id)

def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    """Return a new list for this practitioner, optionally filtered by
    status.

    Order by date/time then appointment ID using appointment_sort_key.
    Do not mutate the source list/objects or perform input/output.
    """
    matches = []
    for appointment in appointments:
        # skip apppointments belonging to another practitioner
        if appointment.practitioner.practitioner_id != practitioner_id:
            continue
        # when a status was supplied, keep only that status.
        if status is not None and appointment.status is not status:
            continue
        matches.append(appointment)
    return sorted(matches, key=appointment_sort_key)