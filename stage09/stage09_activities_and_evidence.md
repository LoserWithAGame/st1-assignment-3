# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <!-- complete -->
Members and responsibilities: <!-- complete -->
Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity | Session/domain | The app needs to keep patient's ID and name so it can find them after registering them.|
| Appointment history | sessions/domain | If i cancel an appoiontment, I should still be able to find it and see it in the all-status list during the same session. |
| Temporary menu choice | Transient | The number I type tells the menu what to do this time. THe app can move on from that choice once it finishes the action, no need to save history of that choice. |
| Practitioner specialty | Session/domain | Specialty is part of the pracittioners record, so it should still be there when I look them up later. |
| Debug print output | transient | Only helpful during debugging, no other service requires this as stored data. |
| Appointment status | session/domain | The app needs the status to know whether an appointment can be cancelled and whether it should appear under a particular filter. |

What is intentionally lost on exit? [Because its all stored in memory all data will be lost after the session ends. This includes patient, pracititoner, and appointments. Including the hisotry of cancellations will reset after finishing the session.]

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key | One appointment [object] | A pair containing the date/time and the apopintment ID, [tuple[date/time, str]] | Gives python the two values to sort by. If two appointments have the same time, the ID decides which comes first. | Both values already come from the appointment. |
| select_appointments | A list of appointment objects, a practitioner ID as a string, and an appointmentstatus or None | A new list containing the mathcing appointment objects  | Keeps the appointments for the requested practitioner, applied the status filter if one was given, then sorts those results. It leaves the original list and appointments alone. | It reads the practitioner ID and status on each appointment. The service checks whether the practitioner exists. |
| Service listing | A practitioner ID as a string and an Appointmentstatus or None | A list of matching appointments, or an error | Looks up the pracittioenr, checks the filter and passes the appointments from the store to query. A known pracitioner with no matches gets an emtpy list returned | The store already has the registered practiioner and appointment records. An unknown ID gives LookupError, while an invlaid ID or filter gives ValueError. |
| Console | Keyboard inpout as text, such as a menu number, an ID, a date/time or a status. |Prompts, results and error messages on then screen | Reads what the user types, then converts it when needed and calls the right service. For listing, a blank filter becomes None and, scheduled becomes Appointmentstatus.scheduled. | The menu shares one store for the whole session. Booking uses the existing YYY-MM-DD HH:MM date/time format. |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: [ A patient has an ID and name. A practitioner has an ID, name and specialty. An appointment has its own ID, date/time and status. It links to the actual registered patient and practiioner objects. FOr example, appointment A1 can link to the existing records for P1 and D1. Cancelling it changes the status of that same A1 record. changing one thing can cause a cascade of changes in other parts of the data.]

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input | The appointment object is asking the user for information, whitch is the console's job to do | The console asks for the appointment ID, and the service finds that appointment. Then cancel() checks whether cancellation is allowed and updates the status. This also lets test call cancel() without needing any keyboard. |
| Service prints/reads the menu | The serice is mixing its work with displaying the menu and reading choices. | The console reads the user's choice and displays the result. The service carries out the action and returns an object or raises an error. This makes the serice easier to use and test on its own. |
| Query sorts its source in place | Sorting in place changes the order of the original list given to the query. This could effect other code using that list. | The query should return a new sorted list using sorted(). The caller keeps its original list in the same order, and the appointment object stays the unchanged. |
| Store prints Appointment saved | The store is displaying a message as well as keeping the record. | The store keeps the appointment so it can be retreived later. The console displays the confirmation after the service finishes successfully. This keeps the user messages in the same part of the program. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: [ Using appoiontments.sort(key=appointment_sort_key) sorts the original lilst and returns None. It is still the same list, but the order may have changed.
Using result = sorted(appointments, key=appointments_sort_key) gives me a new sorted list. THe original list stays in its original order. The two lists contain the same appointment objects.
To check that nothing was changed accidentally, I would save the original order and appointment details before running the query. Afterword, I would check that those stays the same, that the result is sorted correctly, and that result is not appointments. ]

Score-example prediction and explanation of passing the named key: [ The result would be [('chen', 5), ('Ali', 8), ('Bea', 8)]. Chen comes first becasue their score is lowest. Ali and Bea have the same score, so their names decide the order. THe original list stayus as Bea, Ali, Chen.
Key=score_key lets sorted() use the function on each item. Writing score-key() would call it straight away wihtout giving it an item. ]

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: [ Cancelling an appointment changes to CANCELLED while keeping it in the soire. Deleting it would remove the record and its history.
To check this, I would book A1, cancel it, then find it again in the same session. It should return the same appointment object with its status changed to Cancelled. The all-status list should still include A1, while the SCHEDULED list should leave it out. ]

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: Despite handling as many errors as we could think of in the Console, we still implemented a Try Except aspect to ensure that even the errors we did not account for could be handled properly.

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| QRY-01 | Practitioner ID and Appointment Status | This section is responsible for finding all appointments with inputs matching the Practitioner ID and Appointment Status. | When given a Practitioner ID and Appointment Status the system will provide all appointments for that Practitioner with that Status. | Success |
| QRY-02 | Practitioner ID and Appointment Status | No matching status produces an empty result | No matching status produces an empty result | Success |
| QRY-03 | Practitioner ID and Appointment Status | | | |
| QRY-04 | Practitioner ID and Appointment Status | Raises Errors in the result of empty values, except for knwon appointments | Known practitioner with no appointments or no matching status: New empty list; no error 
Valid unknown practitioner ID: LookupError
Blank or invalid ID: ValueError under the existing ID contract
Known practitioner with a non-enum status such as 'scheduled': ValueError; do not treat it as no matches
Omitted status: Include every status and preserve history | Success |
| FP-01 | Inputs | Repeat unchanged inputs; inspect code for hidden state, input/output and side effect | Repeat unchanged inputs; inspect code for hidden state, input/output and side effect | Success |
| FP-02 | | Distinct returned list for empty, already-sorted and unsorted inputs; contained objects remain unchange | Distinct returned list for empty, already-sorted and unsorted inputs; contained objects remain unchange | Unknown |
| FP-03 | | Test the named key directly and check sorting actually uses it | Sorting Actually uses it | Unknown |
| UI-01 | Any Required | Registering Patients, Practitioners, and Appointments. Cancelling Appointments, and Listing Scheduled appointments only | Functions as intended | Refer to Appendix |
| UI-02 | Any Required | Use unknown menu options and invalid inputs | Handles Errors correctly, and Rejects Data that is incorrect | Refer to Appendix |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: Empty is without an input, Unknown is the type of input is incorrect, and Invalid is the correct type of input but not within the range required. Enum Conversion is the process of converting multiple Strings in a list into an ordered list of strings, this means you could get the same result from referencing the String or the Integer. Actual Object Identity is the unique memory signature of an object or variable. Error Handling is ensuring that all the errors can be caught, shown, and still allow the program to run past it.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| | | | | |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- response -->
What the tests do and do not establish: <!-- response -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | Using the same ID and Inputs will reproduce results | Registering Patients, Practitioners, and Appointments. Cancelling Appointments, and Listing Scheduled appointments only | All Functional Requirements Satisfied | Refer to Appendix |
| UI-02 invalid-input recovery | Using Inputs of the same invalid, unknown, and empty type will reproduce results | Use unknown menu options and invalid inputs | Handles Errors correctly, and Rejects Data that is incorrect | All Functional Requirements Satisfied | Refer to Appendix |
| Automated service workflow | This is the Automated Method for the program, using the same inputs will reproduce the result | Follows the User's inputs and functions as intended | The Automated Service Workflow Functions as intended and follows all User inputs and Requirements. | Refer to Appendix |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: console.py::run_menu/smartcare/project/console.py
Actual prompt/context supplied: https://github.com/copilot/c/a0c02da6-836a-406f-8a31-a7bb10f5028a
Actual response: https://github.com/copilot/c/a0c02da6-836a-406f-8a31-a7bb10f5028a

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| The program sends IDs through without removing padding, whilst the checks are done with padding removed, the ID is parsed without it. | Code to check: services.py, lines 171–186; data_store.py, lines 54–60; queries.py, lines 26–35. | SEVERE | Accepted | CHANGED immediately to fix the issue. | Code fixed in console.py, run_menu() |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.


## Appendix:
PS E:\st1 assignment3 files\St1-Asignment3\project> python main.py  --interactive
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 1
Patient ID: [INPUT] P1
Patient name: [INPUT] Alex Example
Patient registered: P1: Alex Example
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 3
Practitioner ID: [INPUT] D1
Practitioner name: [INPUT] Taylor Example
Specialty: [INPUT] General
Practitioner registered: D1: Taylor Example, General
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 5
Appointment ID: [INPUT] A1
Patient ID: [INPUT] P1
Practitioner ID: [INPUT] D1
Date/time [YYYY-MM-DD HH:MM]: [INPUT] 2026-10-01 09:00
A1: P1 with D1, 2026-10-01 09:00, scheduled
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 8
Practitioner ID: D1
Status (blank=all; scheduled/cancelled/completed): 
A1: P1 with D1, 2026-10-01 09:00, scheduled
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 8
Practitioner ID: D1
Status (blank=all; scheduled/cancelled/completed): scheduled
A1: P1 with D1, 2026-10-01 09:00, scheduled
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 6
Appointment ID: [INPUT] A1
A1: P1 with D1, 2026-10-01 09:00, cancelled
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 8
Practitioner ID: D1
Status (blank=all; scheduled/cancelled/completed): 
A1: P1 with D1, 2026-10-01 09:00, cancelled
MAIN MENU
------------------------------------------------------------
[1] Register patient
[2] Find patient
[3] Register practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment
[7] Find appointment
[8] List practitioner appointments
[0] Exit
------------------------------------------------------------
Select an option: [INPUT] 0
Exiting. All session-only data is lost.
PS E:\st1 assignment3 files\St1-Asignment3\project> 




