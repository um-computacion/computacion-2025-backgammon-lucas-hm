# Automated Reports
## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
CLI/__init__.py             0      0   100%
CLI/cli.py                149     55    63%   13, 45, 47, 49, 51, 55, 72-76, 112, 126, 130-168, 172-187, 232-239
core/__init__.py            0      0   100%
core/dice.py               20      0   100%
core/juego.py              90      4    96%   114, 120-122
core/jugador.py            29      3    90%   48-50
core/tablero.py           111     13    88%   34-41, 81, 91, 150-153, 169-172, 179
tests/__init__.py           0      0   100%
tests/testScreen.py        39      0   100%
tests/test_cli.py          40      0   100%
tests/test_dice.py         30      0   100%
tests/test_juego.py       172      3    98%   326-329
tests/test_jugador.py      24      0   100%
tests/test_tablero.py     150      0   100%
-----------------------------------------------------
TOTAL                     854     78    91%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
