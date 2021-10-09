# Implementation of basic LCA in Python. 

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