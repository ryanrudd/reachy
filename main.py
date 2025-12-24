from reachy_mini import ReachyMini

with ReachyMini() as reachy:
    print(f"Reachy is connected: {reachy.state}")

    print("Wiggle antennas...")
    reachy.goto_target(antennas=[0.5, -0.5], duration=0.5)
    reachy.goto_target(antennas=[-0.5, 0.5], duration=0.5)
    reachy.goto_target(antennas=[0, 0], duration=0.5)

    print("Done wiggling antennas")