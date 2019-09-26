# Oppdatering september 2019 (OBS: SPOILER!!)

Ny stillingsannonse publisert på https://1005007.webcruiter.no/Main/Recruit/Public/4134047982?language=NB med et interessant bilde [f769efc8-3e0f-4cb1-91a8-364328ee231b.jpg](f769efc8-3e0f-4cb1-91a8-364328ee231b.jpg).

Bildet viser et Python-skript som krypterer innholdet i filen `plain.txt` med en kryptografisk nøkkel. En chiffer-tekst blir deretter generert og blir lagt ut på twitter.com/twitt3rhai:

```
/lb0WZDpaIDJVJwy+Q04LCqERqVj7AUItWGREJuXJeWtZN77yP6grehn1gRif31hjTEjLNFyxESweea81/QluWUyhZV9vmabm8NYkkSc6JJWuylGJKQJzA/wC2cM2ScrQQ8gV7GcnVyBCh7eq/N0jUm/L4xrX6IUIDi5CAkVZ9xSS5Tb4o01onOTbGWLd1EZwzZOMlq88wsTPZ6zY7dqj+LKq3Pj6SKlZfaR9eo6PXrRUOARCe9sQVtWVKc5DJfI
```

Nøkkelen som brukes til krypteringen ser vi heldigvis i koden, med kommentar om å huske å slette den senere, så vi kan lage et program som bruker nøkkelen til å decryptere chiffer-teksten.

## Løsning

### Prereq's

1. Installer Python og Pip.
2. Installer Python-modulen `PyCryptodome`: `python -m pip install PyCryptodome`

### Kjør encrypt.py

Lag en fil `plain.txt` og plasser i samme mappe som `encrypt.py`.
Kjør:

```
C:\python encrypt.py
<chiffer-tekst>
```

Programmet åpner `plain.txt` og krypterer det med en nøkkel. En chiffer-tekst vises som output.

Hvis innholdet i `plain.txt` er rikig, skal chiffer-teksten vi får være lik den som er nevnt ovenfor (og lagt ut på Twitter-kontoen).

For å finne ut hva `plain.txt` faktisk inneholdt, må vi lage `decrypt.py` som dekrypterer chiffer-teksten med nøkkelen som ble brukt til å kryptere.

### Kjør decrypt.py
