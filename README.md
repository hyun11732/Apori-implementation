# Apriori-implementation
I implemented Apriori algorithm in Python.

Apriori Algorithm is the most popular and basic algirthm in recommendation system.
This algorithm finds out a frequent pattern in dataset.
For example, if three customers bought,

cus1 : [beer, diaper, nuts]
cus2 : [beer, m&m]
cus3 : [beer, diaper, candy]

It will return [diaper], [diaper, beer] and [beer], [beer, diaper] with minimum support of 2. 
This indicates, when customer buy a diaper, there is a high chance to buy a beer together and vice versa.

It is very simple algorithm just counting a possible set of items and count its frequency.
However, if we count all possible set of items, there are too many to compute.
For example, if there are 100 items, its number of possible set will be

![equation](https://github.com/hyun11732/Apori-implementation/blob/master/img1.JPG)

So we need to prune out our item sets by using min support. 
Pruning rule is little more complicate but not that hard.
If we have,

