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
tests/testScreen.py        32      1    97%   55
tests/test_cli.py          40      0   100%
tests/test_dice.py         30      0   100%
tests/test_juego.py       172      3    98%   326-329
tests/test_jugador.py      24      0   100%
tests/test_tablero.py     150      0   100%
-----------------------------------------------------
TOTAL                     847     79    91%

```
## Pylint Report
```text
************* Module core.tablero
core/tablero.py:112:0: C0301: Line too long (109/100) (line-too-long)
core/tablero.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/tablero.py:66:4: R1260: 'movimiento_valido' is too complex. The McCabe rating is 14 (too-complex)
core/tablero.py:1:0: C0115: Missing class docstring (missing-class-docstring)
core/tablero.py:1:0: C0103: Class name "board" doesn't conform to PascalCase naming style (invalid-name)
core/tablero.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
core/tablero.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
core/tablero.py:50:4: C0116: Missing function or method docstring (missing-function-docstring)
core/tablero.py:66:4: R0911: Too many return statements (13/8) (too-many-return-statements)
core/tablero.py:145:4: C0116: Missing function or method docstring (missing-function-docstring)
core/tablero.py:176:4: C0116: Missing function or method docstring (missing-function-docstring)
core/tablero.py:183:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.jugador
core/jugador.py:50:0: C0304: Final newline missing (missing-final-newline)
************* Module core.juego
core/juego.py:60:4: R1260: 'jugar_turno' is too complex. The McCabe rating is 11 (too-complex)
core/juego.py:6:0: C0411: standard import "random" should be placed before first party imports "core.dice.Dice", "core.tablero.board", "core.jugador.Jugador"  (wrong-import-order)
core/juego.py:6:0: W0611: Unused import random (unused-import)
************* Module core.dice
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/dice.py:6:0: C0115: Missing class docstring (missing-class-docstring)
core/dice.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
core/dice.py:22:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module CLI
CLI/__init__.py:1:0: C0103: Module name "CLI" doesn't conform to snake_case naming style (invalid-name)
************* Module CLI.cli
CLI/cli.py:239:0: C0304: Final newline missing (missing-final-newline)
************* Module tests.test_cli
tests/test_cli.py:17:48: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_cli.py:23:44: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_cli.py:30:40: W0613: Unused argument 'mock_input' (unused-argument)
************* Module tests.test_jugador
tests/test_jugador.py:12:33: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_jugador.py:24:32: W0613: Unused argument 'mock_input' (unused-argument)
************* Module tests.test_tablero
tests/test_tablero.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_tablero.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_tablero.py:65:16: W0612: Unused variable 'mensaje' (unused-variable)
************* Module tests.test_juego
tests/test_juego.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_juego.py:6:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_juego.py:74:38: W0613: Unused argument 'mock_print' (unused-argument)
tests/test_juego.py:74:50: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_juego.py:87:39: W0613: Unused argument 'mock_print' (unused-argument)
tests/test_juego.py:87:51: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_juego.py:175:41: W0613: Unused argument 'mock_print' (unused-argument)
tests/test_juego.py:240:47: W0613: Unused argument 'mock_print' (unused-argument)
tests/test_juego.py:260:55: W0613: Unused argument 'mock_print' (unused-argument)
tests/test_juego.py:276:13: W0612: Unused variable 'mock_board' (unused-variable)
tests/test_juego.py:322:12: C0415: Import outside toplevel (core.juego) (import-outside-toplevel)
tests/test_juego.py:325:12: W1503: Redundant use of assertTrue with constant value True (redundant-unittest-assert)
tests/test_juego.py:327:12: W0105: String statement has no effect (pointless-string-statement)
tests/test_juego.py:329:69: E0602: Undefined variable 'error' (undefined-variable)
tests/test_juego.py:322:12: W0611: Unused import core.juego (unused-import)
************* Module tests.testScreen
tests/testScreen.py:29:68: C0303: Trailing whitespace (trailing-whitespace)
tests/testScreen.py:31:68: C0303: Trailing whitespace (trailing-whitespace)
tests/testScreen.py:33:69: C0303: Trailing whitespace (trailing-whitespace)
tests/testScreen.py:39:0: C0301: Line too long (113/100) (line-too-long)
tests/testScreen.py:45:26: C0303: Trailing whitespace (trailing-whitespace)
tests/testScreen.py:52:52: C0303: Trailing whitespace (trailing-whitespace)
tests/testScreen.py:53:0: C0301: Line too long (101/100) (line-too-long)
tests/testScreen.py:1:0: C0103: Module name "testScreen" doesn't conform to snake_case naming style (invalid-name)
tests/testScreen.py:16:4: W0221: Number of parameters was 1 in 'TestCase.setUp' and is now 5 in overriding 'TestScreen.setUp' method (arguments-differ)
tests/testScreen.py:47:12: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
tests/testScreen.py:47:12: E0633: Attempting to unpack a non-sequence (unpacking-non-sequence)
tests/testScreen.py:47:35: W0212: Access to a protected member _tirar_dados of a client class (protected-access)
tests/testScreen.py:5:0: W0611: Unused import pygame (unused-import)
************* Module tests.test_dice
tests/test_dice.py:18:38: W0613: Unused argument 'mock_randint' (unused-argument)
tests/test_dice.py:18:52: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_dice.py:26:38: W0613: Unused argument 'mock_randint' (unused-argument)
tests/test_dice.py:26:52: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_dice.py:33:46: W0613: Unused argument 'mock_input' (unused-argument)
tests/test_dice.py:41:46: W0613: Unused argument 'mock_randint' (unused-argument)
tests/test_dice.py:41:60: W0613: Unused argument 'mock_input' (unused-argument)
************* Module pygame_ui.screen
pygame_ui/screen.py:79:33: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:83:33: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:84:38: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:158:42: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:159:59: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:233:51: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:234:70: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:258:63: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:261:63: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:272:32: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/screen.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pygame_ui/screen.py:257:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)

-----------------------------------
Your code has been rated at 9.12/10


```
