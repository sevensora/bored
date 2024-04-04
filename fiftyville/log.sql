-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE day = 28 AND month = 7;

SELECT license_plate, activity, hour, minute FROM bakery_security_logs WHERE hour = 10 AND day = 28 AND month = 7;

SELECT transcript, name FROM interviews WHERE day = 28 AND month = 7 AND transcript like "%bakery%";

SELECT license_plate, activity, hour, minute FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour < 11 and hour > 9;

SELEct amount, account_number, transaction_type FROM atm_transactions WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street";

select people.name from atm_transactions
join bank_accounts on bank_accounts.account_number = atm_transactions.account_number
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
JOIN people ON people.id = bank_accounts.person_id Where atm_transactions.day = 28 AND atm_transactions.month = 7
AND atm_transactions.atm_location = "Leggett Street" AND bakery_security_logs.hour > 9 AND bakery_security_logs.hour < 11
ORDER BY bakery_security_logs.minute;

SELECT name from people join passengers on passengers.passport_number = people.passport_number
where passengers.flight_id = (select id from flights where day = 29 and month = 7 and origin_airport_id = (select id from airports where city = "Fiftyville") order by hour, minute limit 1);

select city from airports where id = (select destination_airport_id from flights where day = 29 and month = 7 and origin_airport_id = (SELECT id from airports where city = "Fiftyville") order by hour,minute limit 1);

select phone_number from people where name = "Bruce"

select name from people where phone_number = (select receiver from phone_calls where day = 28 and month = 7 and duration < 60 and caller = "(367) 555-5533");
