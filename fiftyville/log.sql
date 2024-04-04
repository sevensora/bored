-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE day = 28 AND month = 7;

SELECT transcript FROM interviews WHERE day = 28 AND month = 7 AND transcript like "%bakery%";
