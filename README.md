# Capacitated-vehicle-routing-problem-with-time-windows
Used GENETIC,PARTICLE SWARM and ANT BEE COLONY algorithm

I have picked Vehicle routing problem as my project which is a NP-hard problem .The VRP has many obvious applications in industry. In fact, the use of computer optimization programs can give savings of 5% to a company as transportation is usually a significant component of the cost of a product.I was inspired by this problem because of the challenges we saw that the various delivery agents have to come across with. Customers nowadays prefer to order only from those sites where they will get their delivery on time. To survive in such a competitive market, a company must have an optimized delivery system.
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

GENETIC ALGORITHM
In  computer science  and  operation research , a genetic algorithm (GA) is a metaheuristic  inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problem by relying on bio-inspired operators such as mutation crossover and selection.

In a genetic algorithm, a population of candidate solutions (called individuals, creatures, or phenotypes) to an optimization problem is evolved toward better solutions. Each candidate solution has a set of properties (its chromosomes  or genotype  which can be mutated and altered. Traditionally, solutions are represented in binary as strings of 0s and 1s, but other encodings are also possible.

A typical genetic algorithm requires:
    1. A genetic of the solution domain
    2. A fitness function  to evaluate the solution domain.
Like in our algorithm,We are generating 50 new random chromosomes. We are creating a 2d array in which first column comprises of random numbers and second column comprises of customers. Then we are sorting our 2d array on the basis of first column which leaves us with a new set of chromosome everytime.
Crossover
Among these 50 chromosomes,40 chromosomes undergo crossover. In crossover two parents are selected.
p1=[1,3,4,5,2,7,6]
p2=[2,3,4,1,5,7,6]
The starting position for crossover is index 2 and ending is 5 .It selects the cities from 2 to 5 in p1 i.e [4,5,2,7]. It then delete these cities in p2 and p2 becomes [3,1,6]. Then these deleted elements are appended at the end of p2 which generates a new child.
Child=[3,1,6,4,5,2,7]
Above is just an example with small size of dataset. For our algorithm, starting position is 2 and ending position is 18. The crossover factor here is 0.8.



Mutation
The 10 chromosomes undergo mutation process. In the mutation process a parent generates a new child.
p1=[1,3,2,4,6,5,7]
It starts with index 3 and deletes the object till index 5. The child becomes [1,3,2,7] and then the rest of the elements are appended at end.
Child=[1,3,2,7,4,6,5]
For our algorithm, starting position is 3 and ending position is 10.The mutation factor is 0.2.

Calculate cost
Then we calculate the cost of all these 100 chromosomes. The cost is calculated by distance between various customers with the help of latitude and longitudes.
Since,different customers order different amount and each vehicle has different capacity. We assign each vehicle a set of customers according to its delivering capacity. We then check in our dataset whether the customer demanded the order in morning or evening and added penalties accordingly
Fitness function
The fitness function is calculated as the inverse of cost. More the fitness function, less is the cost and better the route is.

Then we select the best 50 chromosomes among these 100 chromosomes and best 50 undergoes the same process for next generation
Each generation prints the best route calculated, its cost and its fitness function value.
We continue the process for 50 generations

Selection of fittest chromosomes
We are using a combination of tournament and stochastic solution for selecting best parents among 50 chromosomes to undergo crossover and mutation.
In K-Way tournament selection, we select K individuals from the population at random and select the best out of these to become a parent. The same process is repeated for selecting the next parent. We are using first 10-way tournament selection on our population
In a roulette wheel selection, the circular wheel is made. A fixed point is chosen on the wheel circumference and the wheel is rotated. The region of the wheel which comes in front of the fixed point is chosen as the parent. For the second parent, the same process is repeated. We will be using stochastic selection which is an extended version of roulette wheel in which all the parents are chosen in one spin of the wheel.
Implementation wise, we used the following steps 
    • Calculate S = the sum of a finesses.
    • Generate a random number between 0 and S.
    • Starting from the top of the population, keep adding the finesses to the partial sum P, till P<S.
    • The individual for which P exceeds S is the chosen individual.




Our instances description
1) 36 customers and 6 vehicles
2)45 customers and 10 vehicles
3)64 customers and 16 vehicles
