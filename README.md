# Capacitated-vehicle-routing-problem-with-time-windows
Used genetic,particle swarm and ant bee colony algorithm

We have picked Vehicle routing problem as our project which is a NP-hard problem .The VRP has many obvious applications in industry. In fact, the use of computer optimization programs can give savings of 5% to a company as transportation is usually a significant component of the cost of a product.
We were inspired by this problem because of the challenges we saw that the various delivery agents have to come across with. Customers nowadays prefer to order only from those sites where they will get their delivery on time. To survive in such a competitive market, a company must have an optimized delivery system.
To save their time and for good customer satisfaction, they need to identify an optimized route for delivery. Some algorithms consider either only cost or deliver goods according to the dates on which customer ordered.
We will be using nature inspired algorithms to find an optimized route which, in addition to cost between various cities takes into account the time delay cost also, if the delivery agent is tardy in delivering the product. 

PROBLEM STATEMENT
Our challenge is to find "What is the optimal set of routes for a delivery agent to traverse in order to deliver to a given set of customers?”.The VRP concerns the service of a delivery company.
We are provided with latitude and longitudes of different customer’s location. We have to conclude which algorithm works best for our problem.

The objectives which we have to achieve for our problem are:
1)Minimize the transportation cost based on the distance
2)Improved customer satisfaction by delivering goods on time

The constraints for our problem statement are:
1)Different number of vehicles
2)Different number of customers
3)Different vehicle capacity
4)Each customer is ordering different amount of goods


While researching about our problem statement, we came across different variants of vehicle routing problem which are mentioned as belows:
1)Capacitated vehicle routing problem (CVRP)
2)Multi-depot vehicle routing problem (MDVRP)
3)Period vehicle routing problem (PVRP)
4)Split delivery vehicle routing problem (SDVRP)
5)Stochastic vehicle routing problem (SVRP)
6)Vehicle routing problem with pick-up and delivery 
7)Vehicle routing problem with time windows (VRPTW)
8)Time dependent vehicle routing problem with time windows (TDVRPTW)
In our project, we have combined all these aspects mentioned above in a single problem statement using different nature inspired algorithms-genetic algorithm,particle swarm and ant bee colony.
At the end, we are comparing the algorithms by applying different instances on them and plotting a bar graph cost vs algorithm for each instance.
