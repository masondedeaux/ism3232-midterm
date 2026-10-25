# Terminal Record: Harvest Table Catering

## 1. Building the project

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
code .
cd ~/ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
python3 -m pip freeze > requirements.txt
mkdir -p tests
touch business_rules.py main.py commands.md README.md tests/__init__.py tests/test_business_rules.py
printf '.venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n' > .gitignore
git init
git branch -M main
git remote add origin https://github.com/masondedeaux/ism3232-midterm.git
```

## 2. The virtual environment

```bash
which python3
```

```text
/home/mason/ism3232-midterm/.venv/bin/python3
```

The path includes `.venv/bin/python3`, showing that the virtual environment is active.

## 3. The project structure

```bash
tree -L 2
```

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The `__pycache__` folders are on my computer but excluded from GitHub by `.gitignore`.

## 4. Every function and test

```bash
rg 'def '
```

```text
tests/test_business_rules.py
13:def test_food_cost_regular_event():
17:def test_food_cost_with_cents():
21:def test_discount_below_25_guests():
25:def test_discount_at_25_guests():
29:def test_nonprofit_discount_below_100_guests():
33:def test_nonprofit_flag_changes_discount():
38:def test_nonprofit_below_25_has_no_discount():
42:def test_service_fee_at_500():
46:def test_no_service_fee_above_500():
50:def test_no_signoff_at_2500():
54:def test_signoff_above_2500():
58:def test_no_second_chef_at_80_guests():
62:def test_second_chef_above_80_guests():
66:def test_no_second_chef_below_3000():
70:def test_second_chef_at_3000():
74:def test_total_booked_adds_events():
82:def test_total_booked_empty_list():
86:def test_largest_event_uses_discounted_totals():
94:def test_largest_event_keeps_first_when_tied():
103:def test_largest_event_empty_list():
107:def test_format_event_line_no_flags():
112:def test_format_event_line_both_flags():
117:def test_format_event_line_second_chef_only():

commands.md
47:rg 'def '

business_rules.py
12:def calculate_food_cost(guest_price: float, guests: int) -> float:
17:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
27:def calculate_event_total(
39:def needs_signoff(total: float) -> bool:
44:def needs_second_chef(guests: int, total: float) -> bool:
49:def total_booked(events: list) -> float:
59:def largest_event(events: list) -> str:
73:def format_event_line(
```

`business_rules.py` defines eight functions, and `tests/test_business_rules.py` defines 23 tests.

## 5. Which files print

```bash
rg -l 'print'
```

```text
main.py
commands.md
```

`main.py` prints the report. `business_rules.py` returns values without printing. `commands.md` also appears because it contains the recorded `printf` command.

## 6. The commit history

```bash
git log --oneline
```

```text
1854b1f (HEAD -> main) Document catering rules setup and testing
6753766 Complete catering report summary
87306bf Add event and staffing summary counts
15312b2 Print event totals and staffing requirements
cb1dd5d Add catering event records
f5c64ff Add event line formatting and tests
3f0214c Add largest event selection and tests
520bacb Add booking total loop and tests
2d7ad1b Add signoff and second chef rules with boundary tests
14bae13 Add event totals and service fee boundary tests
9abb432 Test nonprofit discount eligibility and guest limits
dbc7f16 Add event discount calculation and guest limit tests
05a7357 Add food cost calculation and two tests
2381d8f Add catering business rule constants
1d54459 Set up midterm environment and project structure
```