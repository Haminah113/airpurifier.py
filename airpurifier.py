import time

def air_purifier_cycle():
    # Time duration for each stage (in seconds)
    check_air_quality_duration = 5   # Time to check air quality
    purify_air_duration = 10         # Time for air purification
    idle_duration = 8                # Time for idle mode

    while True:
        # Checking air quality
        print("Checking air quality: START")
        time.sleep(check_air_quality_duration)
        print("Air quality checked: DONE")
        time.sleep(1)  # Short transition before purification

        # Purifying air
        print("Purifying air: START")
        time.sleep(purify_air_duration)
        print("Purifying air: DONE")
        time.sleep(1)  # Short transition before idle mode

        # Idle mode
        print("Air purifier in idle mode: START")
        time.sleep(idle_duration)
        print("Idle mode: DONE")
        time.sleep(1)  # Short break before restarting the cycle

# Run the air purifier cycle
air_purifier_cycle()