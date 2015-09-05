Multi-Thread Basics
===================

This examples shows the basics of VIPER multi-threading
In VIPER a thread require a function to be executed as input for the definition
the same function can be instanced by various thread giving you the possibility to write very concise and readable code.
In this example 4 threads are created as instances of the same function where different parameters are passed to the function when the thread is initialized

Note that the while True main loop typical of imperative programming is not present in this code. VIPER allows pure thread driven implementation!

tags: [First Steps, Multi-Thread]   
groups:[First Steps]