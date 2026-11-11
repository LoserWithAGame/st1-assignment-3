# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [Wednesday 4:30pm - 6:30pm Group 1]
Members and UG/PG applicability: [@MastrRoshiiii, @LoserWithAGame, @warunabandara11-wq, @quiet-learner]


## A Release scope and starting SHA

- Release label/version and requirements baseline: SmartCare Stage 12 Common RC1. Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2. The common scope covers registration and lookup, booking and conflict checks, cancellation and retained history, appointment listing, and the console.
- Common starting SHA / branch / applicable members: 'f615f78795d031f8b525a7a388e9c340ac296a61', doc/stage12, @MastrRoshiiii
- PG starting SHA / branch / applicable members or not applicable: [N/A]
- Working-state review and approved integration: Stage 9 console and appointment listing work was merged into main through PR #35. An independent test run on the exact starting commit returned 38 passed in 0.06 seconds using Python 3.14.7 and pytest 8.3.5.
- Protected common candidate and PG differences: The common starting point is pinned to 'f615f78795d031f8b525a7a388e9c340ac296a61'. (No PG members).
- Feature freeze / owner / verifier: Feature Freeze date - 9/11/2026, (Owner TBD), Verifier - @LoserWithAGame


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: I would hold off on releasing. Passing tests show that the tested features work, but another person still needs clear setup instructions. I would finish the README, check the dependency, and document the known limitations. Then I would ask a teammate to set up the project from a fresh copy and run the operation tests before releasing it.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works - FR-07 - common scope | The test cancels appointment A1, then checks that looking it up returns the same appointment with status `CANCELLED`. It passed in the 38-test suite. | 'test_cancellation.py', line 18, at 'f615f78795d031f8b525a7a388e9c340ac296a61' | Team reviewer pending | Yes for the behaviour tested. Release review is pending. | Independent check pending. Reviewer should rerun the cancellation history test on the final release. |
| Architecture responsibilities are appropriate — common scope | `domain.py` decides when an appointment can be cancelled. `data_store.py` keeps the records. `services.py` finds the appointment and asks it to cancel. `queries.py` filters and sorts a new list without changing the original records. `console.py` asks for input and displays the results. | These five files are in `project/smartcare` at `f615f78795d031f8b525a7a388e9c340ac296a61`. | Team reviewer pending | Yes for the separation shown in the code. Independent review is pending. | Team member should follow one cancellation and one appointment listing through the code, then record their name and findings. |
| Rescheduling is safe — PG only | N/A | N/A| N/A | N/A | N/A |
| AI use is responsible — common scope | In Stage 8, Copilot suggested that the practitioner comparison was reversed. I checked the `!=` comparison against both failing behaviours before accepting the suggestion. After the repair, all three focused tests passed. | [Stage 8, Part F](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/stage08/stage08_activities_and_evidence.md#L295), SHA `f615f78` | @MastrRoshiiii checked the Stage 8 diagnosis. Stage 12 reviewer pending. | Yes for this example. Final release recheck pending. | Verifier to review this evidence in Part E and record their decision - approved/declined. |
| System is maintainable — common scope | The Stage 8 refactor uses `AppointmentStatus.SCHEDULED` in the conflict check so the code uses the same status value as the rest of the project. All 37 tests passed before and after the refactor. | [Conflict check](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/data_store.py#L112), SHA `f615f78`. Test evidence is in Stage 8, Part H. | Stage 12 reviewer pending | Partly. The code change is supported by tests, but the project README still lists completed work as TODOs in Part F. | Update the README in Part F, reviewer to follow it from a clean copy and record the result. |
| FR-01–03 register/find and validation — common scope | Tests check that registered patients and practitioners can be found, duplicate registrations leave the original records in place, and invalid or unknown lookup IDs raise the expected errors. These tests passed in the 38-test suite. | [Registration tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_starter.py#L61) and [lookup tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_services.py#L19), SHA `f615f78`. | Stage 12 reviewer pending | Yes for the automated checks listed. Console verification is pending. | In Part D, a team member can demonstrate registering and finding a patient and two practitioners, then show that the console can recover from a failed lookup. Results should be recorded as pass/fail. |
| FR-04–05 booking and conflict rules — common scope | The tests show that a valid booking succeeds, a booking with an unknown patient is rejected, and the same practitioner cannot be booked twice at the same time. A different practitioner can take a booking at that time (AC-04.2). These tests passed in the 38-test suite. | [Booking and conflict tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_starter.py#L101), SHA `f615f78`. | Stage 12 reviewer pending | Yes for the automated checks listed. Console verification is pending. | In Part D, show a valid booking, a rejected double-booking, and a successful same-time booking with a different practitioner. Record the final test run in Part C. |
| FR-06–08 cancellation, history, and lookup — common scope | Tests confirm that looking up a known ID returns the original appointment, cancelling it changes its status to `CANCELLED`, and the same record can still be found afterward. A second cancellation is rejected without removing the record. These tests passed in the 38-test suite. | [Appointment lookup test](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_starter.py#L55) and [cancellation tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_cancellation.py#L18), SHA `f615f78`. | Stage 12 reviewer pending | Yes for the automated checks listed. Console verification is pending. | In Part D, cancel A1, find it again and show its `CANCELLED` status, then try cancelling it a second time and record what happens. Record the final test run in Part C. |
| FR-09 and QRY-01–04 / FP-01–03 — listing, filtering, ordering, and purity — common scope | A focused check showed that the query returned a new list containing the original appointment objects, sorted by date/time and then ID. Status filtering worked, and the original records stayed unchanged. A known practitioner with no bookings returned an empty list, while an unknown ID raised `LookupError`. | [Query code](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/queries.py#L15) and [listing service](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/services.py#L160), SHA `f615f78`. | Stage 12 reviewer pending | Partly. The checks passed for `D1`, but ` D1 ` returned an empty list. | Record the spaces-in-ID issue in Part H. After fixing it, test both inputs and record the result in Part C. Show listing and filtering through the console in Part D. |
| UI-01 and UI-02 — full console sequence and error recovery — common scope | An independent console check covered registering and finding records, booking, rejecting a double-booking, cancelling and finding the same appointment, listing appointments, and exiting. The menu kept working after invalid choices, dates, statuses, and unknown IDs. | [Console menu](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/console.py#L72), SHA `f615f78`. Ran `python -B main.py --interactive` from `project`. | Stage 12 team reviewer pending | Yes. The main workflow and error recovery worked. | Record the console walkthrough in Part D. Track the listing issue in Part H, then repeat that step after the fix. |
| Session-only scope / FR-10 retired — common scope | I registered sample patient `P1`, exited the console, and opened a fresh session. Looking up `P1` returned `Patient not found`. The console also warned on exit that session data would be lost. | [Console menu](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/console.py#L72), SHA `f615f78`. Ran `python -B main.py --interactive` from `project`. | Stage 12 team reviewer pending | Yes for the session-only behaviour checked. | Record the exit and restart demonstration in Part D. List the loss of records on exit as an accepted scope limit in Part G. |
| PG RES and assurance integration | N/A | N/A | N/A | N/A | N/A |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | Python 3.14.7, pytest 8.3.5 | From `project`: `python -B -m pytest -q -p no:cacheprovider` | `055b404c35f2d5e6157ccbfbd043ae1e87638aba` | 38 passed in 0.06 seconds | PS C:\Users\Daniel Spence\OneDrive\Documents\ST1Assessment3\project> git rev-parse HEAD 055b404c35f2d5e6157ccbfbd043ae1e87638aba PS C:\Users\Daniel Spence\OneDrive\Documents\ST1Assessment3\project> python -m pytest -q [100%] 38 passed in 0.05s | |
| Complete PG if applicable | N/A | N/A | N/A | N/A | N/A |
| Affected focused checks after correction — listing with spaces around the practitioner ID | Python 3.14.7 | From `project`, ran `python -B main.py --interactive` with scripted inputs. Booked `A1` for `D1`, then listed using `D1` and ` D1 `. Also checked the listing service directly with both IDs. | `055b404c35f2d5e6157ccbfbd043ae1e87638aba` | Console passed: both inputs returned `A1`. | Console correction: (https://github.com/LoserWithAGame/st1-assignment-3/blob/055b404c35f2d5e6157ccbfbd043ae1e87638aba/project/smartcare/console.py#L163). Evidence is supplied as a PNG under 'ST1Assessment3\Stage12\Image Evidence' showing two tests, one with blank space beside the Practitioner ID. |
| Full integrated recheck — common scope on `main` | Python 3.14.7, pytest 8.3.5 | From `project`: `python -m pytest -q` | `055b404c35f2d5e6157ccbfbd043ae1e87638aba` | 38 passed in 0.05 seconds | See the saved terminal output for the Complete common run above. |
| Prior assertions preserved / reviewed test diff: | The test files were compared between the Stage 12 starting commit f615f78 and the tested main commit 055b404. No test files or assertions changed. The only change inside project was in the console code, and all 38 existing tests still passed. |
| Remaining failure / limitation: | All 38 automated tests passed. The console now lists the correct appointments when a practitioner ID has spaces around it, but calling the listing service directly with D1 still returns an empty list even when D1 has bookings. (Limitation has been adrressed, updated and passed). |


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [response] | [response] | [response] | [response] |
| Valid booking | [response] | [response] | [response] | [response] |
| Same practitioner exact-time conflict rejected | [response] | [response] | [response] | [response] |
| Different practitioner same time allowed | [response] | [response] | [response] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [response] | [response] | [response] | [response] |
| Invalid/repeated cancellation rejected | [response] | [response] | [response] | [response] |
| Default all-status listing | [response] | [response] | [response] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [response] | [response] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [response] | [response] | [response] | [response] |
| Session-only limitation and normal exit | [response] | [response] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [response] | [response] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [rnse]espo | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | `domain.py` line 129, `services.py` lines 146 and 160, and `queries.py` line 15. Checked on `main` at `055b404`. | The appointment decides whether it can be cancelled. The service finds the appointment and asks it to cancel. The query filters and sorts a new list without changing the original records. One issue remains: the listing service passes an ID with spaces to the query, so it can miss existing bookings. | The console now removes the extra spaces. |
| PascalCase and snake_case naming | `services.py` and `data_store.py` | Class names such as `AppointmentService` and `SmartCareDataStore` use PascalCase. Methods and variables such as `list_practitioner_appointments` and `practitioner_id` use snake_case. | The names checked follow the expected style, so no changes were needed. |
| Useful type hints and meaningful docstrings | `queries.py` line 15 and `services.py` line 160 | The type hints show that the listing functions take a practitioner ID and an optional status, and return a list of appointments. The docstrings explain how the list is sorted and what happens when a practitioner is unknown or has no matching appointments. | The type hints and docstrings match the code in the functions reviewed. No changes needed. |
| Four-space indentation and imports/layout | `queries.py` line 4 and `console.py` line 162 | The code reviewed uses four spaces for each level of indentation. Built-in | Four-space indentation and imports/layout | All 11 Python files in the app and tests. Import examples checked in `queries.py` and `console.py`. | All 11 files use four spaces for each block level. The imports checked are grouped clearly. One closing parenthesis in the 'console.py' listing is slightly out of line (line 164). | No indentation changes needed. The closing parenthesis can be lined up with the start of the call as a small fox. |
| Focused methods / duplication / dead or commented code | `console.py`, lines 16, 33 and 95–104 | `parse_date_time()` checks the date and time, and `format_appointment()` prepares the text shown on screen. The menu checks whether the choice is from 0 to 8 twice. The second check can never reject anything because the first check has already rejected every other choice. | Correction to remove the second check. Then try `9` to confirm the menu still shows an error, and `0` to confirm it still exits normally from the original check. |
| Globals / leakage / unnecessary inheritance or frameworks | `console.py` line 72, `data_store.py` lines 18 and 98, and `domain.py` line 26 | Each console session creates its own store. The records are kept inside that store, and listing appointments gives the caller a new list. The app uses built in Python tools, including `Enum` for appointment statuses. No unnecessary frameworks or class layers were found. | No changes needed for this check. Record the console restart in Part D to show that a new session starts with empty records. |
| No SQLite/persistence/repository ABCs/speculative features | `data_store.py` line 18 and `console.py` lines 72 and 107 | SmartCare stores records in memory for one session. The common app uses `SmartCareDataStore` directly, with no database, file saving, or extra storage layer. No unrequested features such as billing or notifications were found. | No changes needed. Use the restart check in Part D as evidence and record session-only storage a sstated in Stage09. |
| Synthetic data / secrets / dependencies / provenance | Project README, `requirements-dev.txt`, Stage 12 screenshot and Stage 8 Part F | We used made-up records in the tests and demo. The files checked showed no obvious passwords or keys. SmartCare runs with standard Python, and pytest 8.3.5 is used for testing. The README shows where the project started, Git shows what the team changed, and Stage 8 Part F explains how we checked Copilot’s advice. | No corrections or chnages needed. |
| Significant common Copilot contributions and human verification | Stage 8 Part F and the focused test results in Part G | Copilot suggested that the lookup was skipping cancelled appointments and that the booking check was comparing the wrong practitioners. We checked both ideas against the code and the failing tests. After the fixes, the two cancellation tests and three booking conflict tests passed. | We accepted both suggestions because the code and test results supported them. |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | N/A | N/A | N/A |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| Copilot said the booking check looked at the wrong practitioner. | FR-05 — prevent double booking | We read the code and checked the failing tests. | Accepted. The code checked for a different practitioner instead of the same one. | We fixed the check. All 3 focused tests passed. |
Access route or approved equivalent / limitations: We used GitHub Copilot Chat in VS Code. It gave us ideas about what might be wrong. We checked those ideas ourselves using the code and tests.
Available AI evidence and missing evidence honestly disclosed: Stage 8 Part F has the prompts we sent and notes on how we checked Copilot’s suggestions. Part G has the test results. We haven’t added links to the original Copilot replies yet as I was not sure how to link the reponses.


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | Root README, lines 3 and 34, and project README, line 14 | @LoserWithAGame — check pending | The READMEs explain what SmartCare is and that it keeps records for one session. Add a short list of what this release includes: registration and lookup, booking, cancellation with history, appointment listing, and the console menu. Our group is UG, so only the common scope applies. |
| Out-of-scope capabilities and known limitations | Project README, line 14, and root README, line 30 | @LoserWithAGame — check pending | The README already explains that records are cleared when you close SmartCare. SmartCare doesn’t include logins, billing, reminders or rescheduling. |
| Confirmed teaching Python version and dependency installation | Project README setup instructions and `requirements-dev.txt` | @LoserWithAGame — check pending | The course setup lists Python 3.13 and pytest 8.3.5. Our Part C run passed on Python 3.14.7. |
| Working directory / demo / interactive / test commands | Root README, line 47, and project README, line 5 | @LoserWithAGame — check pending | Both READMEs explain that commands run from the `project` folder. They list `python main.py` for the demo and `python -m pytest` for the tests. We should include `python main.py --interactive` so users know how to open the menu. |
| Repository structure and architecture responsibilities | Root README, lines 38–45, and project README, line 16 | @LoserWithAGame — check pending | The root README helps users find the app setup and each stage’s evidence. The project README explains where the rules, records and services live. Add that `queries.py` filters and sorts appointments, while `console.py` handles what the user types and sees. |
| Responsible AI summary / synthetic-data rule | Root README, line 56, and project README, line 14 | @LoserWithAGame — check pending | Both READMEs say to use made-up records. The root README also says to check Copilot’s suggestions. We compared its advice with the code and test results before accepting it. See Part E for the example above. |
| Release label/version and SHA links | Root README, line 14, and Stage 12 Parts A and K | @LoserWithAGame — check pending | Part A names the release `SmartCare Stage 12 Common RC1`. Once the final version is tested, add that label and a link to the tested commit in the README. |
Root README index and project/README verified: All eight links in the root README point to files that exist. The project README explains how to install pytest, run the demo, and run the tests. It still needs the interactive menu command, python main.py --interactive. The fresh-copy check by a teammate is pending.
Fresh clone or extracted ZIP / candidate identity: The project folder was exported from main at commit 055b404c35f2d5e6157ccbfbd043ae1e87638aba and tested in a separate folder. A teammate still needs to check the final submission from a fresh clone or the full source ZIP.
Verifier and clean environment / actual version: @LoserWithAGame is the nominated verifier, and their check is pending. The extracted copy was tested using Python 3.14.7 and pytest 8.3.5 in an existing environment.
Setup/run/test commands and observed results: From the extracted project folder at 055b404, python main.py showed the sample appointment, and python main.py --interactive opened the menu and exited normally when I chose 0. python -m pytest -q returned 38 passed in 0.07 seconds. This check used an existing Python 3.14.7 environment with pytest 8.3.5.
Missing local file or setup gap / remedy and recheck: The extracted copy had all the files needed to run the app and tests. The project README still needs python main.py --interactive so users know how to open the menu.


## G Known limitations debt and release notes

- Delivered features: Register and find patients and practitioners, book and cancel appointments, and view appointment history through the menu.
- Important fixes: Cancelled appointments can still be found, and a practitioner can’t be booked twice at the same time.
- Architecture/quality improvements: We kept the menu, records and booking rules separate so the code is easier to follow and test.
- Known limitations: SmartCare is for practice with made-up records. All records are cleared when the app closes.
- AI-assisted development note: We used Copilot to help spot problems and checked its suggestions against the code and tests.

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| The menu checks the number range twice | Unnecessary repeat of code | low | Remove the extra check and test the menu afterwards | Yes. The menu still handles the out of range choice |
Session-only synthetic data and minute-precision local time: We use made-up records. They’re cleared when the app closes, and appointments use local time without seconds.
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: Logins, staff permissions, a patient portal, reminders, billing, insurance and AI medical advice are outside this release.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: The app is built for one person using the menu at a time. A real clinic would need support for more users, time zones, monitoring and accessibility checks.
Difference between accepted scope limit and unresolved required behaviour: Clearing records on exit is expected. Showing the wrong appointments is a bug that needs fixing and testing again.
PG assurance residual risks / owner / status or not applicable: N/A


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| FR-09: List a practitioners appointments | D1 shows bookings in the menu. On main, calling the listing service directly with D1 still returns an empty list. | Medium. A valid ID can show no bookings when the service is called directly. | @quiet-learner: Fix the direct service for when appointments are called directly. | The console change removes spaces from the ID. | The console check and all 38 tests passed on 055b404. After the service fix is merged, check both IDs directly and rerun the full suite. | The direct service issue is still present. |
Justified no-change conclusion if no defect found: N/A - Defect still present in the direct listing.
Release blockers still open / status: The service fix still needs to be merged into main and tested.


## I Git review and integration evidence

- Issue / PR / diff links and reviewed SHA — The listing fix and new tests were reviewed at 03ebe1e387ec3214250225fcb59dfee006c40160. The Stage 12 evidence was added through separate PRs. [Listing fix and tests](https://github.com/LoserWithAGame/st1-assignment-3/pull/42/changes) · [Part C](https://github.com/LoserWithAGame/st1-assignment-3/pull/41) · [Parts E and F](https://github.com/LoserWithAGame/st1-assignment-3/pull/43) · [Part D](https://github.com/LoserWithAGame/st1-assignment-3/pull/45)
- Independent reviewer / feedback / response: @LoserWithAGame approved the listing fix and the Part C, E and F updates. The feedback was positive and requested no changes. [Fix approval](https://github.com/LoserWithAGame/st1-assignment-3/pull/42#pullrequestreview-5839735196), [Part C approval](https://github.com/LoserWithAGame/st1-assignment-3/pull/41#pullrequestreview-5839743133), [Parts E and F approval](https://github.com/LoserWithAGame/st1-assignment-3/pull/43#pullrequestreview-5850504609)
- Integration commit / full recheck: Tested main at 1d268dbe3e01d90f67935c187498554590cfb8eb. From project, python -B -m pytest -q -p no:cacheprovider returned 58 passed in 0.09 seconds using Python 3.14.7 and pytest 8.3.5. The focused test for IDs with spaces also passed. [Integrated commit](https://github.com/LoserWithAGame/st1-assignment-3/commit/1d268dbe3e01d90f67935c187498554590cfb8eb)
- Tracked and untracked file inspection / cleanliness: Tracked and untracked file inspection / cleanliness — The files in the extracted copy were checked. Before I make the final ZIP, I’ll run git status --short to check for any unfinished changes or extra files.
- Secrets/staff material/caches/tool-metadata exclusion check: The file check found no .env files, key files, caches, virtual environments or Stage 8 setup files in the extracted copy.
- Candidate recovery plan / known-good SHA: 1d268dbe3e01d90f67935c187498554590cfb8eb is a known-good SHA. If a later change breaks the app, start a recovery branch from this commit and rerun the full-suit tests.
- Named substantive contributions: @MastrRoshiiii recorded the Part C tests and screenshot and completed Parts A, B, C, E, F, G, H, I, L and part;y N. @quiet-learner fixed the listing issue and added query tests. @LoserWithAGame completed Part D, J, M, and N and reviewed the changes and merged them. @warunabandara11-wq contributed the Stage 8 repairs and regression tests carried into this release.


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA — 1d268dbe3e01d90f67935c187498554590cfb8eb. The full suite passed all 58 tests on this commit. See Part C for the test details on previous suite before fixes.
Exact PG tested SHA or not applicable: N/A
Final submitted SHA / repository URL: The submitted SHA is pending until the final changes are merged.
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification — After the earlier 38-test run, the practitioner listing fix and new tests were merged. The focused test passed, and the full rerun passed all 58 tests. If the code changes again before submission, we will rerun the tests and record the new SHA.
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [x] Feature freeze and scoped requirements traced.
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [x] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [x] Release notes, technical debt and limitations visible.
- [x] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [x] project/ source and all accumulated applicable tests included.
- [x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [x] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [x] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [x] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]


## N Reflection viva and handover

- Strongest evidence SmartCare is ready: All 58 tests passed on the version we checked. That included the test for finding appointments when the practitioner ID has extra spaces.
- Weakest area: The setup instructions still need a user to try them from a fresh copy. I’d like to know they can get the app running without asking us for help.
- How AI use changed from Stage 1 to Stage 12: Some members used AI to help with understanding questions and used in the AI ON parts. By stage 12 it was only used when a part prompted its use and to clarify questions and tasks.
- Start doing — engineering and AI use: Write down what I expect to happen before asking AI for help. Save the test result and commit SHA as soon as I run the test.
- Stop doing — engineering and AI use: Leaving the evidence until the end and having to go back to find which version we tested.
- Continue doing — engineering and AI use: Make small fixes, test the problem we fixed, and ask a teammate to review the change.
- What worked / caused rework / future delivery improvement: Working on separate branches helped us share changes. We lost time going back to find old test results and commit SHAs. Next time, I’d record them as we go.
- One paragraph — If AI can write code why do we still need software engineers: AI can give us code to try. We still need people to understand what the software should do, check that it works, and decide when it’s ready. In SmartCare, Copilot suggested what might be wrong with the booking check. We had to read the code and run the tests to find out if it was right.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
