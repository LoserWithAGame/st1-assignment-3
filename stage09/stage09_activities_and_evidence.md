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

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- response -->

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| | | | | |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: <!-- response -->

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| QRY-01 | `select_appointments`; test `test_select_appointments_only_returns_requested_practitioner` | Requesting D1 returns exactly its original appointment and excludes D2. | Passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py|
| QRY-02 | Test `test_select_appointments_filters_by_status` | Default returns all statuses. Each enum filter returns the expected appointment. | Four cases passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| QRY-02 | Test `test_select_appointments_returns_empty_when_status_has_no_matches` | No matching status returns an empty list. The scheduled appointment stays unchanged. | Passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| QRY-03 and FP-01 | Test `test_select_appointments_sorts_without_changing_source` | Sorts by date/time then ID. Repeated calls return the same objects in separate lists. Source order and fields stay unchanged. | Passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py  |
| FP-02 | Tests `test_select_appointments_returns_fresh_empty_list` and `test_select_appointments_returns_fresh_list_when_already_sorted` | Empty and already-sorted inputs produce fresh lists containing the original matching objects. | Both passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| FP-03 | `appointment_sort_key`; test `test_named_sort_key_values_and_use` | Checks the key tuple directly and records that selection uses the named key. | Passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| QRY-04 | Test `test_service_listing_returns_fresh_empty_list_for_known_practitioner` | Known practitioner with no appointments receives separate empty lists. Records stay unchanged. | Passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| QRY-04 | Test `test_service_listing_rejects_unknown_and_invalid_ids` | Unknown ID raises LookupError. Invalid IDs raise ValueError. Existing appointment stays unchanged. | Five cases passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| QRY-04 | Test `test_service_listing_rejects_invalid_status` | Raw strings and an integer raise ValueError. Stored appointment stays unchanged. | Three cases passed. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py |
| QRY-04 and FR-07 | Test `test_service_listing_retains_cancelled_history_and_accepts_spaces` | Cancelled appointment keeps its identity. Spaced ID finds its history. Scheduled filter excludes it. | Failed initially, then passed after the service used the registered practitioner's ID. | https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py; https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/smartcare/services.py |

I ran python -m pytest -q from project/ using Python 3.14.7 and pytest 8.3.5. The result was 58 passed in 0.07s. The tested code was committed as e680e44b7d3adb61b92a4531f94e9473883bfb29.

[query-tests]: https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/tests/test_queries.py
[listing-service]: https://github.com/LoserWithAGame/st1-assignment-3/blob/e680e44b7d3adb61b92a4531f94e9473883bfb29/project/smartcare/services.py

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: [ I checked that the query uses the appointment list, pracitioner ID and optional status passed into it. It builds a seperate list and sorts it using the named key. It reads appointment fields without changing them. It has no keyboard input, printing or hidden store access. The service gets records from the shared store before calling the query. ]
What the tests do and do not establish: [ The tests check selection, filtering ordering, object identity, fresh lists and unchanged inputs for the supplied cases. They found a problem with spaces around a practitioner ID, which was fixed and retested. Seperate console and workflow evidence in part D ios still needed to show the features working together through the menu.]



## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | | | | |
| UI-02 invalid-input recovery | | | | |
| Automated service workflow | | | | |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: <!-- paste or accessible reference -->
Actual response: <!-- accessible reference -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| | | | | | |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? [ One concern was making sure the menu and services use the same store for the whole session. If each menu choice created a new store, the patient I just registered would be missing when I tried to book an appointment. The console reads the input, the service checks the request, and the query filters and sorts the appointments.]
2. Which Copilot suggestion did you reject as over-engineering, and why? [ I have not recorded a GitHub suggestion that i rejected as over-engineering. The changes I worked through were needed for the Stage 9 requirements, such as returning a new list and accepting spaces around practitioner IDs. I would need to check the group's Copilot review for an actual rejected suggestion before giving an example.]
3. How did you prove cancelled appointments remain retrievable and listable in the same session? [ I wrote a testthat books A1, cancels it, and checks that the same appointment is still stored with CANCELLED status. It also checks that A1 appears in the all-status and cancelled lists, but stays out of the scheduled list. At first, the test failed because entering spaces around D1 returned an empty list. I fixed the service to use the ID from the registered practitioner object. The test then passed, and the full suite finished with 58 passed. ]

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? [ It works with the inputs it is given them unchanged. For example, if it sorted the original list or changed an appointment's status, it would affectdata outside the result it returns. ]
2. Which explicit inputs are needed, and why avoid a global store? [ It needs a list of appointments, the practitioner ID and an optional status. Passing these in makes testing easier because I can give the function the exact data I want to check. ]
3. How can a new list reuse Appointment objects safely? [ The new loist can refer to the same appointments. Changing the order of the new list leaves the original list in its own order. The query still needs to leave the appointments themselves uncahnged because both lists use those objects. ]
4. Why use a named key, and what breaks equal-time ties? [ The named key gives us one clear sorting rule that we can test. Appointments are sorted by date and time first. If those match, the appointment ID decides which comes first. ]
5. How do default and explicit status filters differ? [ If I leave the status out, I get all appointments for that practitioner. If I choose cancelled, I only get their cancelled appointments. ]
6. How do empty, unknown practitioner and invalid filter cases differ? [ An empty list means the practitioner exists but has no appointments matching the request. An unknown practitioner raises LookupError. An invalid filter raisesValueError. The service expects an AppointmentStatus value or None. ]
7. Which console errors recover, and how is unchanged state checked? [ The menu should show a message and let the user continue after things like a wrong ID, duplicate ID, bad date or invalid choice. I would check that the original records are still there with the same details, then try a valid action. For a rejecting booking, I would also check that it was never stored. ]
8. What is data integrity for registered participants, conflicts and history? [ A booking should use the patient and practitioner objects already regisdtered in the store. It should reject a secon d scheduled booking for the same practitioner at the same time. After cancellation, the appointment should stay in the store so its history can still be found. ]
9. What is Copilot's review role, and who verifies findings? [ Copilot can help spot possible issues and suggest tests. We still need to check sugggestions against the requirements and actual code. The person reviewing the change is responsible for checking the evidence before accepting it. ]
10. How do pure functions and OOP responsibilities work together? [ Each part has a job. The object hold their details and rules, the store keeps the records, and services coordinate actions. The pure functions can then filter and sort the appointments they recieve. The console asks the user questions and displays the results. ]

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
