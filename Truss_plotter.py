import matplotlib.pyplot as plt
import numpy as np

steelDat = {
    'Trial 1' : {
        'Loads' : [76.36,155.06,235.47,317.52,394.65],
        'F5measured' : [-92.20,-172.59,-249.51,-323.24,-389.87],
        'F6measured' : [55.15,95.98,137.28,178.37,217.19],
        'F7measured' : [73.80,133.20,184.77,239.23,295.46],
        'Disp' : [0.028,0.038,0.048,0.058,0.067],
    },
    'Trial 2' : {
        'Loads' : [79.58,157.72,239.29,319.40,397.56],
        'F5measured' : [-96.59,-174.92,-252.70,-325.57,-399.77],
        'F6measured' : [57.70,97.71,139.46,180.01,219.20],
        'F7measured' : [74.95,132.51,187.81,243.61,294.46],
        'Disp' : [0.031,0.041,0.051,0.060,0.069],
    },
    'Trial 3' : {
        'Loads' : [80.62,158.86,242.83,320.46,397.23],
        'F5measured' : [-98.84,-175.97,-255.21,-324.40,-339.80],
        'F6measured' : [58.30,98.09,140.70,179.41,219.12],
        'F7measured' : [75.76,132.29,187.43,240.77,292.43],
        'Disp' : [0.030,0.040,0.050,0.059,0.069],
    },
    'Trial 4' : {
        'Loads' : [79.12,157.67,239.44,319.19,398.12],
        'F5measured' : [-96.95,-174.47,-253.07,-325.54,-399.80],
        'F6measured' : [57.62,97.37,139.53,180.01,219.71],
        'F7measured' : [81.62,130.30,186.43,243.04,294.23],
        'Disp' : [0.032,0.040,0.051,0.060,0.069],
    },
    'Trial 5' : {
        'Loads' : [79.64,159.07,241.72,321.68,397.95],
        'F5measured' : [-96.21,-175.31,-254.06,-327.39,-399.82],
        'F6measured' : [57.59,98.00,140.29,181.35,219.42],
        'F7measured' : [82.22,132.92,189.30,243.87,292.18],
        'Disp' : [0.033,0.042,0.052,0.061,0.070],
    }
}

alumData = {
    'Trial 1': {
        'Loads': [43.73, 77.38, 118.37, 158.93, 201.19],
        'F5measured': [-35.96, -70.57, -112.59, -153.40, -195.39],
        'F6measured': [19.45, 34.01, 51.89, 71.09, 90.21],
        'F7measured': [30.25, 54.11, 83.62, 110.61, 139.78],
        'Disp': [0.0085, 0.0135, 0.024, 0.033, 0.04],
    },
    'Trial 2': {
        'Loads': [43.53, 82.21, 118.50, 159.50, 199.32],
        'F5measured': [-35.36, -77.25, -112.38, -154.11, -193.32],
        'F6measured': [18.64, 38.08, 54.42, 71.31, 88.60],
        'F7measured': [31.36, 58.82, 83.50, 111.70, 138.81],
        'Disp': [0.0085, 0.0155, 0.0235, 0.033, 0.04],
    },
    'Trial 3': {
        'Loads': [43.12, 78.45, 119.24, 158.53, 199.02],
        'F5measured': [-35.94, -71.76, -112.15, -151.93, -193.72],
        'F6measured': [18.77, 35.73, 53.11, 70.42, 89.42],
        'F7measured': [29.12, 55.40, 84.61, 108.81, 136.73],
        'Disp': [0.009, 0.0145, 0.0235, 0.032, 0.04],
    },
    'Trial 4': {
        'Loads': [41.08, 80.20, 120.02, 158.54, 199.41],
        'F5measured': [-34.72, -72.31, -112.68, -152.72, -193.62],
        'F6measured': [16.95, 35.31, 52.72, 71.39, 89.43],
        'F7measured': [29.30, 55.41, 82.19, 109.98, 137.46],
        'Disp': [0.006, 0.015, 0.0235, 0.032, 0.04],
    },
    'Trial 5': {
        'Loads': [39.18, 79.34, 120.01, 159.86, 199.19],
        'F5measured': [-31.75, -72.46, -113.34, -154.16, -192.74],
        'F6measured': [17.31, 35.47, 53.75, 70.31, 89.98],
        'F7measured': [29.24, 56.38, 83.05, 110.17, 138.64],
        'Disp': [0.006, 0.0155, 0.023, 0.03, 0.0405],
    }
}

def compute_bar_slope(trussData, bar_label):
    """
    Computes and prints the slope of a best-fit line (linear regression)
    between applied loads and measured bar loads across all trials
    for the specified bar.

    Parameters
    ----------
    trussData : dict
        One of the truss dictionaries (e.g., steelDat or alumData).
    bar_label : str
        Bar name, e.g. 'F5', 'F6', 'F7'.

    Returns
    -------
    float
        The computed slope (best-fit coefficient).
    """
    all_loads = []
    all_forces = []

    # Collect all trial data for this bar
    for trial_data in trussData.values():
        all_loads.extend(trial_data['Loads'])
        all_forces.extend(trial_data[f'{bar_label}measured'])

    # Convert to NumPy arrays
    loads = np.array(all_loads)
    forces = np.array(all_forces)

    # Linear regression (1st-degree polyfit)
    slope, intercept = np.polyfit(loads, forces, 1)

    print(f"{bar_label} slope for truss = {slope:.4f}, intercept = {intercept:.4f}")
    return slope, intercept


def plot_truss_data(steelDat, alumData, theoretical_funcs):
    """
    Plots measured and theoretical load-vs-applied-load curves for bars 5, 6, and 7.

    Parameters
    ----------
    steelDat : dict
        Steel truss data structured like the example steelDat dictionary.
    alumData : dict
        Aluminum truss data structured like the example alumData dictionary.
    theoretical_funcs : dict
        Dictionary mapping sensor name ('F5', 'F6', 'F7') to a function f(load)
        that returns the theoretical bar load for a given applied load.
    """

    bar_labels = ['F5', 'F6', 'F7']
    colors = {'steel': 'tab:blue', 'alum': 'tab:orange'}

    for bar_label in bar_labels:
        plt.figure(figsize=(7, 5))
        # Compute and print slopes for both trusses
        compute_bar_slope(steelDat, bar_label)
        compute_bar_slope(alumData, bar_label)
        print("--------------------------------------")

        # --- Add theoretical curve ---
        all_loads = np.linspace(0, max(
            max([max(t['Loads']) for t in steelDat.values()]),
            max([max(t['Loads']) for t in alumData.values()])
        ), 100)
        theoretical_loads = theoretical_funcs[bar_label](all_loads)
        plt.plot(all_loads, theoretical_loads, 'k-', linewidth=2.0, label='Theoretical')

        # --- Plot measured data for steel ---
        for i, (trial_name, trial_data) in enumerate(steelDat.items()):
            plt.plot(
                trial_data['Loads'], trial_data[f'{bar_label}measured'],
                color=colors['steel'], marker='o',
                label=f'Steel' if i == 0 else None,
                alpha=0.8
            )

        # --- Plot measured data for aluminum ---
        for i, (trial_name, trial_data) in enumerate(alumData.items()):
            plt.plot(
                trial_data['Loads'], trial_data[f'{bar_label}measured'],
                color=colors['alum'], marker='o',
                label=f'Aluminum' if i == 0 else None,
                alpha=0.8
            )

        # --- Format plot ---
        plt.title(f'Measured vs Theoretical Load on Bar {bar_label[-1]}')
        plt.xlabel('Applied Load (lbs)')
        plt.ylabel(f'Measured Load on Bar {bar_label[-1]} (lbs)')
        plt.legend(title='Truss Material')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(bar_label + '.png')
    plt.show()


# === Example usage ===
# Define your theoretical functions for each bar.
# (Replace these linear relations with your actual analytical models.)
def F5_theoretical(load):
    return -load

def F6_theoretical(load):
    return load / 2

def F7_theoretical(load):
    return load / np.sqrt(2)

theoretical_funcs = {
    'F5': F5_theoretical,
    'F6': F6_theoretical,
    'F7': F7_theoretical
}

# Then call:
plot_truss_data(steelDat, alumData, theoretical_funcs)

def plot_load_displacement(steelDat, alumData):
    """
    Creates a combined load–displacement figure with 10 total curves:
    5 trials for the steel truss and 5 trials for the aluminum truss.

    Parameters
    ----------
    steelDat : dict
        Dictionary containing steel truss trial data.
    alumData : dict
        Dictionary containing aluminum truss trial data.
    """

    plt.figure(figsize=(8, 6))

    colors = {'steel': 'tab:blue', 'alum': 'tab:orange'}
    linestyles = {'steel': '-', 'alum': '--'}
    markers = ['o', 's', 'd', '^', 'v']

    # --- Plot steel trials ---
    for i, (trial_name, trial_data) in enumerate(steelDat.items()):
        plt.plot(
            trial_data['Disp'], trial_data['Loads'],
            color=colors['steel'], linestyle=linestyles['steel'],
            marker=markers[i % len(markers)],
            label=f'Steel' if i == 0 else None,
            alpha=0.8
        )

    # --- Plot aluminum trials ---
    for i, (trial_name, trial_data) in enumerate(alumData.items()):
        plt.plot(
            trial_data['Disp'], trial_data['Loads'],
            color=colors['alum'], linestyle=linestyles['alum'],
            marker=markers[i % len(markers)],
            label=f'Aluminum' if i == 0 else None,
            alpha=0.8
        )

    # --- Formatting ---
    plt.title('Load vs. Displacement for Steel and Aluminum Trusses')
    plt.xlabel('Displacement (in)')
    plt.ylabel('Applied Load (lbs)')
    plt.grid(True)
    plt.legend(title='Truss Material')
    plt.tight_layout()
    plt.show()
    plt.savefig('displacement.png')

plot_load_displacement(steelDat, alumData)
