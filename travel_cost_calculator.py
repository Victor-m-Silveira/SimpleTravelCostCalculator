from PyQt5 import QtWidgets, uic

# Create a Qt application
app = QtWidgets.QApplication([])

# Load the UI defined in the .ui file
formulario = uic.loadUi('travel_cost.ui')

# Define the function to be called when the button is clicked
def calculate_travel_cost():
    distance = float(formulario.txtDistance.text())
    consumption = float(formulario.txtConsumption.text())
    fuel_price = float(formulario.txtFuelPrice.text())
    travel_cost = (distance / consumption) * fuel_price
    formulario.lblTravelCost.setText(f'Cost: €{travel_cost:.2f}')

# Connect the UI button to the 'calculate_travel_cost' function
formulario.btnCalculate.clicked.connect(calculate_travel_cost)

# Display the form
formulario.show()

# Execute the application
app.exec()
