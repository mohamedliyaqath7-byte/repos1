# Project Plan

## Project: Plant Watering Reminder Robot

**Idea in two sentences:** My robot has a soil moisture sensor. When the soil is too dry, it reminds me to water the plant, and when the soil is wet enough, it stays quiet.

## How it works
1. Sensor: reads the soil moisture (simulated with random numbers for now).
2. Decision: if moisture is below 30 percent, the soil is too dry.
3. Action: print a reminder to water the plant.

## Plan
- Stage 1: basic simulator (done)
- Stage 2: add a "keep an eye on it" message for medium moisture
- Stage 3: count how many reminders were sent
- Stage 4: replace the random sensor with real readings from hardware