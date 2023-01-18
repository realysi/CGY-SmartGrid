def route(houses):
    x = []
    y = []
    start_x = houses[2].x
    start_y = houses[2].y
    delta_x = 7
    delta_y = -18
    end_x = start_x + delta_x
    # To the same value of the x-axis of the battery (if delta_x is positive, moves from battery to the right).
    if delta_x >= 0:
        for i in range(start_x, (start_x + delta_x + 1), 1):
            x.append(i)
            y.append(start_y)
            plt.plot(x, y, color = 'deepskyblue')
    if delta_x < 0:
        for i in range(start_x, (start_x + delta_x + 1), -1):
            x.append(i)
            y.append(start_y)
            plt.plot(x, y, color = 'deepskyblue')
    if delta_y >= 0:
        for i in range(start_y, (start_y + delta_y + 1), 1):
            x.append(end_x)
            y.append(i)
            plt.plot(x, y, color = 'deepskyblue')
    if delta_y < 0:
        for i in range(start_y, (start_y + delta_y + 1), -1):
            x.append(end_x)
            y.append(i)
            plt.plot(x, y, color = 'deepskyblue')

