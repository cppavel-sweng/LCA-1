# Implementation of basic LCA in Python. 

This repo was recently updated to contain DAG implementation. 

Please note that the definition of LCA in DAGs 
is different from LCAs in binary trees: "Lowest common ancestors of x and y are the nodes of out-degree zero in the subgraph of G induced by the set of common ancestors of x and y."

Whereas for binary trees, we have: "The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself)."

Basically, that means that we do not include nodes themselves into the parents subgraph and hence LCA(node, node) 
is not equal to node. It will actually be equal to the set of all direct parents of node.

However, to account for the case LCA(root, node), I consider the root to be a parent of itself.

LCA(root1, root2) will be empty, since different roots do not have any common parents, or any parents at all.

See the [other repo](https://github.com/cppavel-sweng/LCA-TypeScript) for the TypeScript version.


Uses parameterized testing and coverage collection. 


* Larger objects are logged into a separate file, for example arrays, 
which take part in the assert statements.


* This log file can be viewed after the tests are run, since it is opened with the
"more" command.


* This project assumes you are running on windows. If you have docker installed 
all you need to do is open cmd and run run_tests.cmd to execute tests.


* On mac/linux, you may have to copy the commands from run_tests.cmd, tweak them a little 
bit and run them in terminal.


* The current version coverage is 100% (feel free to verify it yourself by running tests).