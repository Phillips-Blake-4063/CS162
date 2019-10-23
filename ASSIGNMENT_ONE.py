#! usr/bin/python3
"""
This program will generate a hardware report.
In this program we have created a computer object that has a few
components, variables and methods. When ran, this program will
give the user the option to print out a system report of the hardware
inside the computer. User input is required for this program to run correctly.
Blake Phillips.
"""


class Computer:
    """The class called Computer."""

    def __init__(self, chip, mobo, ram, psu, ssd, gpu, pwr, disp):
        """__Init__ Constructor."""
        self.processor = chip
        self.motherboard = mobo
        self.memory = ram
        self.powersupply = psu
        self.storage = ssd
        self.graphics = gpu
        self.powerstatus = pwr
        self.display = disp

    def Power_Status(self):
        """Check the power status."""
        question1 = input("Would you like to check the POWER state?: ")
        if question1.lower() == "yes":
            print("The current POWER state is: ", self.powerstatus)
        else:
            print("I have two more questions.. : ",)

    def Display_Status(self):
        """Check the display state."""
        question2 = input("Would you like to check the DISPLAY state?: ")
        if question2.lower() == "yes":
            print("The current DISPLAY state is: ", self.display)
        else:
            print("One last question,: ")

    def Systems_Report(self):
        """Print the system report."""
        question3 = input("Would you like a Systems Report?: ")
        if question3.lower() == "yes":
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
            print("Your processor is a: {intel}".format(intel=self.processor))
            print("Your motherboard is a: {asus}".format(
                asus=self.motherboard))
            print("Your random access memory is: {corsair}".format(
                corsair=self.memory))
            print("Your power supply is a: {evga}".format(
                evga=self.powersupply))
            print("Your storage is a: {samsung}".format(samsung=self.storage))
            print("Your graphics cards are two: {rtx}".format(
                rtx=self.graphics))
            print("POWER: ON")
            print("DISPLAY:OFF")
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
            print("Goodbye!")
        else:
            print("Goodbye!")


obj1 = Computer("Intel I9900K", "Asus Prime X299",
                "Corsair Vengence Pro, 64GB", "EVGA Supernova 1600Wy",
                "Samsung 8TB NVMe SSD", "EVGA GeForce RTX2080Ti's 11GB",
                "CONNECTED", "DISCONNECTED")
obj1.Power_Status()
obj1.Display_Status()
obj1.Systems_Report()