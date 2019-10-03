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

```python
ciphertext_b64 = "/lb0WZDpaIDJVJwy+Q04LCqERqVj7AUItWGREJuXJeWtZN77yP6grehn1gRif31hjTEjLNFyxESweea81/QluWUyhZV9vmabm8NYkkSc6JJWuylGJKQJzA/wC2cM2ScrQQ8gV7GcnVyBCh7eq/N0jUm/L4xrX6IUIDi5CAkVZ9xSS5Tb4o01onOTbGWLd1EZwzZOMlq88wsTPZ6zY7dqj+LKq3Pj6SKlZfaR9eo6PXrRUOARCe9sQVtWVKc5DJfI"
key = b"\xba\xda\x55 HackerMan \x13\x37"
iv = b"\x00"*16

ciphertext = b64decode(ciphertext_b64)
cipher = AES.new(key, AES.MODE_CBC, IV=iv)

plaintext = cipher.decrypt(ciphertext)

print(plaintext)
```

gir oss "b'5!tX\t\x15\x0cD\x05\x0c\n\x1c\x06\x1aU\x05erer! Du klarte det! Beklager, men denne gangen har vi ikke laget flere oppgaver. H\xc3\xa5per du vil s\xc3\xb8ke jobben. Hvis du blir ansatt kan vi love deg mange utfordrende oppgaver.\x03\x03\x03'"

De første 16 bytene er AES CBC-blocken som har blir XOR'et med IV'en. Resten fra og med "erer!" er lesbart fordi det er bare i første block at en ukjent faktor ligger.

Vi må finne hva som skal stå i "plain.txt" og spesifikt i første 16 bytes (første block).
"erer!" er kanskje "Gratulerer!". Men "Gratul" er bare 6 bytes. Mangler 10 for å ha en block. Prøver å padde litt med "xxxxxxxxxxGratul" i plain.txt og kjøre "encrypt.py" på nytt, og printe ut IV.

Får da IV "er uate!k,mngn i". Chifferen som blir generert er fortsatt feil...

Bruker denne IV'en i decrypt.py istedet for `\x00"*16` (blank).

Får da en lesbar tekst:

'PST-haien gratulerer! Du klarte det! Beklager, men denne gangen har vi ikke laget flere oppgaver. H\xc3\xa5per du vil s\xc3\xb8ke jobben. Hvis du blir ansatt kan vi love deg mange utfordrende oppgaver.'

Putter "PST-haien gratul" i "plain.txt" ("Gratulerer" var visst feil) og kjører "encrypt.py" på nytt, og får lik chiffertekst som den på TwitterH4i-kontoen :)

Min lille chiffer: "Yg+8drmNN/giyyL10whyPey06N63YpMb8lUC3p3Agp1VZVxp1hsqUcbOU3WBnNxVS6iY1IzhqVG3v8xFN1/wkjmXGS2Oh4Vo9/sHO1D2ZFajeaVz75rRVvDRxoMF9wExXwN1gTe0iG1Bszett0dL0A=="

IV: "udsfvrt mm v eei"
Tekst: "PST-haien lever! Kudos for varierte og morsomme oppgaver. Keep em coming!🕵https://gph.is/1Sjcgph"
