-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE day = 28 AND month = 7;

SELECT license_plate, activity, hour, minute FROM bakery_security_logs WHERE hour = 10 AND day = 28 AND month = 7;

SELECT transcript, name FROM interviews WHERE day = 28 AND month = 7 AND transcript like "%bakery%";

SELECT license_plate, activity, hour, minute FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour < 11 and hour > 9;

SELEct amount, account_number, transaction_type FROM atm_transactions WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street";

select people.name from atm_transactions
join bank_accounts on bank_accounts.account_number = atm_transactions.acount_number JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
JOIN people ON people.id = bank_accounts.person_id Where atm_transactions.day = 28 AND atm_transactions.month = 7 AND atm_transactions.atm_location = "Leggett Street" AND bakery_security_logs.hour > 9 AND bakery_security_logs.hour < 11
ORDER BY bakery_security_logs.minute;
