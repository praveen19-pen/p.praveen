import math

# Constant
G = 9.81  # Acceleration due to gravity (m/s^2)

def calculate_reynolds_number(density, velocity, diameter, viscosity):
    """Calculates Reynolds Number (Re)"""
    return (density * velocity * diameter) / viscosity

def calculate_friction_factor(reynolds, roughness, diameter):
    """Calculates Darcy Friction Factor (f)"""
    if reynolds <= 2000:
        # Laminar flow
        return 64.0 / reynolds
    else:
        # Turbulent flow (Swamee-Jain equation)
        relative_roughness = roughness / diameter
        term = (relative_roughness / 3.7) + (5.74 / (reynolds ** 0.9))
        f = 0.25 / (math.log10(term) ** 2)
        return f

def calculate_head_loss(f, length, diameter, velocity):
    """Calculates Head Loss (hf) in meters"""
    return f * (length / diameter) * ((velocity ** 2) / (2 * G))

def calculate_pressure_drop(head_loss, density):
    """Calculates Pressure Drop (delta_p) in Pascals"""
    return density * G * head_loss

def main():
    while True:
        print("\n" + "="*35)
        print("      PIPE FLOW CALCULATOR")
        print("="*35)
        print("1. Calculate Reynolds Number")
        print("2. Calculate Darcy Friction Factor")
        print("3. Calculate Head Loss")
        print("4. Calculate Pressure Drop")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            rho = float(input("Enter fluid density (kg/m^3): "))
            v = float(input("Enter fluid velocity (m/s): "))
            d = float(input("Enter pipe inner diameter (m): "))
            mu = float(input("Enter dynamic viscosity (Pa·s): "))
            
            re = calculate_reynolds_number(rho, v, d, mu)
            print(f"\nResult: Reynolds Number (Re) = {re:.2f}")
            if re < 2000:
                print("Flow Regime: Laminar")
            elif re <= 4000:
                print("Flow Regime: Transitional")
            else:
                print("Flow Regime: Turbulent")

        elif choice == '2':
            re = float(input("Enter Reynolds number: "))
            d = float(input("Enter pipe inner diameter (m): "))
            epsilon = float(input("Enter pipe roughness (m) [e.g., 0.000045 for commercial steel]: "))
            
            f = calculate_friction_factor(re, epsilon, d)
            print(f"\nResult: Darcy Friction Factor (f) = {f:.5f}")

        elif choice == '3':
            f = float(input("Enter Darcy friction factor (f): "))
            L = float(input("Enter pipe length (m): "))
            d = float(input("Enter pipe inner diameter (m): "))
            v = float(input("Enter fluid velocity (m/s): "))
            
            hf = calculate_head_loss(f, L, d, v)
            print(f"\nResult: Head Loss (hf) = {hf:.4f} m")

        elif choice == '4':
            hf = float(input("Enter head loss (m): "))
            rho = float(input("Enter fluid density (kg/m^3): "))
            
            dp = calculate_pressure_drop(hf, rho)
            print(f"\nResult: Pressure Drop (ΔP) = {dp:.2f} Pa ({dp/1000:.3f} kPa)")

        elif choice == '5':
            print("\nExiting calculator. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
