# Car Register – Python 

Car Register er et Python-prosjekt som simulerer grunnleggende funksjonalitet for et bilregister. Programmet inneholder funksjoner for å registrere biler, hente informasjon, beregne leiepriser, finne dato for neste EU-kontroll og beregne totalpris inkludert registreringsavgifter.

Prosjektet er utviklet for å øve på **funksjoner, dictionaries, løkker, betingelser, datohåndtering og grunnleggende objektorientert programmering** i Python.

## Teknologier

- **Python** – Programmeringsspråket som brukes til å utvikle funksjonaliteten.
- **Datetime** – Innebygd Python-modul som brukes til å håndtere datoer og beregne bilers alder.
- **Dictionaries** – Brukes til å organisere og lagre informasjon om bilene.

## Funksjonalitet

Prosjektet inneholder flere funksjoner for å håndtere informasjon og beregninger knyttet til biler:

- **Bilregister** – Lagrer informasjon om biler, inkludert merke, modell, pris, produksjonsdato, tilstand og kilometerstand.
- **Registrering av biler** – Legger til nye biler i registeret med en unik nøkkel basert på merke og modell.
- **Bilinformasjon** – Skriver ut informasjon om en bil.
- **Aldersberegning** – Beregner bilens alder basert på produksjonsåret.
- **Månedlig leiepris** – Beregner leiepris basert på bilens verdi, med et ekstra gebyr for nye biler.
- **EU-kontroll** – Beregner neste kontrolldato basert på en forenklet modell med kontroll hvert andre år.
- **Totalpris** – Beregner bilens totalpris inkludert en registreringsavgift som avhenger av bilens alder og tilstand.

## Hvordan programmet fungerer

Programmet bruker en dictionary (`car_register`) til å lagre informasjon om forskjellige biler. Hver bil har sin egen nøkkel og tilhørende egenskaper.

`print_car_information()` skriver ut informasjon om en bil, inkludert merke, modell, pris, produksjonsdato og om bilen er ny eller brukt.

`create_car()` oppretter en ny bil og legger den til i bilregisteret.

`get_car_age()` beregner bilens alder ved å trekke produksjonsåret fra inneværende år.

`rent_car_monthly_price()` beregner månedlig leiepris basert på en fast prosentandel av bilens verdi. Nye biler får et ekstra månedlig gebyr.

`next_eu_control()` bruker `datetime` og en `while`-løkke for å beregne neste kontrolldato etter prosjektets forenklede regler.

`calculate_total_price()` beregner totalprisen ved å legge til en aldersbasert registreringsavgift. Avgiftssatsene er forhåndsdefinert i programmet.

Prosjektet inneholder også en `Car`-klasse som viser hvordan bilinformasjon og tilhørende funksjonalitet kan organiseres ved hjelp av objektorientert programmering. Klassen har en konstruktør og metoder som foreløpig ikke er implementert.

## Hva jeg har lært

Gjennom dette prosjektet har jeg fått praktisk erfaring med flere sentrale konsepter innen Python:

- Bruk av dictionaries for å lagre og organisere data.
- Opprettelse av funksjoner med parametere og returverdier.
- Bruk av løkker og betingelser.
- Datohåndtering med `datetime`.
- Beregninger basert på ulike betingelser og verdier.
- Bruk av konstanter for faste avgifter og prosentsatser.
- Grunnleggende forståelse av klasser og objektorientert programmering.

## Videreutvikling

Prosjektet kan videreutvikles ved å implementere metodene i `Car`-klassen og flytte mer av funksjonaliteten over til en objektorientert struktur.

Andre mulige forbedringer inkluderer et interaktivt brukergrensesnitt, muligheten til å redigere og slette biler fra registeret og lagring av bilinformasjon i en database.

Prosjektets hovedfokus har vært å arbeide med strukturert databehandling, funksjoner og beregninger i Python, samt å få en introduksjon til objektorientert programmering.
