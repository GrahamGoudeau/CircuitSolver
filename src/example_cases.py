from Component_Types import Two_Prong_Component_Types, Single_Prong_Component_Types
from Junction import Junction
import Component_Single_Prong
import Component_Two_Prongs
from Circuit import Circuit

###############################################################################
def main():
    circuit1 = Circuit()
    circuit2 = Circuit()
    circuit3 = Circuit()
    circuit4 = Circuit()
    circuit5 = Circuit()
    circuit6 = Circuit()
    circuit7 = Circuit()
    circuit8 = Circuit()
    circuit9 = Circuit()
    circuit10 = Circuit()
    circuit11 = Circuit()
    circuit12 = Circuit()
    circuit13 = Circuit()
    circuit15 = Circuit()
    circuit16 = Circuit()
    circuit17 = Circuit()
    circuit18 = Circuit()
    circuit19 = Circuit()
    circuit20 = Circuit()
    circuit21 = Circuit()

    #circuit 1
    print "Circuit 1:"
    j1, j2 = circuit1.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit1.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j2)
    circuit1.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit1.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    circuit1.debug_map()
    print "\n\n"

    #circuit 2
    print "Circuit 2:"
    j1, j2 = circuit2.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    j3, j4 = circuit2.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    circuit2.connect_junctions(j2, j3)
    circuit2.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit2.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit2.debug_map()
    print "\n\n"

    #circuit 3
    print "Circuit 3:"
    j1, j2 = circuit3.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    j3, j4 = circuit3.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    circuit3.connect_junctions(j2, j3)
    circuit3.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1, j1, j4)
    circuit3.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit3.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit3.debug_map()
    print "\n\n"
    
    #circuit 4
    print "Circuit 4:"
    j1, j2 = circuit4.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    circuit4.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j1, j2)
    j3, j4 = circuit4.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit4.connect_junctions(j4, j1)
    circuit4.add_single_prong_component(Single_Prong_Component_Types.OPEN, j3)
    circuit4.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    circuit4.debug_map()
    print "\n\n"

    #circuit 5
    print "Circuit 5:"
    j1, j2 = circuit5.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit5.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j2)
    circuit5.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j1, j2)
    circuit5.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit5.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    circuit5.debug_map()
    print "\n\n"

    #circuit 6
    j1, j2 = circuit6.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    j3, j4 = circuit6.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    j5, j6 = circuit6.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    circuit6.connect_junctions(j2, j3)
    circuit6.connect_junctions(j4, j5)
    circuit6.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit6.add_single_prong_component(Single_Prong_Component_Types.OPEN, j6)
    circuit6.debug_map()
    print "\n\n"

    #circuit 7
    print "Circuit 7:"
    j1, j2 = circuit7.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    j3, j4 = circuit7.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    j5, j6 = circuit7.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    j7, j8 = circuit7.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4)
    circuit7.connect_junctions(j2, j3)
    circuit7.connect_junctions(j4, j5)
    circuit7.connect_junctions(j6, j7)
    circuit7.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit7.add_single_prong_component(Single_Prong_Component_Types.OPEN, j8)
    circuit7.debug_map()
    print "\n\n"

    #circuit 8
    print "Circuit 8:"
    j1, j2 = circuit8.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    j3, j4 = circuit8.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    circuit8.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j3, j4)
    circuit8.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j3, j4)
    circuit8.connect_junctions(j2, j3)
    circuit8.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit8.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit8.debug_map()
    print "\n\n"

    #circuit 9
    print "Circuit 9:"
    j1, j2 = circuit9.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    j3, j4 = circuit9.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    circuit9.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j3, j4)
    j5, j6 = circuit9.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4)
    circuit9.connect_junctions(j2, j3)
    circuit9.connect_junctions(j4, j5)
    circuit9.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit9.add_single_prong_component(Single_Prong_Component_Types.OPEN, j6)
    circuit9.debug_map()
    print "\n\n"

    #circuit 10
    print "Circuit 10:"
    j1, j2 = circuit10.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit10.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j2)
    circuit10.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j1, j2)
    circuit10.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j1, j2)
    circuit10.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit10.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    circuit10.debug_map()
    print "\n\n"

    #circuit 11
    print "Circuit 11:"
    j1, j2 = circuit11.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    circuit11.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j1, j2)
    j3, j4 = circuit11.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    circuit11.connect_junctions(j4, j1)
    circuit11.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1, j3, j2)
    circuit11.add_single_prong_component(Single_Prong_Component_Types.OPEN, j3)
    circuit11.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    circuit11.debug_map()
    print "\n\n"

    #circuit 12
    print "Circuit 12:"
    j1, j2 = circuit12.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit12.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j2)
    j3, j4 = circuit12.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    circuit12.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j3, j4)
    circuit12.connect_junctions(j2, j3)
    circuit12.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit12.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit12.debug_map()
    print "\n\n"

    #circuit 13
    print "Circuit 13:"
    j1, j2 = circuit13.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    j3, j4 = circuit13.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2)
    j5, j6 = circuit13.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    j7, j8 = circuit13.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4)
    circuit13.connect_junctions(j2, j3)
    circuit13.connect_junctions(j6, j7)
    circuit13.connect_junctions(j1, j5)
    circuit13.connect_junctions(j4, j8)
    circuit13.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit13.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit13.debug_map()
    print "\n\n"

    #circuit 14 is a duplicate so dont need to test
    print "Circuit 14 is a duplicate so dont need to test"
    print "\n\n"

    #circuit 15
    print "Circuit 15:"
    j1, j2 = circuit15.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3)
    j3, j4 = circuit15.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4)
    circuit15.connect_junctions(j2, j3)
    circuit15.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j4)
    j5, j6 = circuit15.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit15.connect_junctions(j6, j1)
    circuit15.add_single_prong_component(Single_Prong_Component_Types.OPEN, j5)
    circuit15.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit15.debug_map()
    print "\n\n"

    #circuit 16
    print "Circuit 16:"
    j1, j2 = circuit16.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit16.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit16.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    _, j3 = circuit16.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j2)
    circuit16.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j1, j3)
    _, j4 = circuit16.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j1)
    circuit16.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5, j4, j3)
    circuit16.debug_map()
    print "\n\n"

    #circuit 17
    print "Circuit 17:"
    j1, j2 = circuit17.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit17.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit17.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    _, j3 = circuit17.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1)
    circuit17.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j3, j2)
    circuit17.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j3, j2)
    circuit17.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5, j3, j2)
    circuit17.debug_map()
    print "\n\n"

    #circuit 18
    print "Circuit 18:"
    j1, j2 = circuit18.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit18.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    _, j3 = circuit18.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j2)
    _, j4 = circuit18.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j3)
    circuit18.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j3, j4)
    circuit18.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5, j2, j4)
    circuit18.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit18.debug_map()
    print "\n\n"

    #circuit 19
    print "Circuit 19:"
    j1, j2 = circuit19.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit19.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit19.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j2)
    _, j3 = circuit19.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j2)
    _, j4 = circuit19.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j3)
    circuit19.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5, j3, j4)
    circuit19.add_single_prong_component(Single_Prong_Component_Types.OPEN, j4)
    circuit19.debug_map()
    print "\n\n"

    #circuit 20
    print "Circuit 20:"
    j1, j2 = circuit20.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit20.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    _, j3 = circuit20.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j2)
    _, j4 = circuit20.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j3)
    _, j5 = circuit20.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j4)
    _, j6 = circuit20.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5, j5)
    circuit20.add_single_prong_component(Single_Prong_Component_Types.OPEN, j6)
    circuit20.debug_map()
    print "\n\n"

    #circuit 21
    print "Circuit 21:"
    j1, j2 = circuit21.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 1)
    circuit21.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 2, j1, j2)
    circuit21.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 3, j1, j2)
    circuit21.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 4, j1, j2)
    circuit21.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5, j1, j2)
    circuit21.add_single_prong_component(Single_Prong_Component_Types.OPEN, j1)
    circuit21.add_single_prong_component(Single_Prong_Component_Types.OPEN, j2)
    circuit21.debug_map()
    print "\n\n"
    
###############################################################################
if __name__ == "__main__":
    main()
