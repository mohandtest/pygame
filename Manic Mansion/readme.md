# Manic Mansion
Dette er Manic Mansion, et enkelt spill der du kontrollerer en karakter som prøver å redde sauene sine mens du unngår hindringer og spøkelser. Her finner du all nødvendig informasjon for å komme i gang med spillet.

![bilde](https://github.com/mohandtest/pygame/assets/112395083/7ece265d-a33b-4802-a26b-8ac222de3b83)

### Installasjon
#### 1. Klon eller last ned repo'et
I git:
```bash
git clone <repository-url>
```

#### 2. Installer pygame
   
```bash
pip install pygame
```

*alternativt åpne terminalen i samme mappe og skrive:*

```bash
pip install -r requirements.txt
```

### Hvordan Spille
Ditt mål er å redde så mange sauer som mulig uten å bli fanget av spøkelser.

Bruk piltastene for å bevege karakteren din opp, ned, venstre eller høyre på spillbrettet.

Karakteren din starter på venstre side av brettet og må navigere til høyre side for å redde en sau. Unngå å kollidere med hindringer og spøkelser, da dette vil avslutte spillet. Etter å ha reddet en sau, returnerer karakteren din til venstre side for å gjenta prosessen.

Hver gang du redder en sau og returnerer til venstre side, tjener du ett poeng.

Spillet avsluttes hvis karakteren din kolliderer med en hindring, et spøkelse, eller hvis du prøver å redde en annen sau mens du allerede bærer en.

### Tilpasning
Du kan gjerne tilpasse spillet slik du ønsker! Dette var hovedsaklig en skoleoppgave men også en fin måte å bli flinkere med pygame.