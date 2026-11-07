# Stage 8 local verification evidence

Source ZIP: `st1-assignment-3-debug-stage08.zip`, GitHub branch `debug/stage08`, snapshot commit `7c56089ca9eacfb3db15f857724fe9e967bf6a59`.

Tests were executed locally with Python 3.13.5 and pytest 9.0.2, from `project/`. The approved Stage 7 project README requests Python 3.13 and pytest 8.3.5; rerun in the approved environment before integration.

Test order:
1. `00` prepared full suite: 5 failures, 29 passed.
2. `01` F8-01 focused baseline: 2 failures.
3. `02` F8-02 focused baseline: 3 failures.
4. `03` F8-01 after its single minimal repair: 2 passed.
5. `04` F8-02 after its minimal repair (both faults now fixed): 3 passed.
6. `05` all supplied tests before refactor: 34 passed.
7. `06` all tests after adding 3 Stage 8 tests but before refactor: 37 passed.
8. `07` focused test subset after enum refactor: 14 passed.
9. `08` full suite after refactor: 37 passed.
10. `09` `python main.py` demo: exit 0.

`data_store.py.diff` is the precise cumulative comparison against the original snapshot. It includes both separate functional repair edits and the final style refactor. For an auditable group Git history, commit repairs, new tests and refactor in appropriately scoped steps; the ZIP has no Git metadata and these are **not yet GitHub commits**.

No Stage 6/7 files or existing test files were modified.
