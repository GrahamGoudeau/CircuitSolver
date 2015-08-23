if __name__ == "__main__":
    circuit = Circuit()
    # returns the ids of the two junctions it creates
    j1, j2 = circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 5)
    circuit.add_two_prong_component(Two_Prong_Component_Types.CAPACITOR, 10, j1, j2)
    _, y = circuit.add_two_prong_component(Two_Prong_Component_Types.RESISTOR, 100, j1)
    circuit.add_single_prong_component(Single_Prong_Component_Types.OPEN, y)
    circuit.debug_map()
