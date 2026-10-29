# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | [response] | [response] | [response] |
| FR-05 Prevent practitioner conflict | [response] | [response] | [response] |
| FR-06 Cancel appointment | [response] | [response] | [response] |
| FR-07 Retain cancelled history | [response] | [response] | [response] |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert appointment is not None`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert len(results) > 0`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract:

|Scenario|Input or starting state|Expected result|Supporting contract|
|---|---|---|---|
|Blank Identifiers|search using patient_id: "" (empty string)|Raise ValueError, with message saying this field cannot be empty.|The patient lookup requires IDs to be non-blank strings.|
|Whitespace-only names|Attempting to register a new user with name as: "   " <- empty space OR "\n\n" <- new line|ValueError is raised and no new patient is stored.|patient name is a requirement so it must contain non whitespace text.|
|Same-time practitioner bookings|IF  A1 <- appointment is SCHEDULED for pracitioner D1 at 10:00 AM. Try booking A2 for D1 at the same time and date.|ValueError is raised, A2 is not stored and A1 remains unchainged and still booked.|Fr-05 rejects a bookinjg if that doctor already has a SCHEDULED appointment at the same time.|
|Cancelled appointments|Cancel SCHEDULED appointment A1, then attempt to find it|reutrn that same appointment but with cancelled status instead of booked. Hisotry needs to remain|FR-07 retain cancelled history|
|Invalid status transitions|attempting to cancel a finished appointment.|Should give a ValueError and leave the appointment unchanged.|Only SCHEDULED appointments can be cancelled.|

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | [By checking an object is not None only proves that something was returned. it could still therefore be the wrong patient] | [Register a patient, look up their ID and verify that the results is the same exact registered patient that was registered.] |
| 2 | [An object being not None does not prove the cancellation worked or history was retained.] | [Cancel a SCHEDULED appointment, then check its status is CANCELLED and that the lookup returns the same previusly stored appointment.] |
| 3 | [Assert True checks nothing abuot the program's result, so incorrect bnehaviour could still pass if not checking other paremiters.] | [Attempt a booking that connflicts with a current appointment for the same practitioner at the same date and time. Check that a ValueError is raised and no new appointments were stored as a result.] |
| 4 | [SMS notifications are not part of requirment scope of the program features. So its checking invented behaviour.] | [Reject the sms test. Change to an alternative test that validates the booking appointment status was changed to SCHEDULED and the actual registered patient and pratitioner objects exist.] |
| 5 | [This also tests a feature called SMS notification that is assumed to exist. Passing this test does not establish that the rules are working correctly.] | [Reject the SMS test. An alternative test could be checking that repeated cancellations raises ValueError and leaves the cancelled appointment unchanged and retrievable as requested.] |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[response]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [code used to test: python -m pytest -v] | [project/] | [2fba9705ec1baabf68b34fd0b74a200cd5bdca8b] | [32] | [0] | [No failure observed] | [Current baseline: All collected cancellation, patient/practitioner lookup and starter test cases passed.] | [baseline run using puthon 3.14.7 and pytest 8.3.5. All 32 collected cases passed. REPLACE THIS PART -> PENDING comment of 32 passed tests to the comment section when uploading. then link that comment here <- pending] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
[Is the program behaving according to its stated requirements? for example, does it reject a conflicting booking when someone attempts to book an appoitment with the same practitioner at the same date/time.]

2. What question does validation answer?
[does the program meet the intented use of the users needs. for exampple can the staff that book appointments do those tasks effectively.]

3. What is a unit test?
[A unit test is a small specific tesst to varify behaviour. for example, it should check that when registering a patient that the name field is not empty.]

4. What is a pytest fixture?
[A fixture provides reusable setup for tests. IT can create fresh store and objects for each test, thus helping prevent tests from affecting one another.]

5. What is parametrisation in pytest?
[Parametrisation runs the same test function multiple times using different set of data inputs. By providing a list of arguments you can test many variables.]

6. What is regression testing?
[regression testing means rerunning tests that prevously done after adding changes to check that the behaviour still works as intended and nothing broke.]

7. What does code coverage tell us, and what does it not prove?
[Code coverage shows witch parts of the code executed during testing. IT can help dientify untested areas. It does not prove that expected results are correct.]

8. What makes an assertion weak?
[An assertion is weak when an incrorect results could still pass. When testing passes but fails to prove that the system is corking correctly or not.]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[Copilot can be used to suggest test cases and assertions. We must check that they match the correct checks that provide meaninful results. Github copilot can be used to brainstorm and apply critical thinking to the project.]

10. What is the Stage 7 engineering rule?
[A passing test should contain meaninful assertions linked to the current requirements. Passing alone does not prove the test was good.]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
