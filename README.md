# computer-monitoring-vuejs

Recently with the hot days of summer, my computer was suffering from the heat and sometimes it was shutting down unexpectedly. My high GPU usage mixed up with the ~35-45°C summer temperatures could make my computer shut down many times in a few hours. As a solution I decided to use monitoring tools to watch the temperature of my graphic card and processor to predict and then prevent any shutdown. The tools I had found online could do the job and showed the temperatures in real time but I couldn't really make my own board or use multiple charts as I wanted. So I decided to create my own monitoring tool, the target was to code a simple but efficient monitoring tool suiting my needs.

I have already used angluar 7 / nodejs / reactjs when I was at university and I wanted to challenge myself with something new to me. I have heard a lot about vuejs and I thought it was a good subject to try it out. The interface will be done using vuejs with d3js for the charts and the data will be provided by a nodejs API server.


Update : I've reseted the project and choose to use a python server to get the data and send them to a VueJS application on a socket
