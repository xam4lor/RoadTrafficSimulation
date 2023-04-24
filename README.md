# **RoadTrafficSimulation**
![](demo.png)

## **Introduction**
This project aims to simulate road traffic using a macroscopic approach. The traffic flow is modeled using the Lighthill-Whitham-Richards (LWR) model. The simulation is done in 2D and the road network is generated using a web interface. The results are then displayed in a video file, or in multiple graphs showing the evolution of the density over time on each road.


## **How to run this project**
### Prerequisites
- Clone this repository and enter the python environment. The list of dependencies is in the `requirements.txt` file. You will also **need to install [ffmpeg](https://ffmpeg.org/)** to generate the video file.
- To change the parameters used by the numerical solver, edit the `config.json` file in the `res/` folder.

### Generate the road network
- Open the HTML file `index.html` in the `app/` folder in a browser. This will open an interface to generate the road network and the traffic flow. The instructions are written on the interface webpage.
- Once the network is generated, click on the `Export` button to get a file called `roads.json`. This file contains the road network data used by the simulation. Copy this file in the `res/` folder by replacing the existing file (*the name of the file is important and should be `roads.json`*).

### Run the simulation
- Finally, run the `main.py` file. This will run the simulation and generate a video file in the `out/` folder. This video file contains the simulation of the traffic flow on the road network.
- You can also choose to visualize the evolution of density over time on each road, you can also change the value of `outputType` from "*video*" to "*density*" in the `res/config.json` file (*advise: do not use this option if you have a lot of roads, otherwhise it might cause lag*).


## **References**
Main sources used for this project:
 - [Lighthill-Whitham-Richards traffic flow model (lectures)](https://sboyles.github.io/teaching/ce392d/5-lwrmodel.pdf)
 - [Traffic flow: the Lighthill-Whitham-Richards model (python implementation)](http://www.clawpack.org/riemann_book/html/Traffic_flow.html)
 - [2D-LWR in large-scale network with space dependent fundamental diagram](https://hal.science/hal-01866959/document)
