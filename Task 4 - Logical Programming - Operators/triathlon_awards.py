print(
    "##########\n\n"
    "Welcome to the Github Triathlon!\n\n"
    "##########\n\n"
    )

print("Enter your completion time (in minutes) for each event please.\n\n")

# Define completion time for each activity.
swimming = int(
    input("Enter your completion time for the \"Swimming\" event: ")
    )
cycling = int(
    input("\n\nEnter your completion time for the \"Cycling\" event: ")
    )
running = int(
    input("\n\nEnter your completion time for the \"Running\" event: ")
    )

# Calculate total completion time for triathlon.
completion_time = swimming + cycling + running

# Display completion time.
print(
    f"\n\nYou completed the Github Triathlon in {completion_time} minutes.\n\n"
    )

# Check completion time and display corresponding message.
if completion_time <= 100:
    print(
        "Congratulations! You have received the Gold Code Conqueror award."
        )
elif completion_time > 100 and completion_time <= 105:
    print(
        "Congratulations! You have received the Silver Commit Champion award."
        )
elif completion_time > 105 and completion_time <= 110:
    print(
        "Congratulations! You have received the Bronze Push Pioneer award."
        )
else:
    print(
        "Well done on completing the Github Triathlon. "
        "Unfortunately you did not qualify for any awards."
        )