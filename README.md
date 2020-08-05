A Rest API which scrapes data from [CoronaBD](https://corona.gov.bd) website using Flask.
Make a `GET` request to `/` and get the json data.

JSON Sample:

```
{
  "data": {
    "new_cured": "১৮৯০",
    "new_death": "৩৩",
    "new_infected": "২৬৫৪",
    "new_test": "১১১৬০",
    "total_cured": "১৪১৭৫০",
    "total_death": "৩২৬৭",
    "total_infected": "২৪৬৬৭৪",
    "total_test": "১২১২৪১৬"
  },
  "source": "https://corona.gov.bd/"
}
```
