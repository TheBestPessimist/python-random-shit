# package thebestpessimist.workshop.pyground
# check this things, they look interesting




#######################################################################
#                                                                      ask for their presentations!!!!!                                                                 #
#######################################################################




import functools
=> functools.partial
=> functools.wraps #(decorators)



=> operator.<a lot of things go here>
    => operator.add->x + y
    
# iterators and generators
=> called with next(my_iterator/generator)
=> iterators: it is a class with a next() and a __iter__ methods (and of course, __init__), amongst other things
=> generators: are functions (has something called "yeld" <= that is what makes it a generator, because it stops at the yeld, untill "next(my_iterator/generator)" is called again
    
# don't forget about the dir() function!

# to make a faster generator: use :()
(x for x in range(5))