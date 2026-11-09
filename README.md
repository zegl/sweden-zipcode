# Swedish Zipcodes 🇸🇪

![Zip](http://upload.wikimedia.org/wikipedia/commons/e/ee/2_digit_postcode_sweden.png)

En komplett lista med alla svenska postorter och postnummer.

The complete set of zipcodes in Sweden.

## Uppdatera

Postnummer ändras vanligtvis en gång om året, i mars. PostNord publicerar en sammanställning på [denna sida](https://www.postnord.se/vara-verktyg/sok-postnummer-och-adress). Kopiera tabellraderna ur PDF:en till en textfil (t.ex. med `pdftotext -raw`) och kör:

```sh
python scripts/update.py < andringar.txt
```
