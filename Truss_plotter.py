"""
Project: Truss Data Analysis
Author: Asael Acosta
Acknowledgment: Portions of this code were developed with assistance from ChatGPT (GPT-5, OpenAI, 2025).
"""
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
        'F5measured' : [-98.84,-175.97,-255.21,-324.40,-399.80],
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


def compute_average_percent_error(trussData, theoretical_funcs):
    """
    Computes the average percent error between the measured and
    theoretical bar loads across all trials, for each bar (F5, F6, F7).

    Percent error is defined as:
        |measured - theoretical| / |theoretical| * 100

    Parameters
    ----------
    trussData : dict
        Truss data dictionary (e.g., steelDat or alumData)
    theoretical_funcs : dict
        Dictionary mapping bar labels ('F5', 'F6', 'F7') to their theoretical functions.

    Returns
    -------
    dict
        Dictionary of average percent error values for each bar.
    """
    bar_labels = ['F5', 'F6', 'F7']
    percent_errors = {}

    for bar_label in bar_labels:
        error_list = []
        for trial_data in trussData.values():
            measured = np.array(trial_data[f'{bar_label}measured'])
            loads = np.array(trial_data['Loads'])
            theoretical = theoretical_funcs[bar_label](loads)

            # Avoid division by zero
            valid_mask = theoretical != 0
            measured = measured[valid_mask]
            theoretical = theoretical[valid_mask]

            percent_error = np.abs((measured - theoretical) / theoretical) * 100
            mean_error = np.mean(percent_error)
            error_list.append(mean_error)

        avg_percent_error = np.mean(error_list)
        percent_errors[bar_label] = avg_percent_error

        print(f"Average percent error for {bar_label}: {avg_percent_error:.2f}%")

    return percent_errors


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
            trial_data['Loads'], trial_data['Disp'],
            color=colors['steel'], linestyle=linestyles['steel'],
            marker=markers[i % len(markers)],
            label=f'Steel' if i == 0 else None,
            alpha=0.8
        )

    # --- Plot aluminum trials ---
    for i, (trial_name, trial_data) in enumerate(alumData.items()):
        plt.plot(
            trial_data['Loads'], trial_data['Disp'],
            color=colors['alum'], linestyle=linestyles['alum'],
            marker=markers[i % len(markers)],
            label=f'Aluminum' if i == 0 else None,
            alpha=0.8
        )

    # --- Formatting ---
    plt.title('Load vs. Displacement for Steel and Aluminum Trusses')
    plt.xlabel('Applied Load (lbs)')
    plt.ylabel('Displacement (in)')
    plt.grid(True)
    plt.legend(title='Truss Material')
    plt.tight_layout()
    plt.savefig('OVER_HERE.png')
    plt.show()


def plot_residuals_from_theoretical_funcs(steelDat, alumDat, theoretical_funcs, save_fig=False):
    """
    Compute and plot residuals (measured - theoretical) for Aluminum and Steel truss data
    using a dictionary of theoretical functions.

    Parameters
    ----------
    steelDat : dict
        Nested dict where each key is a trial, containing 'Loads' and measured forces (F5, F6, F7).
    alumDat : dict
        Same structure as steelDat for the aluminum truss.
    theoretical_funcs : dict
        Dictionary mapping bar names ('F5', 'F6', 'F7') to functions f(load) → expected load.
    save_fig : bool, optional
        If True, saves the residual plots as PNGs.

    Returns
    -------
    residuals : dict
        Nested dictionary of residuals for each material, trial, and bar.
    """

    materials = {"Aluminum": alumDat, "Steel": steelDat}
    residuals = {"Aluminum": {}, "Steel": {}}

    for material, dataset in materials.items():
        for trial, data in dataset.items():
            residuals[material][trial] = {}
            loads = np.array(data["Loads"])

            for bar in ["F5", "F6", "F7"]:
                measured_key = f"{bar}measured"
                if measured_key not in data:
                    continue

                measured = np.array(data[measured_key])
                theoretical = np.array([theoretical_funcs[bar](L) for L in loads])
                res = measured - theoretical
                residuals[material][trial][bar] = res

                # Plot residuals
                plt.figure(figsize=(6, 4))
                plt.axhline(0, color='black', linestyle='--', linewidth=1)
                plt.plot(loads, res, 'o-', label=f"{trial} ({bar}) Residuals")
                plt.xlabel("Applied Load (N)")
                plt.ylabel("Residual (Measured - Theoretical) [N]")
                plt.title(f"{material} — {bar} Residuals ({trial})")
                plt.legend()
                plt.grid(True, linestyle=':', alpha=0.7)
                plt.tight_layout()

                if save_fig:
                    plt.savefig(f"{material}_{bar}_{trial}_residuals.png", dpi=300)

                plt.show()

    return residuals


def plot_bar_residuals(steelDat, alumDat, theoretical_funcs, save_fig=False):
    """
    Compute and plot residuals (measured - theoretical) for all bars.
    Each bar has one figure showing residuals for all trials of both materials.

    Parameters
    ----------
    steelDat : dict
        Steel truss data (nested dict with trial entries containing 'Loads' and measured bar data).
    alumDat : dict
        Aluminum truss data with the same structure as steelDat.
    theoretical_funcs : dict
        Maps bar labels ('F5', 'F6', 'F7') to functions that return expected loads for given applied loads.
    save_fig : bool, optional
        If True, saves the plots as PNG files.

    Returns
    -------
    residuals : dict
        Nested dictionary of residuals by material, trial, and bar.
    """

    materials = {"Steel": steelDat, "Aluminum": alumDat}
    residuals = {"Steel": {}, "Aluminum": {}}

    bar_labels = ["F5", "F6", "F7"]
    colors = {
        "Steel": "tab:blue",
        "Aluminum": "tab:orange"
    }

    for bar in bar_labels:
        plt.figure(figsize=(7, 5))
        plt.axhline(0, color="black", linestyle="--", linewidth=1)

        for material, dataset in materials.items():
            for trial_name, trial_data in dataset.items():
                loads = np.array(trial_data["Loads"])
                measured = np.array(trial_data[f"{bar}measured"])
                theoretical = np.array([theoretical_funcs[bar](L) for L in loads])
                res = measured - theoretical

                # Store residuals
                residuals[material].setdefault(trial_name, {})[bar] = res

                # Plot residual line for this trial
                plt.plot(
                    loads,
                    res,
                    marker="o",
                    linestyle="-",
                    color=colors[material],
                    alpha=0.6,
                    label=f"{material}" if trial_name == "Trial 1" else None
                )

        # Plot formatting
        plt.title(f"Residuals for Bar {bar[-1]}")
        plt.xlabel("Applied Load (lbs)")
        plt.ylabel("Residual (Measured - Theoretical) [lbs]")
        plt.legend(title="Material", loc="best")
        plt.grid(True, linestyle=":", alpha=0.7)
        plt.tight_layout()

        if save_fig:
            plt.savefig(f"residuals_{bar}.png")

        plt.show()

    return residuals



theoretical_funcs = {
    'F5': lambda load: -load,
    'F6': lambda load: load / 2,
    'F7': lambda load: load / np.sqrt(2)
}

#Plot the truss data
plot_truss_data(steelDat, alumData, theoretical_funcs)

#Plot the displacement data
plot_load_displacement(steelDat, alumData)

#Plot the residuals
residuals = plot_bar_residuals(steelDat, alumData, theoretical_funcs, save_fig=True)
print(f"The residuals:")
print(residuals)

#print out percent errors/differences
print("\n--- % Difference for Steel ---")
steel_mse = compute_average_percent_error(steelDat, theoretical_funcs)
print("\n--- % Difference for Aluminum ---")
alum_mse = compute_average_percent_error(alumData, theoretical_funcs)
