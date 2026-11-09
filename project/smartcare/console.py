"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')


def run_menu() -> None:
    """Stage 9: implement the register/find/book/cancel/list/exit menu.

    Call services, recover from expected input errors, and keep this
    session's data until exit. main.py reports the incomplete menu
    without crashing.
    """
    menuSelection: str = input(f"MAIN MENU\n------------------------------------------------------------\n[1] Register patient\n[2] Find patient\n[3] Register practitioner\n[4] Find practitioner\n[5] Book appointment\n[6] Cancel appointment\n[7] Find appointment\n[8] List practitioner appointments\n[0] Exit\n------------------------------------------------------------\nSelect an option: [INPUT] ")

    if not menuSelection.strip().isdigit() or len(menuSelection.strip()) != 1:
        print("Unknown choice. Choose a number from 0 to 8.")

    numSelection = int(menuSelection.strip())

    # Registering a Patient
    if numSelection == 1:
        patientID: str = input("Patient ID: [INPUT] ")
        patientName: str = input("Patient name: [INPUT] ")
        patient = PatientService.register_patient(patient_id=patientID, patientName=patientName)
        print(f"Patient registered successfully.\nPatient ID : {patient.patient_id}\nName : {patient.name}")
    # Patient Finder
    elif numSelection == 2:
        patientID: str = input("Patient ID: [INPUT] ")
        patient = PatientService.find_patient(patient_id=patientID)
        print(f"Patient found. {patient.patient_id}: {patient.name}\nPatient ID : {patient.patient_id}\nName : {patient.name}")
    elif numSelection == 3:
        practitionerID: str = input("Practitioner ID: [INPUT] ")
        practitionerName: str = input("Practitioner name: [INPUT] ")
        specialty: str = input("Specialty: [INPUT] ")
        practitioner = PractitionerService.register_practitioner(practitioner_id=practitionerID, name=practitionerName, specialty=specialty)
        print(f"Practitioner registered successfully.\nPractitioner ID : {practitioner.practitioner_id}\nName : {practitioner.name}\nSpecialty : {practitioner.specialty}")
    elif numSelection == 4:
        practitionerID: str = input("Patient ID: [INPUT] ")
        practitioner = PractitionerService.find_practitioner(practitioner_id=practitionerID)
        print(f"Practitioner found. {practitioner.practitioner_id}: {practitioner.name}, {practitioner.specialty}\nPractitioner ID : {practitioner.practitioner_id}\nName : {practitioner.name}\nSpecialty : {practitioner.specialty}")
    elif numSelection == 5:
        appointmentID: str = input("Appointment ID: [INPUT] ")
        patientID: str = input("Patient ID: [INPUT] ")
        practitionerID: str = input("Practitioner ID: [INPUT] ")
        dateandTime: str = input("Date/time [YYYY-MM-DD HH:MM]: [INPUT] ")
        appointment = AppointmentService.book_appointment(patient_id=patientID, practitioner_id=practitionerID, date_time=dateandTime, appointment_id=appointmentID)
        patient = PatientService.find_patient(patient_id=patientID)
        practitioner = PractitionerService.find_practitioner(practitioner_id=practitionerID)
        print(f"Appointment Booked Successfully. Appointment ID : {appointment.appointment_id}\nPatient : {patient.name} ({patient.patient_id})\nPractitioner : {practitioner.name} ({practitioner.practitioner_id})\nSpecialty : {practitioner.specialty}\nDate/time : {appointment.date_time}\nStatus : {appointment.status}\nReference : {appointment.appointment_id}: {patient.patient_id} with {practitioner.practitioner_id}, {appointment.date_time}, scheduled")
    elif numSelection == 6:
        appointmentID = input("Appointment ID: [INPUT] ")
        appointment = AppointmentService.cancel_appointment(appointment_id=appointmentID)
        # appointment = AppointmentService.find_appointment(appointment_id=appointmentID)
        practitioner = PractitionerService.find_practitioner(practitioner_id=appointment.practitioner)
        patient = PatientService.find_patient(patient_id=appointment.patient)
        print(f"Appointment Cancelled Successfully. Appointment ID : {appointment.appointment_id}\nPatient : {patient.name} ({patient.patient_id})\nPractitioner : {practitioner.name} ({practitioner.practitioner_id})\nSpecialty : {practitioner.specialty}\nDate/time : {appointment.date_time}\nStatus : {appointment.status}\nReference : {appointment.appointment_id}: {patient.patient_id} with {practitioner.practitioner_id}, {appointment.date_time}, cancelled")
    elif numSelection == 7:
        appointmentID = input("Appointment ID: [INPUT] ")
        appointment = AppointmentService.find_appointment(appointment_id=appointmentID)
        practitioner = PractitionerService.find_practitioner(practitioner_id=appointment.practitioner)
        patient = PatientService.find_patient(patient_id=appointment.patient)
        print(f"Appointment Cancelled Successfully. Appointment ID : {appointment.appointment_id}\nPatient : {patient.name} ({patient.patient_id})\nPractitioner : {practitioner.name} ({practitioner.practitioner_id})\nSpecialty : {practitioner.specialty}\nDate/time : {appointment.date_time}\nStatus : {appointment.status}\nReference : {appointment.appointment_id}: {patient.patient_id} with {practitioner.practitioner_id}, {appointment.date_time}, {appointment.status}")
    elif numSelection == 8:
        practitionerID: str = input("Practitioner ID: [INPUT] ")
        appointmentStatus: str = input("Appointment Status: [INPUT] ")
        AppointmentService.list_practitioner_appointments(practitioner_id=practitionerID, status=appointmentStatus)
    elif numSelection == 0:
        joke = input("Are you sure you want to leave? [y,n]")