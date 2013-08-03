import math

def calculateCap():
	
	energyDensityDesired = input("Enter energy density (Wh/kg): ")
	voltage = input("Desired Voltage (V): ")
	
	capacitance = ((8*energyDensityDesired)/(voltage*voltage))
	print "Specific Capacitance: " + str(capacitance) + " F/g"
	
	return capacitance, energyDensityDesired, voltage
	
def calculateEnergyDensity():
	

	capacitance = input("Enter specific capacitance (F/g): ")
	voltage = input("Enter voltage (V): ")
	energyDensity = ((capacitance)*(voltage*voltage)/8)
	print "Energy Density: " + str(energyDensity) + " Wh/kg"
	
	return energyDensity, capacitance, voltage
	
	

def introScript():
	
	print "Hey there, welcome to the Energy Density Program."
	print 
	print "Press '1' for Calculating Theoretical Energy Density"
	print 
	print "Press '2' for Calculating Theoretical Specific Capacitance"
	print
	print "Press '3' for Calculating Nominal Voltage"
	choice = input("Choice '1' or '2' or '3' ? ")
	print
	
	
	return choice

def calculateNominalVoltage():
	
	energyDensity = input("Enter your desired energy density: ")
	capacitance = input("Enter your capacitance: ")
	
	desiredVoltage = math.sqrt(((energyDensity*8)/capacitance))
	
	print "Minimal Voltage: " + str(desiredVoltage)
	return desiredVoltage

def main():

	choice = introScript()
	
	if choice == 1:
		calculateEnergyDensity()
	
	elif choice == 2:
		calculateCap()
		
	elif choice == 3:
		calculateNominalVoltage()
		
	else:	
		print "You broke me! Just Kidding, please enter a valid option." #Place while loop for this option.


main()
	