#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def delta_psi(z, eps0):
    """
    Idealized Psi--Continuum response signature.

    Parameters
    ----------
    z : array_like
        Redshift.
    eps0 : float
        Response parameter epsilon_0.

    Returns
    -------
    Delta_Psi(z) : array_like
        Dimensionless response signature.
    """
    return eps0 / (1.0 + z)


# This script produces an illustrative response curve used for visualization
# in Psi–Continuum Cosmology v3. It is not used for parameter estimation.
def main():
    # Redshift range (low-z regime relevant for the response signature)
    z = np.linspace(0.0, 2.0, 500)

    # Representative values of the response parameter
    eps_list = [0.02, 0.03, 0.04]  # 2%, 3%, 4% at z = 0

    for eps0 in eps_list:
        plt.plot(
            z,
            100.0 * delta_psi(z, eps0),
            label=rf"$\varepsilon_0 = {eps0:.2f}$"
        )

    plt.xlabel(r"Redshift $z$")
    plt.ylabel(r"Response signature $\Delta_\Psi(z)$ [\%]")

    plt.xlim(0.0, 2.0)
    plt.ylim(0.0, 5.0)

    plt.legend(frameon=False)
    plt.tight_layout()

    plt.savefig("figures/delta_psi_idealized.pdf")
    plt.savefig("figures/delta_psi_idealized.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    main()
