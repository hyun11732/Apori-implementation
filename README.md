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

It is very simple algorithm just counting a possible set of items and count its frequency through bottom-up process.
However, if we count all possible set of items, there are too many to compute.
For example, if there are 100 items, its number of possible set will be

![equation](https://github.com/hyun11732/Apori-implementation/blob/master/images/img1.JPG)

So we need to prune out our item sets by using min support.
Pruning rule is little more complicate but not that hard.
When we make k+1 itemset based on k itemset. If a k+1 itemset's k subset is not in k itemsets, it should be pruned out.
For example,
![equation](https://github.com/hyun11732/Apori-implementation/blob/master/images/img2.JPG)

"acde" is pruned because its 3-subset "ade" and "cde" are not in 3-itemsets.

By pruning process, we can remove unused possibility and increase performance.
