# Capacitated-vehicle-routing-problem-with-time-windows

Used GENETIC,PARTICLE SWARM(PSO) and ANT COLONY OPTIMISATION(ACO) AND HYBRID OF ACO AND PSO algorithm<br />

We will be hybridizing different nature inspired algorithms and will be comparing costs and computational time for all datasets. 
Different applications involve: <br />
1)Waste collection <br />
2) School bus drop <br />
3) Delivery system <br />
*****
**Objectives**<br />
1)Minimize the transportation cost based on the distance<br /> 
2)Improved customer satisfaction by delivering goods on time <br />
*****
**Constraints**<br />
1)Different number of vehicles <br />
2)Different number of customers <br />
3)Different vehicle capacity <br />
4)Each customer is ordering different amount of goods <br />
5) Each Customer wants Delivery at different time <br />
6) Each route is a tour which starts from a depot, visits a subset of the customers, and ends at the same depot. <br />

**CONCLUSION**<br />
This study proposed five meta heuristic methods named Genetic Algorithm (GA),Particle Swarm Optimization (PSO), Ant bee colony(ABC), hybridized genetic and PACO to solve the Capacitated Vehicle Routing Problem (CVRP). We tested the proposed algorithm on a data set from solomon benchmark problems to see the performance of all the algorithms. The results indicate that the performance of proposed algorithm is competitive. <br />The genetic algorithm gives us the solution with maximum cost and high computational time. The hybridized genetic algorithm provides us with less cost than genetic algorithm but requires more computational time. Though the gaps are relatively small but still if not concerned about the computational time hybridized genetic algorithm is better than genetic algorithm. <br />The PSO algorithm provides us with the better cost than genetic and even hybridized genetic algorithm and the computational time is almost negligible in comparison to genetic algorithm.Among these three, PSO turns out to be the best in both parameters, cost and computational time. <br />
This research also compares all these algorithms on the real data set of India cities and the depot is located in Bangladesh and the performance is compared. The ant colony optimization has two variants : Ant colony system and Ellitist. <br />
The Ant colony system provides us with a better solution than Ellitist. These two variants were tested on the same values of initial pheromone, alpha, beta and rho. Also we can conclude that ACS and Ellitist, both provides us with a better solution than Genetic and PSO algorithm, with ACS being the best.In the desire for more better results, our implementation of hybridized ABC and PSO algorithm (PACO) turned out to be the best solution finally on all datasets. The PACO algorithm provides us with a route with the least cost. And moreover, to our surprise its computational time is also relatively less. Though PSO algorithm has less computational time than PACO but the cost difference is high in both the algorithms. <br />
So our research concludes that PACO algorithm provides us with the best results in both parameters: Cost and computational time. 
We would like to carry our research forward in this field and would compare the performances of more hybridized algorithms on the same dataset. 

**Dataset refrence:**<br />
http://web.cba.neu.edu/~msolomon/problems.htm




