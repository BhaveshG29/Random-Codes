import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def plot_curve():
    a = float(input("Enter the value of parameter 'a': "))
    
    print(f"Plotting curve: (x² + y² - {a}²)³ = x²y³")
    
    x = np.linspace(-3*abs(a), 3*abs(a), 1000)
    y = np.linspace(-3*abs(a), 3*abs(a), 1000)
    X, Y = np.meshgrid(x, y)
    
    Z = (X**2 + Y**2 - a**2)**3 - X**2 * Y**3
    
    plt.figure(figsize=(10, 10))
    
    plt.contour(X, Y, Z, levels=[0], colors='blue', linewidths=2.5)
    
   
    
    plt.grid(True, alpha=0.3)
    plt.axis("equal")
    plt.xlabel("X Axis", fontsize=14)
    plt.ylabel("Y Axis", fontsize=14)
    plt.title("Heart", fontsize=16)
    
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='blue', linewidth=2.5, 
               label=f'$(x^2 + y^2 - {a}^2)^3 = x^2 y^3$'),
    ]
    

    plt.legend(handles=legend_elements, loc="best")
    
    
    limit = 2.5 * abs(a) if a != 0 else 2.5
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    
    plt.tight_layout()
    plt.savefig("figs/heart.png", dpi=300)
    plt.show()


plot_curve()

