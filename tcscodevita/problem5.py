def civil_war(n,power):
    left = 0
    right = n-1
    cap_team_power = 0
    iron_team_power = 0
    turn = 0

    while left<=right:
        if power[left] > power[right]:
            selected_power = power[left]
            left += 1
        else:
            selected_power = power[right]
            right -= 1

        if turn % 2 == 0:
            cap_team_power += selected_power
        else:
            iron_team_power += selected_power

        turn += 1
    return abs(cap_team_power - iron_team_power)

n = int(input())
power = list(map(int,input().split()))

print(civil_war(n,power))