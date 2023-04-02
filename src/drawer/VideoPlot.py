from src.drawer.PlotType import PlotType
import matplotlib.pyplot as plt
import numpy as np
import os

class VideoPlot(PlotType):
    """
    Plot the roads values as a video.

    Parameters
    ----------
    config : Config
        The json configuration.
    roads : array
        The roads to plot.
    """
    def draw(self, config, roads):
        print("Drawing the animation of the roads...")

        L = config["config"]["x_max"]
        dx = config["config"]["dx"]
        framesCount = int(config["config"]["t_max"] * 60)
        framesList = np.linspace(0, len(roads[0].rhoValues) - 1, framesCount).astype(int)

        # Make sure the folder for the images exists
        if not os.path.exists("./out/images/"):
            os.makedirs("./out/images/")

        # Generate an image for each time step
        print("Converting images to pixels and saving them...")
        tIterator = 0
        for tVal in framesList:
            # Create pixel array
            pS = int(L / dx)
            pixels = np.zeros([pS, pS])
            pixelsCount = np.zeros([pS, pS])

            # Add the roads
            for road in roads:
                for j in range(0, len(road.rhoValues[tVal])):
                    xPos = road.startPos[0] + (road.endPos[0] - road.startPos[0]) * j / len(road.rhoValues[tVal])
                    yPos = road.startPos[1] + (road.endPos[1] - road.startPos[1]) * j / len(road.rhoValues[tVal])

                    # Draw the pixel and a bit around it
                    for x in range(int(xPos * pS / L) - 1, int(xPos * pS / L) + 2):
                        for y in range(int(yPos * pS / L) - 1, int(yPos * pS / L) + 2):
                            if x >= 0 and x < pS and y >= 0 and y < pS:
                                pixels[x, y] += road.rhoValues[tVal][j]
                                pixelsCount[x, y] += 1

            # Average the pixels
            for x in range(0, pS):
                for y in range(0, pS):
                    if pixelsCount[x, y] > 0:
                        pixels[x, y] /= pixelsCount[x, y]

            # Save the image
            plt.imsave('out/images/' + str(tIterator) + '.png', pixels, cmap='inferno', vmin=0, vmax=0.6)

            # Print progress
            if int(tIterator / len(framesList) * 1000) % 20 == 0:
                print("Frames generating percentage = " + str(int(tIterator / len(framesList) * 1000) / 10) + "%.", end="\r")
            tIterator += 1

        # Delete the old video
        if os.path.exists('out/video.mp4'):
            os.remove('out/video.mp4')

        # Create a video from the images and scale it to 1080p, force overwrite
        print("Creating video...")
        os.system('ffmpeg -r 30 -i out/images/%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p -vf "transpose=2, scale=1920:1080" out/video.mp4')

        # Remove the images
        for file in os.listdir('out/images'):
            os.remove('out/images/' + file)
        
