-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE day = 28 AND month = 7;

SELECT license_plate, activity, hour, minute FROM bakery_security_logs WHERE hour = 10 AND day = 28 AND month = 7;
