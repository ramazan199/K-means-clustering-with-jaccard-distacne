import matplotlib.pyplot as plt

def plotting(central_groups_dct_best, videos_with_their_tags_dct):
    cmap = plt.get_cmap('jet_r')
    counter = 0
    # plt.figure()
    
    for ct in [*central_groups_dct_best]:
        color = cmap(float(counter)/len([*central_groups_dct_best]))
        counter = counter + 1
        x = list(central_groups_dct_best[ct])

        for vd in x:
            y = list(videos_with_their_tags_dct[vd])
            plt.plot( y, '-o', markersize=2,c = color)

        plt.axis('equal')
    plt.pause(1000)