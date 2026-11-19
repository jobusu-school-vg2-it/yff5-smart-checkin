# Smart Check-in – elevstartpakke (Windows 11)

## Start i PowerShell i VS Code

1. Installer Python 3.12 eller nyere og VS Code med Python-utvidelsen.
2. Åpne prosjektmappen i VS Code.
3. Kjør disse kommandoene én etter én:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

4. Åpne http://127.0.0.1:5000 i nettleseren.

Du trenger ikke aktivere venv i PowerShell; dette unngår ExecutionPolicy-problemer.

## Oppdrag

- TODO 1 i `app.py`: Kall `save_visit(name, purpose)`.
- TODO 2 i `app.py`: Bruk `get_visits()` til å hente registreringer.
- TODO 3 i `database.py`: Lag INSERT-spørring med parameterverdier.
- TODO 4 i `database.py`: Lag SELECT-spørring, sorter nyeste først, returner `fetchall()`.
- EKSTRA: Implementer utsjekking ved å oppdatere `ut_tid`.
- EKSTRA: Generer QR-kode til en adresse som faktisk er tilgjengelig på testnettverket. Standardoppsettet bruker bare localhost og kan ikke nås fra mobilen.

Test med fiktive navn og besøksformål. Administrasjonssiden er ikke passordbeskyttet. Ikke eksponer løsningen på internett eller et åpent nettverk.

## Test

Registrer fem fiktive besøkende. Sjekk at navn, formål og tidspunkt lagres og vises. Test tomme felter. Test utsjekking dersom du har laget den.
