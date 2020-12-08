# rekrutacja-daftcode
Zadanie rekrutacyjne dla Daftcode. Rozwiązanie składa się z dwóch części: API i przykłądowego interfejsu graficznego służącego pokazaniu funkcjonalności API.

## Dokumentacja API

Komunikacja z API przebiega za pomocą zapytań RESTowych. Dane przesyłane są w formacie json.

### Uwierzytelnianie

Część API jest dostępna tylko dla uwierzytelnionych urzytkowników. Razem z zapytaniami do tej części API należy wysłać token uwierzytelniający.

#### Wygeneruj token
**POST** `/auth/token`

Dane: 
- login: nazwa urzytkownika
- password: hasło do konta

Odpowiedź:
- token: token uwierzytelniający do przyszłego użycia, ważny przez 24 godziny

Przykładowe zapytanie:
```json
{
    "login": "Kate",
    "password": "Kate",
}
```
Przykładowa odpowiedź:
```json
{"token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA"}
```

#### Odświerz token
**POST** /auth/refresh

Dane:
- token: wygenerowany token do odświerzenia

Odpowiedź:
- token: odświerzony token ważny kolejne 24 godziny

Przykładowe zapytanie:
```json
{"token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA"}
```
Przykładowa odpowiedź:
```json
{"token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA"}
```

### Wiadomości

#### Odczyt wiadomości
**GET** /{message_id}/read

Dane:
- brak

Odpowiedź:
- id: numer identyfikacyny wiadomości
- content: treść wiadomości
- edited: data ostatniej edycji/utworzenia wiadomości w formacie "YYYY-MM-DD hh:mm:ss.ffffff"
- views: liczba zapytań o odczytanie wiadomości od ostatniej edycji, licząc z tym zapytaniem

Przykładowa odpowiedź:
```json
{
    "id": 0,
    "content": "Message conten, maximum 160 characters",
    "edited": "2020-10-17 21:37:14.884209",
    "views": "6",
}
```

#### Edycja wiadomości
**POST** /{message_id}/edit

Dane:
- token: token uwierzytelniający
- content: treść wiadomości, nie więcej niż 160 znaków

Odpowiedź:
- id: numer identyfikacyny wiadomości
- content: nowa treść wiadomości
- edited: data edycji w formacie "YYYY-MM-DD hh:mm:ss.ffffff"
- views: 0

Przykładowe zapytanie:
```json
{
    "token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA",
    "content": "New message content, not more than 160 characters",
}
```

Przykładowa odpowiedź:
```json
{
    "id": 0,
    "content": "New message content, not moret than 160 characters",
    "edited": "2020-10-17 21:37:14.884209",
    "views": "0",
}
```

#### Tworzenie wiadomości
**POST** /create

Dane:
- token: token uwierzytelniający
- content: treść wiadomości, nie więcej niż 160 znaków

Odpowiedź:
- id: numer identyfikacyny nowej wiadomości
- content: treść nowej wiadomości
- edited: data utworzenia w formacie "YYYY-MM-DD hh:mm:ss.ffffff"
- views: 0

Przykładowe zapytanie:
```json
{
    "token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA",
    "content": "New message content, not more than 160 characters",
}
```

Przykładowa odpowiedź:
```json
{
    "id": 0,
    "content": "New message content, not moret than 160 characters",
    "edited": "2020-10-17 21:37:14.884209",
    "views": "0",
}
```

#### Usuwanie wiadomości
**POST** /{message_id}/delete

Dane:
- token: token uwierzytelniający

Odpowiedź:
- id: numer identyfikacyny usuniętej wiadomości
- content: treść usuniętej wiadomości
- edited: data ostatniej edycji/utworzenia w formacie "YYYY-MM-DD hh:mm:ss.ffffff"
- views: liczba zaytań o odczytanie wiadomości od ostatniej edycji

Przykładowe zapytanie:
```json
{"token": "vYix496dxYeWtIUqRKrzQ1EmqdyVTolVb6FNawAIKER-hkC_SSaU65I5B8GhSNnnvk5DgIKAvpw25hSn1TczCdm-5B9WqCOJzjisvz_D_WTCaofZRC-Cuj2wMWwvZqdCfq7kujPBTMxuxeVyg-3y3epE11hBeLvbTgps8wyV0ZZFiQbN0IvmeajegBHVzgK-DSrisyIs2ZFaTF0dk21Uz8MXos3RDsEjKPUymXkbdPJH9noJZEd150-IV6u7xHeIoETcsvDy-IpD2_Tb4Ol2FEtkDPoIuKee9wVv7OSYIs-gA4gEyNtu0QVrr6nAjvPV0SI7bs-8Q7TK84AyttPakA"}
```

Przykładowa odpowiedź:
```json
{
    "id": 0,
    "content": "Old message content, not moret than 160 characters",
    "edited": "2020-10-17 21:37:14.884209",
    "views": "16",
}
```

### Błędy
Aplikacja zwraca następujące kody błędów:
- 400: Nieodpowiednie dane przesłane z zapytaniem (np. brakuje pól albo zbyt długia treść wiadomości
- 403: Nieodowiednie lub brakujące dane uwierzytelniające bądź ich brak
- 404: Nie znaleziono strony
- inne: Błąd zapytania nieprzewidziany przez dewelopera

## Dokumentacja GUI

WIP

## Dokumentacja CLI

Po stronie serwera można wywołać następujące komendy:

`flask init-db [--clear/--no-clear] [--src=PATH]`

Utwórz potrzebne tabele w bazie danych (nie tworzy tych które już istnieją)

**--clear**/**--no-clear** - Wyczyść bazę i utwórz tabele od zera. Domyślnie: **--no-clear**

**--src__=PATH** - Dodaj do bazy rekordy z plików .csv znajdujących się w folderze PATH. Przykładowy zestaw plików znajduje się w folderze test-db.
