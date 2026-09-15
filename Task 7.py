def goal_stack_planning():
    print("Goal: Get Banana")

    print("\nTrying first plan...")
    print("Move Box to Banana")
    print("Failure: Box cannot be moved to Banana")

    print("\nBacktracking...")
    print("Trying alternative plan...")

    plan = [
        "Move Box to Table",
        "Climb Table",
        "Pick Banana"
    ]

    print("\nPlan:")
    for action in plan:
        print(action)

    print("\nGoal Achieved!")


goal_stack_planning()
