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
![equation](http://www.sciweavers.org/tex2img.php?eq=1%2Bsin%28mc%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)
