# Automated Reports
## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
CLI/__init__.py             0      0   100%
CLI/cli.py                144     54    62%   34, 36, 38, 40, 44, 62-66, 104, 119, 123-165, 169-186, 233-240
core/__init__.py            0      0   100%
core/dice.py               20      0   100%
core/juego.py              87      4    95%   113, 121-123
core/jugador.py            25      3    88%   33-35
core/tablero.py           111     13    88%   34-41, 81, 91, 150-153, 169-172, 179
tests/__init__.py           0      0   100%
tests/test_cli.py          40      0   100%
tests/test_dice.py         29      0   100%
tests/test_juego.py       170      2    99%   314-315
tests/test_jugador.py      24      0   100%
tests/test_tablero.py     150      0   100%
-----------------------------------------------------
TOTAL                     800     76    90%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
