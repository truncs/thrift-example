Requirements
=============
  
 * thrift
 * python thrift lib


To Compile
==========
g++ -DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H -Wall -I/usr/local/include/thrift
*.cpp -L/usr/local/lib -lthrift -o server


To Run
========
./server



