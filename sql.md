
http://assets.red-gate.com/community/books/inside-the-sql-server-query-optimizer.pdf
# Query Optimizer

The SQL Server Query Optimizer is a cost-based optimizer. It analyzes a number of
candidate execution plans for a given query, estimates the cost of each of these plans,
and selects the plan with the lowest cost of the choices considered. Indeed, given that the
Query Optimizer cannot consider every possible plan for every query, it actually has to
find a balance between the optimization time and the quality of the selected plan.

# Join ordering  
Join ordering is one of the most complex problems in query optimization, and one that
has been the subject of extensive research since the seventies. It refers to the process of
calculating the optimal join order, that is, the order in which the necessary tables are
joined, when executing a query. As suggested in the ongoing challenges briefly discussed
earlier, join ordering is directly related to the size of the search space, as the number of
possible plans for a query grows very rapidly, depending on the number of tables joined.
the Query Optimizer needs to make two important decisions regarding joins:
• the selection of a join order
• the choice of a join algorithm

# Index

A database index is a physical access structure for a database table that functions much as the name
would suggest: it is a sorted file that informs the database of where records are physically located on the disk.  To get the idea of what an index does, consider a textbook.

## Clustered index
## Unclustered Index


# Points
Goetz Grafe
Cascades, Volcano
execution plans
cost estimations


# Questions
1) Differecne between Physical plan vs Logical plan
2) Join ordering problem and dynamic programming
3) Difference between cost based and rule based


#Books
Inside the SQL Server query optimizer
