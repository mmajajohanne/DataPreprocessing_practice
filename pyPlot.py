import matplotlib.pyplot as plt
import matplotlib.patches as patches

obs_boundary = [
            [0, 0, 10, 600],
            [0, 600, 900, 10],
            [10, 0, 900, 10],
            [900, 10, 10, 600]
        ]
obs_cir_own = [
    [50,500,10],
    [100,300,10],
    [240,240,10],
    [300,400,10],
    [190,50,10]

        ]
obs_cir_opp = [
            [700, 420, 10],
            [460, 200, 10],
            [550, 500, 10],
            [670, 70, 10],
            [800, 230, 10],
            [600,300,10]
        ]
fig, ax = plt.subplots()

for (ox, oy, w, h) in obs_boundary:
    print(ox, oy, w, h)        
    ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    edgecolor='black',
                    facecolor='black',
                    fill=True
                )
            )

for (ox, oy,r) in obs_cir_own:
            ax.add_patch(
                patches.Circle(
                    (ox, oy), r,
                    edgecolor='black',
                    facecolor='green',
                    fill=True
                )
            )
for (ox, oy, r) in obs_cir_opp:
            ax.add_patch(
                patches.Circle(
                    (ox, oy), r,
                    edgecolor='black',
                    facecolor='red',
                    fill=True
                )
            )
 
plt.plot(50,50, "bs", linewidth=30)
plt.plot(870, 550, "ys", linewidth=30)           
name='arena'
plt.title(name)
plt.axis("equal")
