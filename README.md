# rekrutacja-daftcode
Zadanie rekrutacyjne dla Daftcode. Rozwiązanie składa się z dwóch części: API i przykłądowego interfejsu graficznego służącego pokazaniu funkcjonalności API.

## Dokumentacja API

Komunikacja z API przebiega za pomocą zapytań RESTowych. Dane przesyłane są w formacie json.

### Uwierzytelnianie

Część API jest dostępna tylko dla uwierzytelnionych urzytkowników. Razem z zapytaniami do tej części API należy wysłać token uwierzytelniający.

Wygeneruj token
> **POST** `/auth/token`
> Dane: 
> - login: nazwa urzytkownika
> - password: hasło do konta
> Odpowiedź:
> - token: token uwierzytelniający do przyszłego użycia

> Przykładowe zapytanie:
```json
{
    "login": "Kate",
    "password": "Kate",
}
```
> Przykładowa odpowiedź:
```json
{"token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA"}
```

## Dokumentacja GUI

WIP

## Dokumentacja CLI

Po stronie serwera można wywołać następujące komendy:

`flask init-db [--clear/--no-clear] [--src=PATH]`
    Utwórz potrzebne tabele w bazie danych (nie tworzy tych które już istnieją)

    **--clear__/__--no-clear**
        Wyczyść bazę i utwórz tabele od zera. Domyślnie: **--no-clear**

    **--src__=PATH**
        Dodaj do bazy rekordy z plików .csv znajdujących się w folderze PATH. Przykładowy zestaw plików znajduje się w folderze test-db.
